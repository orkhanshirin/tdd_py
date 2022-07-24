"""
TDD tutorial: Tests
"""

from re import compile
from unittest import TestCase, main

from bank import Bank
from money import Money
from portfolio import Portfolio


class TestMoney(TestCase):
    def setUp(self) -> None:
        self.bank = Bank()
        self.bank.add_exchange_rate("EUR", "USD", 1.2)
        self.bank.add_exchange_rate("USD", "KRW", 1100)

    def test_multiplication(self) -> None:
        five_usd = Money(5, "USD")
        ten_usd = Money(10, "USD")
        self.assertEqual(ten_usd, five_usd.times(2))
        ten_eur = Money(10, "EUR")
        twenty_eur = ten_eur.times(2)
        self.assertEqual(20, twenty_eur.amount)
        self.assertEqual("EUR", twenty_eur.currency)

    def test_division(self) -> None:
        original_money = Money(4002, "KRW")
        actual_money_after_division = original_money.divide(4)
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(
            expected_money_after_division.amount, actual_money_after_division.amount
        )
        self.assertEqual(
            expected_money_after_division.currency, actual_money_after_division.currency
        )

    def test_addition(self) -> None:
        five_usd = Money(5, "USD")
        ten_usd = Money(10, "USD")
        fifteen_usd = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(five_usd, ten_usd)
        self.assertEqual(fifteen_usd, portfolio.evaluate(self.bank, "USD"))

    def test_addition_usd_eur(self) -> None:
        five_usd = Money(5, "USD")
        ten_eur = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_usd, ten_eur)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate(self.bank, "USD")
        self.assertEqual(
            expected_value, actual_value, "%s != %s" % (expected_value, actual_value)
        )

    def test_addition_usd_krw(self) -> None:
        one_usd = Money(1, "USD")
        eleven_hundred_krw = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_usd, eleven_hundred_krw)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate(self.bank, "KRW")
        self.assertEqual(
            expected_value, actual_value, "%s != %s" % (expected_value, actual_value)
        )

    def test_addition_with_multi_missing_exchange_rates(self) -> None:
        one_usd = Money(1, "USD")
        one_eur = Money(1, "EUR")
        one_krw = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_usd, one_eur, one_krw)
        with self.assertRaisesRegex(
            Exception,
            compile(
                "Missing exchange rate\(s\):\[USD\->Kalganid, EUR\->Kalganid, KRW\->Kalganid]"
            ),
        ):
            portfolio.evaluate(self.bank, "Kalganid")

    def test_conversion_with_different_rates(self) -> None:
        ten_eur = Money(10, "EUR")
        self.assertEqual(self.bank.convert(ten_eur, "USD"), Money(12, "USD"))

        self.bank.add_exchange_rate("EUR", "USD", 1.3)
        self.assertEqual(self.bank.convert(ten_eur, "USD"), Money(13, "USD"))

    def test_conversion_with_missing_exchange_rate(self) -> None:
        ten_eur = Money(10, "EUR")
        with self.assertRaisesRegex(Exception, "EUR->Kalganid"):
            self.bank.convert(ten_eur, "Kalganid")


if __name__ == "__main__":
    main()
