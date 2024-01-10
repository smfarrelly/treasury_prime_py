import enum

from treasury_prime_py.models.apply.account_product import AccountProduct
from treasury_prime_py.models.apply.business_application import (
    BusinessApplicationPersonRole,
)
from treasury_prime_py.models.apply.person_application import PersonApplication
from treasury_prime_py.models.base import Base, SubObject


class AccountApplicationPersonRole(enum.Enum):
    OWNER = enum.auto()
    MINOR = enum.auto()
    SIGNER = enum.auto()

    def __str__(self):
        return self.name.lower()


class AccountApplicationPerson(SubObject):
    @classmethod
    def random_body(cls, person_application_id=None, roles=None):
        person_application_id = (
            PersonApplication.create().id
            if person_application_id is None
            else person_application_id
        )
        roles = (
            [
                str(AccountApplicationPersonRole.OWNER),
                str(BusinessApplicationPersonRole.SIGNER),
            ]
            if roles is None
            else roles
        )

        return {"id": person_application_id, "roles": roles}


class AccountApplicationStatus(enum.Enum):
    APPROVED = 1
    MANUAL_REVIEW = 2
    PROCESSING = 3
    REJECTED = 4
    SUBMITTED = 5

    @property
    def tin_prefix_simulation(self):
        return str(self.value)


class AccountApplicationConfigError(Exception):
    pass


class AccountApplication(Base):
    """https://developers.treasuryprime.com/docs/account-application"""

    ID_PREFIX = "aact_"
    _API_PATH = "/apply/account_application"

    @classmethod
    def random_body(
        cls,
        account_product_id=None,
        business_application_id=None,
        deposit_id=None,
        person_applications=None,
        primary_person_application_id=None,
    ):
        account_product_id = (
            AccountProduct.fake_id()
            if account_product_id is None
            else account_product_id
        )
        body = {"account_id": None, "account_product_id": account_product_id}

        # Default to Person Application
        if business_application_id is None:
            person_applications = (
                [AccountApplicationPerson.random_body()]
                if person_applications is None
                else person_applications
            )
            body["person_applications"] = person_applications

        body["primary_person_application_id"] = (
            person_applications[0]["id"]
            if primary_person_application_id is None
            else primary_person_application_id
        )

        if deposit_id is not None:
            body["deposit_id"] = deposit_id
        if person_applications and business_application_id:
            raise AccountApplicationConfigError(
                "Business applications do not accept person_applications. "
                "Did you mean to set the primary_person_application_id?"
            )
        if business_application_id:
            body["business_application_id"] = business_application_id

        return body
