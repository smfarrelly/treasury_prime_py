import enum

import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.account import AccountType
from treasury_prime_py.models.payments.ach import ACHSECCode
from treasury_prime_py.models.payments.shared import PaymentDirection
from treasury_prime_py.models.simulations.shared import Simulation


class ACHSimulationType(enum.Enum):
    """https://developers.treasuryprime.com/docs/ach-simulations#ach-simulation-types"""

    PROCESSING_SENT = enum.auto()
    PROCESSING_RETURNED = enum.auto()
    INCOMING_ACH = enum.auto()

    def __str__(self):
        return f"ach.{self.name.lower()}"


class ACHSimulation(Simulation):
    """https://developers.treasuryprime.com/docs/ach-simulations"""

    @classmethod
    def random_simulation_body(cls, ach_id=None):
        return {"ach_id": ach_id}


class IncomingACHSimulation(Simulation):
    """https://developers.treasuryprime.com/docs/ach-simulations#create-an-incoming-ach-simulation"""

    @classmethod
    def random_simulation_body(
        cls,
        amount=None,
        account_type=None,
        direction=None,
        sec_code=None,
        account_number=None,
        company_name=None,
        company_description=None,
        company_id=None,
    ):
        amount = tp_random.amount() if amount is None else amount
        account_type = AccountType.CHECKING if account_type is None else account_type
        direction = PaymentDirection.CREDIT if direction is None else direction
        sec_code = ACHSECCode.WEB if sec_code is None else sec_code
        account_number = (
            tp_random.account_number() if account_number is None else account_number
        )
        company_name = (
            tp_random.company_name() if company_name is None else company_name
        )
        company_description = (
            tp_random.pseudoword(15)
            if company_description is None
            else company_description
        )
        company_id = tp_random.company_id() if company_id is None else company_id
        return {
            "account_number": account_number,
            "account_type": str(account_type),
            "amount": amount,
            "direction": str(direction),
            "sec_code": str(sec_code),
            "company_name": company_name,
            "company_desc": company_description,
            "company_id": company_id,
        }

    @classmethod
    def random_body(cls, **kwargs):
        return super().random_body(
            simulation_type=ACHSimulationType.INCOMING_ACH, **kwargs
        )
