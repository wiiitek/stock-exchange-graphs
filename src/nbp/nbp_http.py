import json
import urllib.request


def _call_for_currency(url: str):
    request = urllib.request.urlopen(url)
    result = json.load(request)
    return result
