"""
TDD tutorial: Tests
"""

from unittest import TestCase, main

from money import Money
from portfolio import Portfolio


class TestMoney(TestCase):
    def test_multiplication(self):
        five_usd = Money(5, "USD")
        ten_usd = Money(10, "USD")
        self.assertEqual(ten_usd, five_usd.times(2))
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

    def test_addition_usd_eur(self):
        five_usd = Money(5, "USD")
        ten_eur = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_usd, ten_eur)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate("USD")
        self.assertEqual(
            expected_value, actual_value, "%s != %s" % (expected_value, actual_value)
        )

    def test_addition_usd_krw(self):
        one_usd = Money(1, "USD")
        eleven_hundred_krw = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_usd, eleven_hundred_krw)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate("KRW")
        self.assertEqual(
            expected_value, actual_value, "%s != %s" % (expected_value, actual_value)
        )


if __name__ == "__main__":
    main()
