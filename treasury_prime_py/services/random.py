import logging
import os
import random
import re
import string

import shortuuid
from faker import Faker

from treasury_prime_py.services.constants import ABA_ROUTING_NUMS

LOGGER = logging.getLogger(__name__)
DEFAULT_LOCALE = os.getenv("DEFAULT_LOCALE", "en_US")
FAKER = Faker(DEFAULT_LOCALE)
LOGGER.info(f"Setting fake data locale for {FAKER.current_country()}")


def credit_card_number():
    return FAKER.credit_card_number()


def credit_card_cvc():
    return FAKER.credit_card_security_code()


def credit_card_expire():
    return FAKER.credit_card_expire()


def date_of_birth():
    return str(FAKER.date_of_birth(None, 21, 100))


def email(domain=None):
    return FAKER.email(safe=True, domain=None)


def first_name():
    return FAKER.first_name()


def last_name():
    return FAKER.last_name()


def us_phone_number():
    return FAKER.phone_number()


def citizenship():
    return FAKER.current_country_code()


def title():
    return FAKER.job()


def naics():
    return str(FAKER.random_int(1, 100))


def address(country_code="US"):
    full_address = FAKER.address()
    while "FPO" in full_address or " Box " in full_address:
        full_address = FAKER.address()
    full_address_array = full_address.split("\n")
    street_line = (full_address_array[0]).strip()
    city_state_zip = full_address_array[1]
    city = city_state_zip.split(",")[0]
    if len(street_line) > 35:
        street_line = street_line[0:35]
    if len(city) > 18:
        city = city[0:18]
    state = (re.findall("[A-Z]{2}", city_state_zip.split(",")[1]))[0]
    zipp = (re.findall("\\d{5}", city_state_zip.split(",")[1]))[0]
    if country_code != "US":
        state = None
    return {
        "street_line_1": street_line,
        "street_line_2": None,
        "city": city,
        "state": state,
        "postal_code": zipp,
        "country": country_code,
    }


def zip_code():
    return FAKER.postalcode()


def tin(status=None):
    """
    Creates tin/ssn for status simulation

    Approved    1xx-xx-xxxx
    Manual Review   2xx-xx-xxxx
    Processing  3xx-xx-xxxx
    Rejected    4xx-xx-xxxx
    Submitted   5xx-xx-xxxx

    https://developers.treasuryprime.com/docs/apply-testing#personal-application-testing
    https://developers.treasuryprime.com/docs/apply-testing#business-application-testing
    """
    # Avoid circular import
    from treasury_prime_py.models.apply.account_application import (
        AccountApplicationStatus,
    )

    status = AccountApplicationStatus.APPROVED if status is None else status
    return (status.tin_prefix_simulation + FAKER.ssn()[1:]).replace("-", "")


def account_number():
    return FAKER.aba()[0:8]


def full_name():
    return first_name() + " " + last_name()


def routing_number():
    index = FAKER.random_int(0, len(ABA_ROUTING_NUMS) - 1)
    return ABA_ROUTING_NUMS[index]


def amount():
    amount = float(FAKER.random_int(1, 5000))
    return f"{amount}0"


def pseudoword(length):
    return FAKER.unique.text(length).lower()


def text(length):
    return FAKER.lexify(text="?" * length)


def company_name():
    return FAKER.company()


def company_id():
    return str(FAKER.random_int(1000000000, 9999999999))


def bank_name():
    return company_name() + " Bank"


def url():
    return FAKER.url()


def characters(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length))


def legal_structure():
    list_of_legal_structure = [
        "ccorp",
        "corp",
        "estate",
        "foreign_entity",
        "llc",
        "llp",
        "lp",
        "nonprofit",
        "partnership",
        "scheme",
        "scorp",
        "soleprop",
        "trust",
    ]
    random_index = FAKER.random_int(0, len(list_of_legal_structure) - 1)
    return list_of_legal_structure[random_index]


def model_id(id_prefix):
    return id_prefix + "fake" + shortuuid.uuid()[:10]


def plaid_token():
    return "process-sandbox-" + uuid()


def uuid():
    return FAKER.uuid4()
