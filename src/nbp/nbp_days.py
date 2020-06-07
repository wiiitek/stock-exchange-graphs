from datetime import date, timedelta


def _last_monday(day: date):
    result: date
    delta = day.weekday()
    result = day - timedelta(days=delta)
    return result
