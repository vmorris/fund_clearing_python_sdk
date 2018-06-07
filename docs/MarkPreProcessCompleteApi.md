# fund_clearing_python_sdk.MarkPreProcessCompleteApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mark_pre_process_complete_create**](MarkPreProcessCompleteApi.md#mark_pre_process_complete_create) | **POST** /MarkPreProcessComplete | Create a new instance of the model and persist it into the data source.
[**mark_pre_process_complete_find**](MarkPreProcessCompleteApi.md#mark_pre_process_complete_find) | **GET** /MarkPreProcessComplete | Find all instances of the model matched by filter from the data source.
[**mark_pre_process_complete_find_by_id**](MarkPreProcessCompleteApi.md#mark_pre_process_complete_find_by_id) | **GET** /MarkPreProcessComplete/{id} | Find a model instance by {{id}} from the data source.


# **mark_pre_process_complete_create**
> MarkPreProcessComplete mark_pre_process_complete_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.MarkPreProcessCompleteApi()
data = fund_clearing_python_sdk.MarkPreProcessComplete() # MarkPreProcessComplete | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.mark_pre_process_complete_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkPreProcessCompleteApi->mark_pre_process_complete_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MarkPreProcessComplete**](MarkPreProcessComplete.md)| Model instance data | [optional] 

### Return type

[**MarkPreProcessComplete**](MarkPreProcessComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_pre_process_complete_find**
> list[MarkPreProcessComplete] mark_pre_process_complete_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.MarkPreProcessCompleteApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.mark_pre_process_complete_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkPreProcessCompleteApi->mark_pre_process_complete_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[MarkPreProcessComplete]**](MarkPreProcessComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_pre_process_complete_find_by_id**
> MarkPreProcessComplete mark_pre_process_complete_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.MarkPreProcessCompleteApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.mark_pre_process_complete_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkPreProcessCompleteApi->mark_pre_process_complete_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**MarkPreProcessComplete**](MarkPreProcessComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

