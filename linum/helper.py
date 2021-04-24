from datetime import timedelta, date


def days_in_month(date_: date.today()):
    year = date_.year
    month = date_.month
    next_month = month + 1 if month + 1 < 13 else 1
    d = date(year=year, month=next_month, day=1)
    last_day_in_month = d - timedelta(days=1)
    return last_day_in_month.day
