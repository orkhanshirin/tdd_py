"""
TDD tutorial
"""

import operator
from functools import reduce
from unittest import TestCase, main


class TestMoney(TestCase):
    def test_multiplication(self):
        five_usd = Money(5, "USD")
        ten_usd = Money(10, "USD")
        self.assertEqual(ten_usd, five_usd.times(2))

    def test_multiplication_eur(self):
        ten_eur = Money(10, "EUR")
        twenty_eur = ten_eur.times(2)
        self.assertEqual(20, twenty_eur.amount)
        self.assertEqual("EUR", twenty_eur.currency)

    def test_division(self):
        original_money = Money(4002, "KRW")
        actual_money_after_division = original_money.divide(4)
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(
            expected_money_after_division.amount, actual_money_after_division.amount
        )
        self.assertEqual(
            expected_money_after_division.currency, actual_money_after_division.currency
        )

    def test_addition(self):
        five_usd = Money(5, "USD")
        ten_usd = Money(10, "USD")
        fifteen_usd = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(five_usd, ten_usd)
        self.assertEqual(fifteen_usd, portfolio.evaluate("USD"))


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)


class Portfolio:
    def __init__(self):
        self.money = []

    def add(self, *money):
        self.money.extend(money)

    def evaluate(self, currency):
        total = reduce(operator.add, map(lambda m: m.amount, self.money), 0)
        return Money(total, currency)


if __name__ == "__main__":
    main()
