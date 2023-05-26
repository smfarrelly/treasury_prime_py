:construction: Project is very much a WIP! :construction:

# Treasury Prime Py

A Python package for interacting with the Treasury Prime developer APIs.

The API reference docs can be found here:

- [Developer Docs](https://developers.treasuryprime.com/docs/introduction])
- [Postman Collection](https://postman.com/treasuryprime/workspace/treasury-prime-public-workspace/collection/16971508-7785a4b3-8e10-4c85-ba87-18c979afa06c)

## Getting Started

1) [Install Poetry](https://python-poetry.org/docs/)
2) Clone this project
3) `poetry shell`
4) `poetry install`
5) Python... (profit?)

## Running Tests

Someone should write some...

## Creating Random/Sample Data

Each of the "model" classes contain a `random_body` class method used for generating sample data applicable to the class.
You can even generate and POST this data to the API (probably Treasury Prime's sandbox developer environment) by calling
the `create` class method.

### Need a key?

You [can get one](https://developers.treasuryprime.com/guides/getting-started) for the developer sandbox.

### Example REPL usage

```
% export TP_PY_KEY=<your key>
% export TP_PY_SECRET=<your secret>
% ipython
Python 3.11.3 (main, Apr  7 2023, 21:05:46) [Clang 14.0.0 (clang-1400.0.29.202)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.13.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from treasury_prime_py.models.payments.counterparty import Counterparty

In [2]: from pprint import pprint

In [3]: without_post = Counterparty.create(with_request=False)

In [4]: pprint(without_post.__dict__)
{'ach': {'account_number': '12235704',
         'account_type': 'checking',
         'routing_number': '041002711'},
 'created_at': datetime.datetime(2023, 5, 26, 6, 12, 18, 352034),
 'id': 'cp_fakeaShQHsedge',
 'name_on_account': 'Daniel Oliver',
 'plaid_token': 'process-sandbox-6a609901-99c6-406e-8b85-d4fc52e9d78c',
 'updated_at': datetime.datetime(2023, 5, 26, 6, 12, 18, 352034),
 'wire': {'account_number': '12235704',
          'account_type': 'checking',
          'address_on_account': {'city': 'West Madisonberg',
                                 'country': 'US',
                                 'postal_code': '43993',
                                 'state': 'UT',
                                 'street_line_1': '20012 Melissa Haven Suite '
                                                  '660',
                                 'street_line_2': None},
          'bank_address': {'city': 'Richardfurt',
                           'country': 'US',
                           'postal_code': '20966',
                           'state': 'OR',
                           'street_line_1': '491 Michael Cove Suite 744',
                           'street_line_2': None},
          'bank_name': 'Williams, Carpenter and Alvarez Bank',
          'routing_number': '041002711'}}

In [5]: with_post = Counterparty.create(with_request=True)

In [6]: pprint(with_post.__dict__)
{'ach': {'account_number': '05682521',
         'account_type': 'checking',
         'routing_number': '123103729'},
 'created_at': '2023-05-26T06:12:34Z',
 'id': 'cp_11j70kejme49f4',
 'name_on_account': 'David Schneider',
 'plaid_processor_token': None,
 'updated_at': '2023-05-26T06:12:34Z',
 'userdata': None,
 'wire': {'account_number': '05682521',
          'address_on_account': {'city': 'North Mitchellberg',
                                 'country': 'US',
                                 'postal_code': '53509',
                                 'state': 'DC',
                                 'street_line_1': '39621 Chelsea Inlet Apt. '
                                                  '444',
                                 'street_line_2': None},
          'bank_address': {'city': 'Benjaminfurt',
                           'country': 'US',
                           'postal_code': '64134',
                           'state': 'PA',
                           'street_line_1': '4295 Gary Mall',
                           'street_line_2': None},
          'bank_name': 'Miller and Sons Bank',
          'routing_number': '123103729'}}

```



More to come...
