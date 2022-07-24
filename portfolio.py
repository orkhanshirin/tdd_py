"""
Portfolio class defined here
"""
from typing import Union

from money import Money


class Portfolio:
    def __init__(self) -> None:
        self.moneys = []
        self._eur_to_usd = 1.2

    def add(self, *money) -> None:
        self.moneys.extend(money)

    def evaluate(self, bank, currency) -> Union[Money, None]:
        total = 0.0
        failures = []
        for money in self.moneys:
            try:
                total += bank.convert(money, currency).amount
            except Exception as exc:
                failures.append(exc)

        if len(failures) == 0:
            return Money(total, currency)

        failure_msg = ", ".join(f.args[0] for f in failures)
        raise Exception(f"Missing exchange rate(s):[{failure_msg}]")
