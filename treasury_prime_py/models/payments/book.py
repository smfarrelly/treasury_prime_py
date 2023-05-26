import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.account import Account
from treasury_prime_py.models.base import Base


class Book(Base):
    """https://developers.treasuryprime.com/docs/book"""

    ID_PREFIX = "book_"
    _API_PATH = "/book"

    @classmethod
    def random_body(
        cls,
        amount=None,
        from_account_id=None,
        to_account_id=None,
        userdata=None,
        **kwargs
    ):
        amount = tp_random.amount() if amount is None else amount
        from_account_id = (
            Account.fake_id() if from_account_id is None else from_account_id
        )
        to_account_id = Account.fake_id() if to_account_id is None else to_account_id
        userdata = (
            {"manual": True, "scheduled_settlement": 0}
            if userdata is None
            else userdata
        )
        return {
            "amount": amount,
            "from_account_id": from_account_id,
            "to_account_id": to_account_id,
            "userdata": userdata,
        }
