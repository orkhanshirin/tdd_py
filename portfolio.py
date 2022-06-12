"""
Portfolio class defined here
"""
import operator
from functools import reduce

from money import Money


class Portfolio:
    def __init__(self):
        self.money = []
        self._eur_to_usd = 1.2

    def __convert(self, _money, _currency):
        exchange_rates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if _money.currency == _currency:
            return _money.amount
        else:
            key = _money.currency + "->" + _currency
            return _money.amount * exchange_rates[key]

    def add(self, *money):
        self.money.extend(money)

    def evaluate(self, currency):
        total = reduce(
            operator.add, map(lambda m: self.__convert(m, currency), self.money), 0
        )
        return Money(total, currency)
