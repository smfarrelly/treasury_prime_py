import logging
import os
from collections import namedtuple

LOGGER = logging.getLogger(__name__)


class ConfigError(Exception):
    pass


def fetch_base_url(base_url=None, default_url=None):
    if base_url is None:
        base_url = os.getenv("TP_PY_BASE_URL", default_url)
    if base_url:
        return base_url
    raise ConfigError("No base url found. Either pass to the Config or set as env var.")


def fetch_auth(api_key=None):
    if api_key is None:
        key = os.getenv("TP_PY_KEY")
        secret = os.getenv("TP_PY_SECRET")
        ApiKey = namedtuple("APIKey", ["key", "secret"])
        api_key = ApiKey(key, secret)
    if api_key.key and api_key.secret:
        return (api_key.key, api_key.secret)
    raise ConfigError(
        "No auth key or auth secret found. Either pass to the Config or set env vars."
    )


def make_url(path, base_url=None):
    base_url = fetch_base_url(base_url)
    return str(base_url) + path


class Config:
    _DEFAULT_BASE_URL = None

    def __init__(self, base_url=None, api_key=None, **kwargs):
        self.base_url = fetch_base_url(base_url, self._DEFAULT_BASE_URL)
        self.auth = fetch_auth(api_key)


class TreasuryPrimeSandboxAPIConfig(Config):
    """https://developers.treasuryprime.com/docs/introduction#authentication"""

    _DEFAULT_BASE_URL = "https://api.sandbox.treasuryprime.com"
