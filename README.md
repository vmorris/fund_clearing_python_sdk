# fund-clearing-python-sdk
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import fund_clearing_python_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fund_clearing_python_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = fund_clearing_python_sdk.BankingParticipantApi()
data = fund_clearing_python_sdk.BankingParticipant() # BankingParticipant | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.banking_participant_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankingParticipantApi->banking_participant_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BankingParticipantApi* | [**banking_participant_create**](docs/BankingParticipantApi.md#banking_participant_create) | **POST** /BankingParticipant | Create a new instance of the model and persist it into the data source.
*BankingParticipantApi* | [**banking_participant_delete_by_id**](docs/BankingParticipantApi.md#banking_participant_delete_by_id) | **DELETE** /BankingParticipant/{id} | Delete a model instance by {{id}} from the data source.
*BankingParticipantApi* | [**banking_participant_exists**](docs/BankingParticipantApi.md#banking_participant_exists) | **HEAD** /BankingParticipant/{id} | Check whether a model instance exists in the data source.
*BankingParticipantApi* | [**banking_participant_find**](docs/BankingParticipantApi.md#banking_participant_find) | **GET** /BankingParticipant | Find all instances of the model matched by filter from the data source.
*BankingParticipantApi* | [**banking_participant_find_by_id**](docs/BankingParticipantApi.md#banking_participant_find_by_id) | **GET** /BankingParticipant/{id} | Find a model instance by {{id}} from the data source.
*BankingParticipantApi* | [**banking_participant_replace_by_id**](docs/BankingParticipantApi.md#banking_participant_replace_by_id) | **PUT** /BankingParticipant/{id} | Replace attributes for a model instance and persist it into the data source.
*BatchTransferRequestApi* | [**batch_transfer_request_create**](docs/BatchTransferRequestApi.md#batch_transfer_request_create) | **POST** /BatchTransferRequest | Create a new instance of the model and persist it into the data source.
*BatchTransferRequestApi* | [**batch_transfer_request_delete_by_id**](docs/BatchTransferRequestApi.md#batch_transfer_request_delete_by_id) | **DELETE** /BatchTransferRequest/{id} | Delete a model instance by {{id}} from the data source.
*BatchTransferRequestApi* | [**batch_transfer_request_exists**](docs/BatchTransferRequestApi.md#batch_transfer_request_exists) | **HEAD** /BatchTransferRequest/{id} | Check whether a model instance exists in the data source.
*BatchTransferRequestApi* | [**batch_transfer_request_find**](docs/BatchTransferRequestApi.md#batch_transfer_request_find) | **GET** /BatchTransferRequest | Find all instances of the model matched by filter from the data source.
*BatchTransferRequestApi* | [**batch_transfer_request_find_by_id**](docs/BatchTransferRequestApi.md#batch_transfer_request_find_by_id) | **GET** /BatchTransferRequest/{id} | Find a model instance by {{id}} from the data source.
*BatchTransferRequestApi* | [**batch_transfer_request_replace_by_id**](docs/BatchTransferRequestApi.md#batch_transfer_request_replace_by_id) | **PUT** /BatchTransferRequest/{id} | Replace attributes for a model instance and persist it into the data source.
*CompleteSettlementApi* | [**complete_settlement_create**](docs/CompleteSettlementApi.md#complete_settlement_create) | **POST** /CompleteSettlement | Create a new instance of the model and persist it into the data source.
*CompleteSettlementApi* | [**complete_settlement_find**](docs/CompleteSettlementApi.md#complete_settlement_find) | **GET** /CompleteSettlement | Find all instances of the model matched by filter from the data source.
*CompleteSettlementApi* | [**complete_settlement_find_by_id**](docs/CompleteSettlementApi.md#complete_settlement_find_by_id) | **GET** /CompleteSettlement/{id} | Find a model instance by {{id}} from the data source.
*CreateBatchApi* | [**create_batch_create**](docs/CreateBatchApi.md#create_batch_create) | **POST** /CreateBatch | Create a new instance of the model and persist it into the data source.
*CreateBatchApi* | [**create_batch_find**](docs/CreateBatchApi.md#create_batch_find) | **GET** /CreateBatch | Find all instances of the model matched by filter from the data source.
*CreateBatchApi* | [**create_batch_find_by_id**](docs/CreateBatchApi.md#create_batch_find_by_id) | **GET** /CreateBatch/{id} | Find a model instance by {{id}} from the data source.
*MarkPostProcessCompleteApi* | [**mark_post_process_complete_create**](docs/MarkPostProcessCompleteApi.md#mark_post_process_complete_create) | **POST** /MarkPostProcessComplete | Create a new instance of the model and persist it into the data source.
*MarkPostProcessCompleteApi* | [**mark_post_process_complete_find**](docs/MarkPostProcessCompleteApi.md#mark_post_process_complete_find) | **GET** /MarkPostProcessComplete | Find all instances of the model matched by filter from the data source.
*MarkPostProcessCompleteApi* | [**mark_post_process_complete_find_by_id**](docs/MarkPostProcessCompleteApi.md#mark_post_process_complete_find_by_id) | **GET** /MarkPostProcessComplete/{id} | Find a model instance by {{id}} from the data source.
*MarkPreProcessCompleteApi* | [**mark_pre_process_complete_create**](docs/MarkPreProcessCompleteApi.md#mark_pre_process_complete_create) | **POST** /MarkPreProcessComplete | Create a new instance of the model and persist it into the data source.
*MarkPreProcessCompleteApi* | [**mark_pre_process_complete_find**](docs/MarkPreProcessCompleteApi.md#mark_pre_process_complete_find) | **GET** /MarkPreProcessComplete | Find all instances of the model matched by filter from the data source.
*MarkPreProcessCompleteApi* | [**mark_pre_process_complete_find_by_id**](docs/MarkPreProcessCompleteApi.md#mark_pre_process_complete_find_by_id) | **GET** /MarkPreProcessComplete/{id} | Find a model instance by {{id}} from the data source.
*QueryApi* | [**query_batch_transfer_request_by_id**](docs/QueryApi.md#query_batch_transfer_request_by_id) | **GET** /queries/BatchTransferRequestById | Select a BatchTransferRequest by the UUID
*QueryApi* | [**query_batch_transfer_request_for_banks_in_state**](docs/QueryApi.md#query_batch_transfer_request_for_banks_in_state) | **GET** /queries/BatchTransferRequestForBanksInState | Select all BatchTransferRequests in a given state for two participating banks
*QueryApi* | [**query_batch_transfer_requests_by_bank_in_state**](docs/QueryApi.md#query_batch_transfer_requests_by_bank_in_state) | **GET** /queries/BatchTransferRequestsByBankInState | Select all BatchTransferRequests in a given state for a participating bank
*QueryApi* | [**query_transfer_requests_by_bank_in_state**](docs/QueryApi.md#query_transfer_requests_by_bank_in_state) | **GET** /queries/TransferRequestsByBankInState | Select all TransferRequests for a participating bank in a given state
*QueryApi* | [**query_transfer_requests_by_banks_in_state**](docs/QueryApi.md#query_transfer_requests_by_banks_in_state) | **GET** /queries/TransferRequestsByBanksInState | Select all TransferRequests for a participating bank in a given state
*SubmitTransferRequestApi* | [**submit_transfer_request_create**](docs/SubmitTransferRequestApi.md#submit_transfer_request_create) | **POST** /SubmitTransferRequest | Create a new instance of the model and persist it into the data source.
*SubmitTransferRequestApi* | [**submit_transfer_request_find**](docs/SubmitTransferRequestApi.md#submit_transfer_request_find) | **GET** /SubmitTransferRequest | Find all instances of the model matched by filter from the data source.
*SubmitTransferRequestApi* | [**submit_transfer_request_find_by_id**](docs/SubmitTransferRequestApi.md#submit_transfer_request_find_by_id) | **GET** /SubmitTransferRequest/{id} | Find a model instance by {{id}} from the data source.
*SystemApi* | [**system_bind_identity**](docs/SystemApi.md#system_bind_identity) | **POST** /system/identities/bind | Bind an identity to the specified participant
*SystemApi* | [**system_get_all_historian_records**](docs/SystemApi.md#system_get_all_historian_records) | **GET** /system/historian | Get all Historian Records from the Historian
*SystemApi* | [**system_get_all_identities**](docs/SystemApi.md#system_get_all_identities) | **GET** /system/identities | Get all identities from the identity registry
*SystemApi* | [**system_get_historian_record_by_id**](docs/SystemApi.md#system_get_historian_record_by_id) | **GET** /system/historian/{id} | Get the specified Historian Record from the Historian
*SystemApi* | [**system_get_identity_by_id**](docs/SystemApi.md#system_get_identity_by_id) | **GET** /system/identities/{id} | Get the specified identity from the identity registry
*SystemApi* | [**system_issue_identity**](docs/SystemApi.md#system_issue_identity) | **POST** /system/identities/issue | Issue an identity to the specified participant
*SystemApi* | [**system_ping**](docs/SystemApi.md#system_ping) | **GET** /system/ping | Test the connection to the business network
*SystemApi* | [**system_revoke_identity**](docs/SystemApi.md#system_revoke_identity) | **POST** /system/identities/{id}/revoke | Revoke the specified identity
*TransferRequestApi* | [**transfer_request_create**](docs/TransferRequestApi.md#transfer_request_create) | **POST** /TransferRequest | Create a new instance of the model and persist it into the data source.
*TransferRequestApi* | [**transfer_request_delete_by_id**](docs/TransferRequestApi.md#transfer_request_delete_by_id) | **DELETE** /TransferRequest/{id} | Delete a model instance by {{id}} from the data source.
*TransferRequestApi* | [**transfer_request_exists**](docs/TransferRequestApi.md#transfer_request_exists) | **HEAD** /TransferRequest/{id} | Check whether a model instance exists in the data source.
*TransferRequestApi* | [**transfer_request_find**](docs/TransferRequestApi.md#transfer_request_find) | **GET** /TransferRequest | Find all instances of the model matched by filter from the data source.
*TransferRequestApi* | [**transfer_request_find_by_id**](docs/TransferRequestApi.md#transfer_request_find_by_id) | **GET** /TransferRequest/{id} | Find a model instance by {{id}} from the data source.
*TransferRequestApi* | [**transfer_request_replace_by_id**](docs/TransferRequestApi.md#transfer_request_replace_by_id) | **PUT** /TransferRequest/{id} | Replace attributes for a model instance and persist it into the data source.


## Documentation For Models

 - [BankingParticipant](docs/BankingParticipant.md)
 - [BatchTransferRequest](docs/BatchTransferRequest.md)
 - [BindIdentityRequest](docs/BindIdentityRequest.md)
 - [CompleteSettlement](docs/CompleteSettlement.md)
 - [CreateBatch](docs/CreateBatch.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [IssueIdentityRequest](docs/IssueIdentityRequest.md)
 - [MarkPostProcessComplete](docs/MarkPostProcessComplete.md)
 - [MarkPreProcessComplete](docs/MarkPreProcessComplete.md)
 - [PingResponse](docs/PingResponse.md)
 - [Settlement](docs/Settlement.md)
 - [SubmitTransferRequest](docs/SubmitTransferRequest.md)
 - [Transfer](docs/Transfer.md)
 - [TransferRequest](docs/TransferRequest.md)
 - [UsdExchangeRate](docs/UsdExchangeRate.md)
 - [XAny](docs/XAny.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



