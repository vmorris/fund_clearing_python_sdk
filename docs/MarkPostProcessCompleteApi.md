# fund_clearing_python_sdk.MarkPostProcessCompleteApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mark_post_process_complete_create**](MarkPostProcessCompleteApi.md#mark_post_process_complete_create) | **POST** /MarkPostProcessComplete | Create a new instance of the model and persist it into the data source.
[**mark_post_process_complete_find**](MarkPostProcessCompleteApi.md#mark_post_process_complete_find) | **GET** /MarkPostProcessComplete | Find all instances of the model matched by filter from the data source.
[**mark_post_process_complete_find_by_id**](MarkPostProcessCompleteApi.md#mark_post_process_complete_find_by_id) | **GET** /MarkPostProcessComplete/{id} | Find a model instance by {{id}} from the data source.


# **mark_post_process_complete_create**
> MarkPostProcessComplete mark_post_process_complete_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.MarkPostProcessCompleteApi()
data = fund_clearing_python_sdk.MarkPostProcessComplete() # MarkPostProcessComplete | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.mark_post_process_complete_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkPostProcessCompleteApi->mark_post_process_complete_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MarkPostProcessComplete**](MarkPostProcessComplete.md)| Model instance data | [optional] 

### Return type

[**MarkPostProcessComplete**](MarkPostProcessComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_post_process_complete_find**
> list[MarkPostProcessComplete] mark_post_process_complete_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.MarkPostProcessCompleteApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.mark_post_process_complete_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkPostProcessCompleteApi->mark_post_process_complete_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[MarkPostProcessComplete]**](MarkPostProcessComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_post_process_complete_find_by_id**
> MarkPostProcessComplete mark_post_process_complete_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.MarkPostProcessCompleteApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.mark_post_process_complete_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarkPostProcessCompleteApi->mark_post_process_complete_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**MarkPostProcessComplete**](MarkPostProcessComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

