from treasury_prime_py.models.base import Base


class AccountProduct(Base):
    """https://developers.treasuryprime.com/docs/account-product"""

    ID_PREFIX = "apt_"
    _API_PATH = "/account_product"

    @classmethod
    def random_body(cls, **kwargs):
        raise NotImplementedError("TODO")
