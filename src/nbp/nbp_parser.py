import json


def _currency_rate(json_input) -> tuple:
    data = json.loads(json_input)
    single_data = data['rates'][0]
    day = single_data['effectiveDate']
    rate = single_data['mid']
    return day, rate


def _currency_rates(json_list):
    result = []
    for json_item in json_list:
        rate = _currency_rate(json_item)
        result.append(rate)
    # sot by first element in tuple
    result.sort(key=lambda tup: tup[0])
    return result
