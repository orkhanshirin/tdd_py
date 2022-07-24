"""
Bank object defined here.
"""
from typing import Union

from money import Money


class Bank:
    def __init__(self) -> None:
        self.exchange_rates = {}

    def add_exchange_rate(
        self, currency_from: str, currency_to: str, rate: float
    ) -> None:
        key = currency_from + "->" + currency_to
        self.exchange_rates[key] = rate

    def convert(self, a_money: Money, a_currency: str) -> Union[Money, None]:
        if a_money.currency == a_currency:
            return Money(a_money.amount, a_currency)

        key = a_money.currency + "->" + a_currency
        if key in self.exchange_rates:
            return Money(a_money.amount * self.exchange_rates[key], a_currency)
        raise Exception(key)
