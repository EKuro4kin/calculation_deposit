from datetime import datetime


def data_validation(initial_deposit: dict):
    """
    :param initial_deposit: dict
    :return: dict | str
    Функция отвечающая за валидацию данных.
    Принимает словарь с входными данными депозита, проводит проверку на корректный ввод данных и возвращает словарь
    с проверенными данными, если не обнаружена ошибка при вводе данных. При обнаружении ошибки ф-ция возвращает строку
    с описанием ошибки.
    """
    # Проверка корректности данных.
    try:
        date_str = initial_deposit['date']
        date_p = datetime.strptime(date_str, "%d.%m.%Y").date()
        periods = int(initial_deposit['periods'])
        amount = int(initial_deposit['amount'])
        rate = float(initial_deposit['rate'])
    except Exception as e:
        return str(e)

    # Проверяем выполнение условия валидации данных.
    if not 0 < periods <= 60 or periods == (True or False):
        return 'Количество месяцев по вкладу должно быть целым числом, в интервале от 0 до 60'

    if not 10000 <= amount <= 3000000:
        return 'Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000'

    if not 0 < rate <= 8 or periods == (True or False):
        return 'Процент по вкладу должен находится в интервале от 0 до 8'

    initial_deposit_verified = {
        'date': date_p.strftime('%d.%m.%Y'),
        'periods': periods,
        'amount': amount,
        'rate': rate
    }

    return initial_deposit_verified
