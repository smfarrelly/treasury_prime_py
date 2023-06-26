import logging

import requests

from treasury_prime_py.services.config import fetch_auth, make_url

LOGGER = logging.getLogger(__name__)
s = requests.Session()


class RequestsApi:
    """Class for session persistence and connection pooling"""

    def __init__(self, config, headers=None, **kwargs):
        self.session = requests.Session()
        self.base_url = config.base_url
        self.session.auth = config.auth
        self.headers = {} if headers is None else headers
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def request(self, method, url, **kwargs):
        return self.session.request(method, self.base_url + url, **kwargs)

    def head(self, url, **kwargs):
        return self.session.head(self.base_url + url, **kwargs)

    def get(self, url, **kwargs):
        return self.session.get(self.base_url + url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(self.base_url + url, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(self.base_url + url, **kwargs)

    def patch(self, url, **kwargs):
        return self.session.patch(self.base_url + url, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(self.base_url + url, **kwargs)

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination


def get(url, **kwargs):
    return requests.get(make_url(url), auth=fetch_auth(), **kwargs)


def post(url, **kwargs):
    return requests.post(make_url(url), auth=fetch_auth(), **kwargs)


def put(url, **kwargs):
    return requests.put(make_url(url), auth=fetch_auth(), **kwargs)


def patch(url, **kwargs):
    return requests.patch(make_url(url), auth=fetch_auth(), **kwargs)


def delete(url, **kwargs):
    return requests.delete(make_url(url), auth=fetch_auth(), **kwargs)
