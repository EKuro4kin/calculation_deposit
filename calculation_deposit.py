from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculation_deposit(initial_deposit: dict):
    """
    :param initial_deposit: dict
    :return: dict
    Функция отвечающая за логику API приложения 'calculation_deposit'.
    Принимает словарь с входными данными депозита, обрабатывает их и возвращает словарь с количеством месяцев указанных
    в ключе 'periods', где значением является перерассчитанная сумма вклада 'amount' с учётом процента по вкладу 'rate'.
    Расчёт ведется с даты переданной в значении ключа 'date'.

    При возникновении исключения, функция отлавливает ошибку и возвращает строку с описанием ошибки.
    """
    count_periods = 0
    count_months = 0
    periods_dict = {}

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

    # Основная логика приложения. Рассчитывает по месяцам сумму вклада с учётом прибавленных процентов.
    while count_periods < periods:
        count_periods += 1
        count_months += 1
        amount = round(amount * (1 + rate/12/100), 2)
        if count_months > 12:
            count_months = 0
            date_p = date_p + relativedelta(month=1)
            date_p = date_p + relativedelta(years=+1)
        else:
            date_p = date_p + relativedelta(month=+count_months)
        date_p = date_p + relativedelta(day=31)
        date_f = datetime.strftime(date_p, '%d.%m.%Y')
        periods_dict[date_f] = amount

    return periods_dict
