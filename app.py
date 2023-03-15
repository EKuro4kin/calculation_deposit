import json
import os.path
from collections import OrderedDict

from flask import Flask, render_template, url_for, request, jsonify

from calculation_deposit import calculation_deposit

app = Flask(__name__)

picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder


initial_deposit = {}


@app.route('/')
@app.route('/deposit_entry')
def deposit_entry():
    """
    :return: страница .html с формой для заполнения данных на расчёт депозита
    Домашняя страница, которая даёт возможность ввести данные на расчёт депозита:
    date - дата заявки, periods - количество месяцев по вкладу, amount - сумма вклада, rate - процент по вкладу.
    """
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'calculator.jpg')
    return render_template('deposit_entry.html', pic=pic)


@app.route('/result_calculation_deposit', methods=['POST', 'GET'])
def result_calculation_deposit():
    """
    :return: json файл, с отображаемой суммой вклада на конец месяца, либо json файл с описанием исключения.
    Функция получает запрос метода post с данными полученными из форм ответа функции "deposit_entry",
    обрабатывает их - производя расчёт депозита, на выходе возвращает json файл с отображением суммы
    вклада на конец месяца.
    """
    if request.method == 'POST':
        initial_deposit['date'] = request.form['date']
        initial_deposit['periods'] = request.form['periods']
        initial_deposit['amount'] = request.form['amount']
        initial_deposit['rate'] = request.form['rate']

        try:
            new = OrderedDict(calculation_deposit(initial_deposit))
        except:
            return jsonify({'ValueError': calculation_deposit(initial_deposit)}), 400, \
                   print({'ValueError': calculation_deposit(initial_deposit)})            # Для отображения в терминале

        try:
            new = json.dumps((new), indent=3)
            return new, 200, print(new)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        pic = os.path.join(app.config['UPLOAD_FOLDER'], 'calculator.jpg')
        return render_template('deposit_entry.html', pic=pic)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
