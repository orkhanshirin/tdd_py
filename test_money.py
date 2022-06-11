"""
TDD tutorial
"""

from unittest import TestCase, main


class TestMoney(TestCase):
    def test_multiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEquals(10, tenner.amount)


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


if __name__ == "__main__":
    main()
