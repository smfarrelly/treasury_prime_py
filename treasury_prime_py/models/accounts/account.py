import enum

from treasury_prime_py.models.base import Base


class AccountType(enum.Enum):
    CHECKING = enum.auto()
    SAVINGS = enum.auto()

    def __str__(self):
        return self.name.lower()


class Account(Base):
    """https://developers.treasuryprime.com/docs/account"""

    ID_PREFIX = "acct_"
    _API_PATH = "/account"

    @classmethod
    def random_body(cls, **kwargs):
        raise NotImplementedError("Check out ApplyAccountApplication")
