import enum

import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.accounts.account import Account, AccountType
from treasury_prime_py.models.base import SubObject
from treasury_prime_py.models.simulations.shared import Simulation


class WireSimulationType(enum.Enum):
    """https://developers.treasuryprime.com/docs/wire-simulations#wire-simulation-types"""

    PROCESSING_SENT = enum.auto()
    PROCESSING_VOIDED = enum.auto()
    INCOMING_WIRE = enum.auto()

    def __str__(self):
        return f"wire.{self.name.lower()}"


class WireSimulation(Simulation):
    """https://developers.treasuryprime.com/docs/wire-simulations"""

    @classmethod
    def random_simulation_body(cls, wire_id=None):
        return {"wire_id": wire_id}


class IncomingWireSimulationBankData(SubObject):
    @classmethod
    def random_body(
        cls,
        bank_data_account_number=None,
        bank_data_account_type=None,
        bank_data_address=None,
        bank_data_bank_name=None,
        bank_data_routing_number=None,
        **kwargs,
    ):
        bank_data_account_number = (
            tp_random.account_number()
            if bank_data_account_number is None
            else bank_data_account_number
        )
        bank_data_account_type = (
            AccountType.CHECKING
            if bank_data_account_type is None
            else bank_data_account_type
        )
        bank_data_address = (
            [v for v in tp_random.address().values() if v is not None]
            if bank_data_address is None
            else bank_data_address
        )
        bank_data_bank_name = (
            tp_random.bank_name()
            if bank_data_bank_name is None
            else bank_data_bank_name
        )
        bank_data_routing_number = (
            tp_random.routing_number()
            if bank_data_routing_number is None
            else bank_data_routing_number
        )

        return {
            "account_number": bank_data_account_number,
            "account_type": str(bank_data_account_type),
            "address": bank_data_address,
            "bank_name": bank_data_bank_name,
            "routing_number": bank_data_routing_number,
        }


class IncomingWireSimulationOriginator(SubObject):
    @classmethod
    def random_body(
        cls,
        originator_address=None,
        originator_name=None,
        originator_bank_data=None,
        **kwargs,
    ):
        originator_address = (
            [v for v in tp_random.address().values() if v is not None]
            if originator_address is None
            else originator_address
        )
        originator_name = (
            tp_random.company_name() if originator_name is None else originator_name
        )
        originator_bank_data = (
            IncomingWireSimulationBankData.random_body(**kwargs)
            if originator_bank_data is None
            else originator_bank_data
        )

        return {
            "address": originator_address,
            "name": originator_name,  # wrong description and is not optional
            "bank_data": originator_bank_data,  # misspelled description
        }


class IncomingWireSimulation(Simulation):
    """https://developers.treasuryprime.com/docs/wire-simulations#create-an-incoming-wire-simulation"""

    @classmethod
    def random_simulation_body(
        cls,
        account_id=None,
        amount=None,
        originator=None,
        originator_to_beneficiary_info=None,
        **kwargs,
    ):
        account_id = Account.fake_id() if account_id is None else account_id
        amount = tp_random.amount() if amount is None else amount
        originator = (
            IncomingWireSimulationOriginator.random_body(**kwargs)
            if originator is None
            else originator
        )
        originator_to_beneficiary_info = (
            "DEPOSIT"
            if originator_to_beneficiary_info is None
            else originator_to_beneficiary_info
        )

        return {
            "account_id": account_id,
            "amount": amount,
            "originator": originator,
            "originator_to_beneficiary_info": originator_to_beneficiary_info,
        }

    @classmethod
    def random_body(cls, **kwargs):
        return super().random_body(
            simulation_type=WireSimulationType.INCOMING_WIRE, **kwargs
        )
