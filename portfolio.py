"""
Portfolio class defined here
"""
import operator
from functools import reduce

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def __convert(self, _money, _currency):
        exchange_rates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if _money.currency == _currency:
            return _money.amount
        else:
            key = _money.currency + "->" + _currency
            return _money.amount * exchange_rates[key]

    def add(self, *money):
        self.moneys.extend(money)

    def evaluate(self, currency):
        total = 0.0
        failures = []
        for money in self.moneys:
            try:
                total += self.__convert(money, currency)
            except KeyError as err:
                failures.append(err)

        if len(failures) == 0:
            return Money(total, currency)

        failure_msg = ", ".join(f.args[0] for f in failures)
        raise Exception(f"Missing exchange rate(s):[{failure_msg}]")
