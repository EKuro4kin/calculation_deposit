import os.path
import unittest

from app import app

picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder

class TestAPI(unittest.TestCase):
    """
    Класс для тестирования http запросов приложения 'calculation_deposit'.
    Предусматривает обращение по адресам: '/', '/deposit_entry', '/result_calculation_deposit',
    с различными методами get и post (и разичными данными)
    """

    def test_home_route(self):
        """
        Функция тестирует метод get направленный на адрес '/'.
        Должен быть получен HTTP код состояния 200,
        который сообщает, что запрос клиента был успешно принят и обработан.
        """
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)


    def test_route_deposit_entry(self):
        """
        Функция тестирует метод get направленный на адрес '/deposit_entry'.
        Должен быть получен HTTP код состояния 200,
        который сообщает, что запрос клиента был успешно принят и обработан.
        """
        response = app.test_client().get('/deposit_entry')
        self.assertEqual(response.status_code, 200)

    def test_route_result_calculation_deposit(self):
        """
        Функция тестирует метод get направленный на адрес '/result_calculation_deposit'.
        Должен быть получен HTTP код состояния 200,
        который сообщает, что запрос клиента был успешно принят и обработан.
        """
        response = app.test_client().get('/result_calculation_deposit')
        self.assertEqual(response.status_code, 200)

    def test_method_post_result_calculation_deposit(self):
        """
        Функция тестирует метод post (с переданными данными) направленный на адрес '/result_calculation_deposit'.
        Должен быть получен корректный ответ с правильными данными и HTTP код состояния 200,
        который сообщает, что запрос клиента был успешно принят и обработан.
        """
        url = '/result_calculation_deposit'
        # Запрос
        data_request = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ответ, который должен быть получен при вышеуказанном запросе
        test_response = """{
   "31.01.2021": 10050.0,
   "28.02.2021": 10100.25,
   "31.03.2021": 10150.75
}"""

        response = app.test_client().post(url, data=data_request)
        self.assertEqual(response.get_data().decode('unicode-escape'), test_response)
        self.assertEqual(response.status_code, 200)

    def test_false_date_method_post(self):
        """
        Функция тестирует метод post (с некорректными данными) направленный на адрес '/result_calculation_deposit'.
        Должен быть получен ответ 'ValueError' обозначающий ошибку в переданных значениях,
        а так же HTTP код состояния 400,
        который сообщает, что запрос не может быть понят сервером из-за некорректного синтаксиса.
        """
        url = '/result_calculation_deposit'
        # Некорректный запрос
        data_request = {
            'date': 'fsfs',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ответ, который должен быть получен при вышеуказанном запросе
        test_response = """{"ValueError":"time data 'fsfs' does not match format '%d.%m.%Y'"}
"""

        response = app.test_client().post(url, data=data_request)
        self.assertEqual(response.get_data().decode('unicode-escape'), test_response)
        self.assertEqual(response.status_code, 400)

    def test_false_periods_method_post(self):
        """
        Функция тестирует метод post (с некорректными данными) направленный на адрес '/result_calculation_deposit'.
        Должен быть получен ответ 'ValueError' обозначающий ошибку в переданных значениях,
        а так же HTTP код состояния 400,
        который сообщает, что запрос не может быть понят сервером из-за неверно переданных значений.
        """
        url = '/result_calculation_deposit'
        # Некорректный запрос
        data_request = {
            'date': '31.01.2021',
            'periods': 88,
            'amount': 10000,
            'rate': 6
        }
        # Ответ, который должен быть получен при вышеуказанном запросе
        test_response = """{"ValueError":"Количество месяцев по вкладу должно быть целым числом, в интервале от 0 до 60"}
"""
        response = app.test_client().post(url, data=data_request)
        self.assertEqual(response.get_data().decode('unicode-escape'), test_response)
        self.assertEqual(response.status_code, 400)

    def test_false_amount_method_post(self):
        """
        Функция тестирует метод post (с некорректными данными) направленный на адрес '/result_calculation_deposit'.
        Должен быть получен ответ 'ValueError' обозначающий ошибку в переданных значениях,
        а так же HTTP код состояния 400,
        который сообщает, что запрос не может быть понят сервером из-за неверно переданных значений.
        """
        url = '/result_calculation_deposit'
        # Некорректный запрос
        data_request = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000000,
            'rate': 6
        }
        # Ответ, который должен быть получен при вышеуказанном запросе
        test_response = """{"ValueError":"Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000"}
"""
        response = app.test_client().post(url, data=data_request)
        self.assertEqual(response.get_data().decode('unicode-escape'), test_response)
        self.assertEqual(response.status_code, 400)

    def test_false_rate_method_post(self):
        """
        Функция тестирует метод post (с некорректными данными) направленный на адрес '/result_calculation_deposit'.
        Должен быть получен ответ 'ValueError' обозначающий ошибку в переданных значениях,
        а так же HTTP код состояния 400,
        который сообщает, что запрос не может быть понят сервером из-за неверно переданных значений.
        """
        url = '/result_calculation_deposit'
        # Некорректный запрос
        data_request = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': 0
        }
        # Ответ, который должен быть получен при вышеуказанном запросе
        test_response = """{"ValueError":"Процент по вкладу должен находится в интервале от 0 до 8"}
"""
        response = app.test_client().post(url, data=data_request)
        self.assertEqual(response.get_data().decode('unicode-escape'), test_response)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
