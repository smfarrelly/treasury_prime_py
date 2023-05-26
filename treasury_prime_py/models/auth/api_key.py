import enum

from treasury_prime_py.models.base import Base
from treasury_prime_py.services.config import make_url


class AccountType(enum.Enum):
    CHECKING = enum.auto()
    SAVINGS = enum.auto()

    def __str__(self):
        return self.name.lower()


class ApiKey(Base):
    """https://developers.treasuryprime.com/guides/getting-started"""

    ID_PREFIX = "key_"
    _API_PATH = "/keys"

    @classmethod
    def create(cls, **kwargs):
        dashboard_url = make_url(cls._API_PATH).replace("//api.", "//developers.")
        raise NotImplementedError(f"Create key(s) via {dashboard_url}")
