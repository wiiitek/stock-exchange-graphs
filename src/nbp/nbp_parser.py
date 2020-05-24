import json


def _currency_rate(currency, json_input):
    result: float
    data = json.loads(json_input)
    table = _find_table(data, 'A')
    day = _find_day(table)
    rate = _find_rate(table, currency)
    return day, rate


def _find_table(data, table_id):
    result = None
    for table in data:
        current_table_id = table['table']
        if current_table_id.lower() == table_id.lower():
            result = table
    return result


def _find_day(table):
    result = table['effectiveDate']
    return result


def _find_rate(table, currency_id):
    result = None
    rates = table['rates']
    for currency in rates:
        code = currency['code']
        if code.lower() == currency_id.lower():
            rate = currency['mid']
            result = rate
    return result
