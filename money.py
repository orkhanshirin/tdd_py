"""
Money class defined here
"""
from typing import Any, Union


class Money:
    def __init__(self, amount: Union[int, float], currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, other) -> bool:
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:0.2f}"

    def times(self, multiplier) -> Any:
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor) -> Any:
        return Money(self.amount / divisor, self.currency)
