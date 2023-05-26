import enum

import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.accounts.account import Account
from treasury_prime_py.models.accounts.accounts.counterparty import Counterparty
from treasury_prime_py.models.base import Base, SubObject
from treasury_prime_py.models.payments.shared import PaymentDirection


class ACHSECCode(enum.Enum):
    """https://developers.treasuryprime.com/docs/ach#sec-codes"""

    CCD = enum.auto()
    CIE = enum.auto()
    PPD = enum.auto()
    TEL = enum.auto()
    WEB = enum.auto()

    def __str__(self):
        return self.name.lower()


class ACHService(enum.Enum):
    SAMEDAY = enum.auto()
    STANDARD = enum.auto()

    def __str__(self):
        return self.name.lower()


class ACHEntryPaymentType(enum.Enum):
    RECURRING = enum.auto()
    SINGLE = enum.auto()
    SUBSEQUENT = enum.auto()

    def __str__(self):
        return self.name.lower()


class ACHCIEDetails(SubObject):
    @classmethod
    def random_body(
        cls,
        individual_id_number=None,
        individual_name=None,
    ):
        individual_id_number = (
            tp_random.account_number()
            if individual_id_number is None
            else individual_id_number
        )
        individual_name = (
            tp_random.full_name() if individual_name is None else individual_name
        )
        return {
            "individual_id_number": individual_id_number,
            "individual_name": individual_name,
        }


class ACHTELDetails(SubObject):
    @classmethod
    def random_body(cls, payment_type=ACHEntryPaymentType.SINGLE):
        return {"payment_type": str(payment_type)}


class ACHWEBDetails(SubObject):
    @classmethod
    def random_body(cls, payment_type=ACHEntryPaymentType.SINGLE):
        return {"payment_type": str(payment_type)}


class ACH(Base):
    """https://developers.treasuryprime.com/docs/ach"""

    ID_PREFIX = "ach_"
    _API_PATH = "/ach"

    @classmethod
    def random_body(
        cls,
        account_id=None,
        amount=None,
        counterparty_id=None,
        direction=None,
        sec_code=None,
        sec_details=None,
        service=None,
        userdata=None,
        **kwargs
    ):
        account_id = Account.fake_id() if account_id is None else account_id
        amount = tp_random.amount() if amount is None else amount
        counterparty_id = (
            Counterparty.fake_id() if counterparty_id is None else counterparty_id
        )
        direction = PaymentDirection.CREDIT if direction is None else direction
        sec_code = ACHSECCode.WEB if sec_code is None else sec_code
        sec_details = ACHWEBDetails.random_body()
        service = ACHService.STANDARD if service is None else service
        userdata = (
            {"manual": True, "scheduled_settlement": 0}
            if userdata is None
            else userdata
        )
        return {
            "account_id": account_id,
            "amount": amount,
            "counterparty_id": counterparty_id,
            "direction": direction,
            "sec_code": sec_code,
            "sec_details": sec_details,
            "service": service,
            "userdata": userdata,
        }
