"""
Portfolio class defined here
"""
import operator
from functools import reduce

from money import Money


class Portfolio:
    def __init__(self):
        self.money = []

    def add(self, *money):
        self.money.extend(money)

    def evaluate(self, currency):
        total = reduce(operator.add, map(lambda m: m.amount, self.money), 0)
        return Money(total, currency)
