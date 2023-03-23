from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculation_deposit(initial_deposit_verified: dict) -> dict:
    """
    :param initial_deposit_verified: dict
    :return: dict
    Функция отвечающая за логику API приложения 'calculation_deposit'.
    Принимает словарь с входными проверенными данными по депозиту, обрабатывает их и возвращает словарь
    с количеством месяцев указанных в ключе 'periods', где значением является перерассчитанная сумма вклада 'amount'
    с учётом процента по вкладу 'rate'. Расчёт ведется с даты переданной в значении ключа 'date'.
    """
    count_periods = 0
    count_months = 0
    periods_dict = {}
    date_p = datetime.strptime(initial_deposit_verified['date'], "%d.%m.%Y").date()
    periods = initial_deposit_verified['periods']
    amount = initial_deposit_verified['amount']
    rate = initial_deposit_verified['rate']
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
