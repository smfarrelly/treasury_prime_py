import enum


class PaymentDirection(enum.Enum):
    CREDIT = enum.auto()
    DEBIT = enum.auto()
