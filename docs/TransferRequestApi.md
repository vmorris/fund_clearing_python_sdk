# fund_clearing_python_sdk.TransferRequestApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_request_create**](TransferRequestApi.md#transfer_request_create) | **POST** /TransferRequest | Create a new instance of the model and persist it into the data source.
[**transfer_request_delete_by_id**](TransferRequestApi.md#transfer_request_delete_by_id) | **DELETE** /TransferRequest/{id} | Delete a model instance by {{id}} from the data source.
[**transfer_request_exists**](TransferRequestApi.md#transfer_request_exists) | **HEAD** /TransferRequest/{id} | Check whether a model instance exists in the data source.
[**transfer_request_find**](TransferRequestApi.md#transfer_request_find) | **GET** /TransferRequest | Find all instances of the model matched by filter from the data source.
[**transfer_request_find_by_id**](TransferRequestApi.md#transfer_request_find_by_id) | **GET** /TransferRequest/{id} | Find a model instance by {{id}} from the data source.
[**transfer_request_replace_by_id**](TransferRequestApi.md#transfer_request_replace_by_id) | **PUT** /TransferRequest/{id} | Replace attributes for a model instance and persist it into the data source.


# **transfer_request_create**
> TransferRequest transfer_request_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.TransferRequestApi()
data = fund_clearing_python_sdk.TransferRequest() # TransferRequest | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.transfer_request_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferRequestApi->transfer_request_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TransferRequest**](TransferRequest.md)| Model instance data | [optional] 

### Return type

[**TransferRequest**](TransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_delete_by_id**
> object transfer_request_delete_by_id(id)

Delete a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.TransferRequestApi()
id = 'id_example' # str | Model id

try:
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.transfer_request_delete_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferRequestApi->transfer_request_delete_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_exists**
> InlineResponse200 transfer_request_exists(id)

Check whether a model instance exists in the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.TransferRequestApi()
id = 'id_example' # str | Model id

try:
    # Check whether a model instance exists in the data source.
    api_response = api_instance.transfer_request_exists(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferRequestApi->transfer_request_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_find**
> list[TransferRequest] transfer_request_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.TransferRequestApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.transfer_request_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferRequestApi->transfer_request_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[TransferRequest]**](TransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_find_by_id**
> TransferRequest transfer_request_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.TransferRequestApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.transfer_request_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferRequestApi->transfer_request_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**TransferRequest**](TransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_request_replace_by_id**
> TransferRequest transfer_request_replace_by_id(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.TransferRequestApi()
id = 'id_example' # str | Model id
data = fund_clearing_python_sdk.TransferRequest() # TransferRequest | Model instance data (optional)

try:
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.transfer_request_replace_by_id(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferRequestApi->transfer_request_replace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**TransferRequest**](TransferRequest.md)| Model instance data | [optional] 

### Return type

[**TransferRequest**](TransferRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

