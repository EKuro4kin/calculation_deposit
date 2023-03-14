import unittest
from calculation_deposit import calculation_deposit


class TestCalculationDeposit(unittest.TestCase):
    """
    Класс для тестирования логики приложения.
    Тестирует на корректность входных данных в функцию 'calculation_deposit', верную обработку и возвращение
    ожидаемого ответа, который был запроектирован.
    """

    def test_date_true_format(self):
        """
        Проверка на правильность возвращаемого ответа, при корректном вводе данных,
        которые передаются в функцию 'calculation_deposit'.
        """
        # Корректные данные поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемый ответ.
        test_initial_deposit_ok = {'31.01.2021': 10050.0, '28.02.2021': 10100.25, '31.03.2021': 10150.75}
        self.assertEqual(calculation_deposit(initial_deposit), test_initial_deposit_ok)

    def test_date_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "date" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit), "time data '' does not match format '%d.%m.%Y'")

    def test_date_not_true_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "date" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': 'str_abcd',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit), "time data 'str_abcd' does not match format '%d.%m.%Y'")

    def test_date_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "date" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': True,
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit), 'strptime() argument 1 must be str, not bool')

    def test_periods_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': '',
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit), "invalid literal for int() with base 10: ''")

    def test_periods_type_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'calculation_deposit'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 'sdf',
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit_periods_str),
                         "invalid literal for int() with base 10: 'sdf'")

    def test_periods_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'calculation_deposit'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': True,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit_periods_str),
                         'Количество месяцев по вкладу должно быть целым числом, в интервале от 0 до 60')

    def test_periods_out_of_range(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "periods" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 67,
            'amount': 10000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit),
                         'Количество месяцев по вкладу должно быть целым числом, в интервале от 0 до 60')

    def test_amount_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': '',
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit), "invalid literal for int() with base 10: ''")

    def test_amount_type_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'calculation_deposit'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': "10df000",
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit_periods_str),
                         "invalid literal for int() with base 10: '10df000'")

    def test_amount_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'calculation_deposit'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': False,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit_periods_str),
                         'Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000')


    def test_amount_out_of_range(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "amount" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 100000000,
            'rate': 6
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit),
                         'Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000')

    def test_rate_no_data_available(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': ''
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit), "could not convert string to float: ''")

    def test_rate_type_str(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'calculation_deposit'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': "6t"
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit_periods_str),
                         "could not convert string to float: '6t'")

    def test_rate_type_bool(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'calculation_deposit'.
        initial_deposit_periods_str = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': False
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit_periods_str),
                         'Процент по вкладу должен находится в интервале от 0 до 8')

    def test_rate_out_of_range(self):
        """
        Проверка возвращаемого сообщения об ошибке, от функции 'calculation_deposit',
        полученного в ходе обработки некорректных данных.
        """
        # Некорректные данные в значении ключа "rate" поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': 62
        }
        # Ожидаемое сообщение об ошибке.
        self.assertEqual(calculation_deposit(initial_deposit),
                         'Процент по вкладу должен находится в интервале от 0 до 8')

    def test_count_months_periods(self):
        """Функция проверяет правильность счётчика даты. Тестирует, что на период 2 месяца произошло
        правильное добавление даты - которая должна отображать последний день 2 месяца."""
        # Корректные данные поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 3,
            'amount': 10000,
            'rate': 6
        }
        # Дата на период 2 месяца от даты заявки '31.01.2021' - равна '28.02.2021', следовательно ищем данный ключ в
        # итоговом словаре выходных данных, так же проверяя произведённый расчёт процентов.
        self.assertEqual(calculation_deposit(initial_deposit)['28.02.2021'],
                         10100.25)

    def test_count_years_periods(self):
        """Функция проверяет правильность счётчика даты. Тестирует, что на период 13 месяца произошло правильное
        добавление даты, отображающей правильный ход календаря,
        где год должен увеличиться на 1, а месяц уменьшиться до 1-го календарного."""
        # Корректные данные поступающие в функцию 'calculation_deposit'.
        initial_deposit = {
            'date': '31.01.2021',
            'periods': 13,
            'amount': 10000,
            'rate': 6
        }
        # Дата на период 13 месяца от даты заявки '31.01.2021' - равна '31.01.2022', следовательно ищем данный ключ в
        # итоговом словаре выходных данных, так же проверяя произведённый расчёт процентов.
        self.assertEqual(calculation_deposit(initial_deposit)['31.01.2022'],
                         10669.87)


if __name__ == '__main__':
    unittest.main()
