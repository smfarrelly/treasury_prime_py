import enum

import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.apply.person_application import PersonApplication
from treasury_prime_py.models.base import Base, SubObject


class BusinessApplicationPersonRole(enum.Enum):
    CONTROL_PERSON = enum.auto()
    SIGNER = enum.auto()

    def __str__(self):
        return self.name.lower()


class BusinessApplicationPerson(SubObject):
    @classmethod
    def random_body(
        cls,
        ownership_percentage=None,
        person_application_id=None,
        roles=None,
        title=None,
    ):
        ownership_percentage = (
            100 if ownership_percentage is None else ownership_percentage
        )
        person_application_id = (
            PersonApplication.create().id
            if person_application_id is None
            else person_application_id
        )
        roles = (
            [
                str(BusinessApplicationPersonRole.CONTROL_PERSON),
                str(BusinessApplicationPersonRole.SIGNER),
            ]
            if roles is None
            else roles
        )
        title = tp_random.title() if title is None else title

        return {
            "id": person_application_id,
            "roles": roles,
            "ownership_percentage": ownership_percentage,
            "title": title,
        }


class BusinessApplication(Base):
    """https://developers.treasuryprime.com/docs/business-application"""

    ID_PREFIX = "abus_"
    _API_PATH = "/apply/business_application"

    @classmethod
    def random_body(
        cls,
        country_code="US",
        description=None,
        email_address=None,
        established_on=None,
        incorporation_state=None,
        legal_structure=None,
        mailing_address=None,
        naics=None,
        naics_description=None,
        name=None,
        person_applications=None,
        phone_number=None,
        physical_address=None,
        tin=None,
        urls=None,
        **kwargs
    ):
        person_applications = (
            [BusinessApplicationPerson.random_body()]
            if person_applications is None
            else person_applications
        )
        addr = tp_random.address()
        description = tp_random.pseudoword(50) if description is None else description
        naics_description = (
            tp_random.pseudoword(15) if naics_description is None else naics_description
        )
        naics = tp_random.naics()
        email_address = tp_random.email() if email_address is None else email_address
        name = tp_random.company_name() if name is None else name
        urls = [tp_random.url()]
        phone_number = (
            tp_random.us_phone_number() if phone_number is None else phone_number
        )
        tin = tp_random.tin() if tin is None else tin
        legal_structure = tp_random.legal_structure()
        mailing_address = addr if mailing_address is None else mailing_address
        physical_address = addr if physical_address is None else physical_address
        incorporation_state = (
            addr["state"] if incorporation_state is None else incorporation_state
        )
        established_on = (
            tp_random.date_of_birth() if established_on is None else established_on
        )

        return {
            "description": description,
            "urls": urls,
            "phone_number": phone_number,
            "tin": tin,
            "legal_structure": legal_structure,
            "mailing_address": mailing_address,
            "naics_description": naics_description,
            "name": name,
            "physical_address": physical_address,
            "naics": naics,
            "incorporation_state": incorporation_state,
            "established_on": established_on,
            "person_applications": person_applications,
        }
