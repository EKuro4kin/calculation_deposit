from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculation_deposit(initial_deposit: dict):
    count_periods = 0
    count_months = 0
    periods_dict = {}
    try:
        date_str = initial_deposit['date']
        date_p = datetime.strptime(date_str, "%d.%m.%Y").date()
        periods = int(initial_deposit['periods'])
        amount = int(initial_deposit['amount'])
        rate = float(initial_deposit['rate'])
    except Exception as e:
        return e

    if not 0 < periods <= 60:
        return "Количество месяцев по вкладу должно составлять от 0 до 60"

    if not 10000 <= amount <= 3000000:
        return "Сумма вклада должна быть целым числом в интервале от 10 000 до 3 000 000"

    if not 0 < rate <= 8:
        return "Процент по вкладу должен находится в интервале от 0 до 8"

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
        date_f = datetime.strftime(date_p, "%d.%m.%Y")
        periods_dict[date_f] = amount

    return periods_dict
