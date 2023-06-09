import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.account import AccountType
from treasury_prime_py.models.base import Base, SubObject


class Deposit(Base):
    """https://developers.treasuryprime.com/docs/deposit"""

    ID_PREFIX = "adpt_"
    _API_PATH = "/apply/deposit"

    @classmethod
    def random_body(
        cls,
        ach=None,
        amount=None,
        card=None,
        name_on_account=None,
        userdata=None,
        **kwargs
    ):
        amount = tp_random.amount() if amount is None else amount
        name_on_account = (
            tp_random.full_name() if name_on_account is None else name_on_account
        )
        userdata = {} if userdata is None else userdata

        body = {
            "amount": amount,
            "name_on_account": name_on_account,
            "userdata": userdata,
        }

        if ach is not None and card is None:
            body["ach"] = ach
        elif card is not None and ach is None:
            body["card"] = card
        else:
            raise ValueError("Deposit requires one of ach or card to be set.")

        return body


class ACHDepositSubObject(SubObject):
    @classmethod
    def random_body(
        cls, account_number=None, account_type=None, routing_number=None, **kwargs
    ):
        account_number = (
            tp_random.account_number() if account_number is None else account_number
        )
        account_type = AccountType.CHECKING if account_type is None else account_type
        routing_number = (
            tp_random.routing_number() if routing_number is None else routing_number
        )

        return {
            "account_number": account_number,
            "account_type": str(account_type),
            "routing_number": routing_number,
        }


class ACHDeposit(Deposit):
    @classmethod
    def random_body(cls, ach=None, **kwargs):
        ach = ACHDepositSubObject.random_body(**kwargs) if ach is None else ach
        return super().random_body(ach=ach, **kwargs)


class CardDepositSubObject(SubObject):
    @classmethod
    def random_body(
        cls,
        card_number=None,
        cvc=None,
        expiration_month=None,
        expiration_year=None,
        zip_code=None,
        **kwargs
    ):
        card_number = (
            tp_random.credit_card_number() if card_number is None else card_number
        )
        cvc = tp_random.credit_card_cvc() if cvc is None else cvc
        expiration_month = (
            tp_random.credit_card_expire().split("/")[0]
            if expiration_month is None
            else expiration_month
        )
        expiration_year = (
            tp_random.credit_card_expire().split("/")[1]
            if expiration_year is None
            else expiration_year
        )
        zip_code = tp_random.zip_code() if zip_code is None else zip_code

        return {
            "card_number": card_number,
            "cvc": cvc,
            "expiration_month": expiration_month,
            "expiration_year": expiration_year,
            "zip_code": zip_code,
        }


class CardDeposit(Deposit):
    @classmethod
    def random_body(cls, card=None, **kwargs):
        card = CardDepositSubObject.random_body(**kwargs) if card is None else card
        return super().random_body(card=card, **kwargs)
