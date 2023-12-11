import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.account import Account
from treasury_prime_py.models.base import Base
from treasury_prime_py.models.payments.counterparty import Counterparty


class Wire(Base):
    """https://developers.treasuryprime.com/docs/wire"""

    ID_PREFIX = "wire_"
    _API_PATH = "/wire"

    @classmethod
    def random_body(
        cls, account_id=None, amount=None, counterparty_id=None, userdata=None, **kwargs
    ):
        account_id = Account.fake_id() if account_id is None else account_id
        amount = tp_random.amount() if amount is None else amount
        counterparty_id = (
            Counterparty.fake_id() if counterparty_id is None else counterparty_id
        )
        userdata = (
            {"manual": False, "scheduled_settlement": 0}
            if userdata is None
            else userdata
        )
        return {
            "account_id": account_id,
            "amount": amount,
            "counterparty_id": counterparty_id,
            "userdata": userdata,
        }
