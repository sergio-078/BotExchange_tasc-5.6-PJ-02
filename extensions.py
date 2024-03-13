import requests
import json
from config import currency

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты: {quote}.')
        try:
            base_ticker = currency[base]
        except KeyError:
            raise APIException(f'Не удалось распознать валюту: {base}. /values')

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise APIException(f'Не удалось распознать валюту: {quote}. /values')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось распознать число: {amount}.')

        url = f'https://api.tinkoff.ru/v1/currency_rates?from={base_ticker}&to={quote_ticker}'
        total_base = (requests.get(url).json()['payload']['rates'][2]['buy'])*amount


        return total_base
