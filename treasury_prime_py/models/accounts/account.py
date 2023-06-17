import enum

from treasury_prime_py.models.base import Base
from treasury_prime_py.models.transactions.transaction import Transaction


class AccountType(enum.Enum):
    CHECKING = enum.auto()
    SAVINGS = enum.auto()

    def __str__(self):
        return self.name.lower()


class AccountTransaction(Transaction):
    _API_PATH = "/account/{id}/transaction"

    @classmethod
    def get_by_id(cls, _id, client=None):
        return cls.super().get_by_id(_id, client=client)


class Account(Base):
    """https://developers.treasuryprime.com/docs/account"""

    ID_PREFIX = "acct_"
    _API_PATH = "/account"

    @classmethod
    def random_body(cls, **kwargs):
        raise NotImplementedError("Check out ApplyAccountApplication")

    @classmethod
    def get_transactions(cls, account_id, client=None):
        return AccountTransaction.get(
            client=client, format_url_kwargs={"id": account_id}
        )
