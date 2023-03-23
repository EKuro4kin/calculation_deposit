import unittest
from application_logic.data_validation import data_validation


class TestDataValidation(unittest.TestCase):
    """
    Класс для тестирования функуии 'data_validation'.
    Тестирует на корректность входные данные в функцию 'data_validation' и возвращение
    ожидаемого ответа, который был запроектирован.
    """

    def test_date_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "date" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit), "time data '' does not match format '%d.%m.%Y'")

    def test_date_not_true_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "date" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': 'str_abcd',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit), "time data 'str_abcd' does not match format '%d.%m.%Y'")

    def test_date_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "date" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': True,
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit), 'strptime() argument 1 must be str, not bool')

    def test_periods_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': '',
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit), "invalid literal for int() with base 10: ''")

    def test_periods_type_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'data_validation'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 'sdf',
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit_periods_str),
                         "invalid literal for int() with base 10: 'sdf'")

    def test_periods_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'data_validation'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': True,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit_periods_str),
                         'Количество месяцев по вкладу должно быть целым числом, в интервале от 0 до 60')

    def test_periods_out_of_range(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 67,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit),
                         'Количество месяцев по вкладу должно быть целым числом, в интервале от 0 до 60')

    def test_amount_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': '',
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit), "invalid literal for int() with base 10: ''")

    def test_amount_type_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'data_validation'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': "10df000",
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit_periods_str),
                         "invalid literal for int() with base 10: '10df000'")

    def test_amount_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'data_validation'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': False,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit_periods_str),
                         'Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000')


    def test_amount_out_of_range(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 100000000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit),
                         'Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000')

    def test_rate_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': ''
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit), "could not convert string to float: ''")

    def test_rate_type_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'data_validation'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': "6t"
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit_periods_str),
                         "could not convert string to float: '6t'")

    def test_rate_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'data_validation'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': False
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit_periods_str),
                         'Процент по вкладу должен находится в интервале от 0 до 8')

    def test_rate_out_of_range(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'data_validation',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'data_validation'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': 62
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(data_validation(initial_deposit),
                         'Процент по вкладу должен находится в интервале от 0 до 8')


if __name__ == '__main__':
    unittest.main()
