import enum

from treasury_prime_py.models.base import Base


class TransactionCategory(enum.Enum):
    FEES = enum.auto()
    INTEREST = enum.auto()
    NULL = enum.auto()

    def __str__(self):
        s = self.name.lower()
        s = None if s == "null" else s
        return s


class Transaction(Base):
    """https://developers.treasuryprime.com/docs/transaction"""

    ID_PREFIX = "ttx_"
    _API_PATH = "/transaction"

    @classmethod
    def random_body(cls, **kwargs):
        raise NotImplementedError("Transactions canmot be instantiated directly")
