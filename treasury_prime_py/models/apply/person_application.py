import treasury_prime_py.services.random as tp_random
from treasury_prime_py.models.base import Base


class PersonApplication(Base):
    """https://developers.treasuryprime.com/docs/person-application"""

    ID_PREFIX = "apsn_"
    _API_PATH = "/apply/person_application"

    @classmethod
    def random_body(
        cls,
        country_code=None,
        date_of_birth=None,
        email_address=None,
        first_name=None,
        last_name=None,
        phone_number=None,
        physical_address=None,
        tin=None,
        **kwargs
    ):
        country_code = tp_random.citizenship() if country_code is None else country_code
        date_of_birth = (
            tp_random.date_of_birth() if date_of_birth is None else date_of_birth
        )
        email_address = tp_random.email() if email_address is None else email_address
        first_name = tp_random.first_name() if first_name is None else first_name
        last_name = tp_random.last_name() if last_name is None else last_name
        phone_number = (
            tp_random.us_phone_number() if phone_number is None else phone_number
        )
        physical_address = (
            tp_random.address(country_code)
            if physical_address is None
            else physical_address
        )
        tin = tp_random.tin() if tin is None else tin

        return {
            "citizenship": country_code,
            "date_of_birth": date_of_birth,
            "email_address": email_address,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "physical_address": physical_address,
            "tin": tin,
        }
