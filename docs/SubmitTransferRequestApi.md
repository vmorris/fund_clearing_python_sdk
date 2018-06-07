# fund_clearing_python_sdk.SubmitTransferRequestApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_transfer_request_create**](SubmitTransferRequestApi.md#submit_transfer_request_create) | **POST** /SubmitTransferRequest | Create a new instance of the model and persist it into the data source.
[**submit_transfer_request_find**](SubmitTransferRequestApi.md#submit_transfer_request_find) | **GET** /SubmitTransferRequest | Find all instances of the model matched by filter from the data source.
[**submit_transfer_request_find_by_id**](SubmitTransferRequestApi.md#submit_transfer_request_find_by_id) | **GET** /SubmitTransferRequest/{id} | Find a model instance by {{id}} from the data source.


# **submit_transfer_request_create**
> SubmitTransferRequest submit_transfer_request_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SubmitTransferRequestApi()
data = fund_clearing_python_sdk.SubmitTransferRequest() # SubmitTransferRequest | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.submit_transfer_request_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmitTransferRequestApi->submit_transfer_request_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SubmitTransferRequest**](SubmitTransferRequest.md)| Model instance data | [optional] 

### Return type

[**SubmitTransferRequest**](SubmitTransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_transfer_request_find**
> list[SubmitTransferRequest] submit_transfer_request_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SubmitTransferRequestApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.submit_transfer_request_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmitTransferRequestApi->submit_transfer_request_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[SubmitTransferRequest]**](SubmitTransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_transfer_request_find_by_id**
> SubmitTransferRequest submit_transfer_request_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SubmitTransferRequestApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.submit_transfer_request_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmitTransferRequestApi->submit_transfer_request_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**SubmitTransferRequest**](SubmitTransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

