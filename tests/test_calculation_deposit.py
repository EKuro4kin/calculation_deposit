import unittest
from application_logic.calculation_deposit import calculation_deposit


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
