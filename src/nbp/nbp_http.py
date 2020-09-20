import json
import urllib.request


class NbpHttp(object):

    def call_for_currency(self, url: str):
        request = urllib.request.urlopen(url)
        result = json.load(request)
        return result
