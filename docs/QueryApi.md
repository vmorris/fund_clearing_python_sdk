# fund_clearing_python_sdk.QueryApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_batch_transfer_request_by_id**](QueryApi.md#query_batch_transfer_request_by_id) | **GET** /queries/BatchTransferRequestById | Select a BatchTransferRequest by the UUID
[**query_batch_transfer_request_for_banks_in_state**](QueryApi.md#query_batch_transfer_request_for_banks_in_state) | **GET** /queries/BatchTransferRequestForBanksInState | Select all BatchTransferRequests in a given state for two participating banks
[**query_batch_transfer_requests_by_bank_in_state**](QueryApi.md#query_batch_transfer_requests_by_bank_in_state) | **GET** /queries/BatchTransferRequestsByBankInState | Select all BatchTransferRequests in a given state for a participating bank
[**query_transfer_requests_by_bank_in_state**](QueryApi.md#query_transfer_requests_by_bank_in_state) | **GET** /queries/TransferRequestsByBankInState | Select all TransferRequests for a participating bank in a given state
[**query_transfer_requests_by_banks_in_state**](QueryApi.md#query_transfer_requests_by_banks_in_state) | **GET** /queries/TransferRequestsByBanksInState | Select all TransferRequests for a participating bank in a given state


# **query_batch_transfer_request_by_id**
> list[BatchTransferRequest] query_batch_transfer_request_by_id(batch_id)

Select a BatchTransferRequest by the UUID

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.QueryApi()
batch_id = 'batch_id_example' # str | 

try:
    # Select a BatchTransferRequest by the UUID
    api_response = api_instance.query_batch_transfer_request_by_id(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_batch_transfer_request_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 

### Return type

[**list[BatchTransferRequest]**](BatchTransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_batch_transfer_request_for_banks_in_state**
> list[BatchTransferRequest] query_batch_transfer_request_for_banks_in_state(error_unknown, error_unknown2, state)

Select all BatchTransferRequests in a given state for two participating banks

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.QueryApi()
error_unknown = 'error_unknown_example' # str | 
error_unknown2 = 'error_unknown_example' # str | 
state = 'state_example' # str | 

try:
    # Select all BatchTransferRequests in a given state for two participating banks
    api_response = api_instance.query_batch_transfer_request_for_banks_in_state(error_unknown, error_unknown2, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_batch_transfer_request_for_banks_in_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_unknown** | **str**|  | 
 **error_unknown2** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**list[BatchTransferRequest]**](BatchTransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_batch_transfer_requests_by_bank_in_state**
> list[BatchTransferRequest] query_batch_transfer_requests_by_bank_in_state(party, state)

Select all BatchTransferRequests in a given state for a participating bank

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.QueryApi()
party = 'party_example' # str | 
state = 'state_example' # str | 

try:
    # Select all BatchTransferRequests in a given state for a participating bank
    api_response = api_instance.query_batch_transfer_requests_by_bank_in_state(party, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_batch_transfer_requests_by_bank_in_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party** | **str**|  | 
 **state** | **str**|  | 

### Return type

[**list[BatchTransferRequest]**](BatchTransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_transfer_requests_by_bank_in_state**
> list[TransferRequest] query_transfer_requests_by_bank_in_state(bank)

Select all TransferRequests for a participating bank in a given state

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.QueryApi()
bank = 'bank_example' # str | 

try:
    # Select all TransferRequests for a participating bank in a given state
    api_response = api_instance.query_transfer_requests_by_bank_in_state(bank)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_transfer_requests_by_bank_in_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank** | **str**|  | 

### Return type

[**list[TransferRequest]**](TransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_transfer_requests_by_banks_in_state**
> list[TransferRequest] query_transfer_requests_by_banks_in_state(bank1, bank2, state, bank3, bank4, state2)

Select all TransferRequests for a participating bank in a given state

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.QueryApi()
bank1 = 'bank1_example' # str | 
bank2 = 'bank2_example' # str | 
state = 'state_example' # str | 
bank3 = 'bank2_example' # str | 
bank4 = 'bank1_example' # str | 
state2 = 'state_example' # str | 

try:
    # Select all TransferRequests for a participating bank in a given state
    api_response = api_instance.query_transfer_requests_by_banks_in_state(bank1, bank2, state, bank3, bank4, state2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_transfer_requests_by_banks_in_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank1** | **str**|  | 
 **bank2** | **str**|  | 
 **state** | **str**|  | 
 **bank3** | **str**|  | 
 **bank4** | **str**|  | 
 **state2** | **str**|  | 

### Return type

[**list[TransferRequest]**](TransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

