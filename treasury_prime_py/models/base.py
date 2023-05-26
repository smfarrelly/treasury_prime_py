import datetime as dt
import logging
from uuid import uuid4

from munch import Munch

import treasury_prime_py.services.requests_api as r
from treasury_prime_py.services.random import model_id

LOGGER = logging.getLogger(__name__)


class Base(Munch):
    ID_PREFIX = ""
    _API_PATH = None

    @classmethod
    def _req(cls, client=None):
        return r if client is None else client

    @classmethod
    def get_by_id(cls, _id, client=None):
        response = cls._req(client).get(f"{cls._API_PATH}/{_id}")
        return cls.fromDict(response.json())

    @classmethod
    def random_body(cls, *args, **kwargs):
        return {}

    @classmethod
    def fake_id(cls):
        return model_id(cls.ID_PREFIX)

    @classmethod
    def create(cls, body=None, headers=None, client=None, with_request=True, **kwargs):
        body = cls.random_body(**kwargs) if body is None else body
        if with_request:
            headers = {} if headers is None else headers
            headers["X-Idempotency-Key"] = str(uuid4())
            response = cls._req(client).post(cls._API_PATH, json=body, headers=headers)
            if response.ok:
                return cls.fromDict(response.json())
            LOGGER.error(
                f"FAILED to create {cls} - {cls._API_PATH}. "
                f"Status code:  {response.status_code} "
                f"Body: {response.text} request body: {body}"
            )
        else:
            body["id"] = cls.fake_id()
            now = dt.datetime.utcnow()
            body["created_at"] = now
            body["updated_at"] = now
            return cls.fromDict(body)


class SubObjectInitError(Exception):
    pass


class SubObject(Base):
    @classmethod
    def create(cls, with_request=False, **kwargs):
        if with_request:
            raise SubObjectInitError(
                f"{cls.__name__} sub-objects cannot be"
                f"instantiated directly via the API."
            )
        else:
            super(SubObject, cls).__init__(with_request=with_request, **kwargs)
