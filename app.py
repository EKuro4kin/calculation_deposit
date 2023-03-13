import json
import os.path
from datetime import datetime
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
    pic = os.path.join(app.config['UPLOAD_FOLDER'], 'calculator.jpg')
    return render_template('deposit_entry.html', pic=pic)


@app.route('/result_calculation_deposit', methods=['POST', 'GET'])
def result_calculation_deposit():
    if request.method == 'POST':
        initial_deposit['date'] = request.form['date']
        initial_deposit['periods'] = request.form['periods']
        initial_deposit['amount'] = request.form['amount']
        initial_deposit['rate'] = request.form['rate']

        try:
            new = OrderedDict(calculation_deposit(initial_deposit))
        except:
            return jsonify({'ValueError': calculation_deposit(initial_deposit)}), 400, \
                   print({'ValueError': calculation_deposit(initial_deposit)})

        try:
            new = json.dumps((new), indent=3)
            return new, 200, print(new)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        pic = os.path.join(app.config['UPLOAD_FOLDER'], 'calculator.jpg')
        return render_template('deposit_entry.html', pic=pic)


if __name__ == '__main__':
    app.run(debug=True)
