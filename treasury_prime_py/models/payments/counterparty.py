import enum

import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.account import AccountType
from treasury_prime_py.models.base import Base


class CounterpartyType(enum.Enum):
    ACH = enum.auto()
    WIRE = enum.auto()
    PLAID = enum.auto()
    ALL = enum.auto()


class Counterparty(Base):
    """https://developers.treasuryprime.com/docs/counterparty"""

    ID_PREFIX = "cp_"
    _API_PATH = "/counterparty"

    @classmethod
    def random_body(
        cls,
        account_number=None,
        account_type=AccountType.CHECKING,
        address_on_account=None,
        bank_address=None,
        bank_name=None,
        counterparty_type=CounterpartyType.ALL,
        name_on_account=None,
        plaid_token=None,
        routing_number=None,
        **kwargs
    ):
        name_on_account = (
            tp_random.full_name() if name_on_account is None else name_on_account
        )
        account_number = (
            tp_random.account_number() if account_number is None else account_number
        )
        routing_number = (
            tp_random.routing_number() if routing_number is None else routing_number
        )
        address_on_account = (
            tp_random.address() if address_on_account is None else address_on_account
        )
        bank_name = tp_random.bank_name() if bank_name is None else bank_name
        bank_address = tp_random.address() if bank_address is None else bank_address
        plaid_token = tp_random.plaid_token() if plaid_token is None else plaid_token
        body = {
            "name_on_account": name_on_account,
            "ach": None,
            "wire": None,
            "plaid_token": None,
        }
        ach = {
            "account_number": account_number,
            "account_type": str(account_type),
            "routing_number": routing_number,
        }
        wire = {
            "account_number": account_number,
            "account_type": str(account_type),
            "routing_number": routing_number,
            "address_on_account": address_on_account,
            "bank_name": bank_name,
            "bank_address": bank_address,
        }
        if counterparty_type == CounterpartyType.ALL:
            body.update({"ach": ach, "wire": wire, "plaid_token": plaid_token})
        elif counterparty_type == CounterpartyType.ACH:
            body.update({"ach": ach})
        elif counterparty_type == CounterpartyType.WIRE:
            body.update({"wire": wire})
        elif counterparty_type == CounterpartyType.PLAID:
            body.update({"plaid_token": plaid_token})

        return body
