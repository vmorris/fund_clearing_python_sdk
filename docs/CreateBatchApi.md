# fund_clearing_python_sdk.CreateBatchApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_create**](CreateBatchApi.md#create_batch_create) | **POST** /CreateBatch | Create a new instance of the model and persist it into the data source.
[**create_batch_find**](CreateBatchApi.md#create_batch_find) | **GET** /CreateBatch | Find all instances of the model matched by filter from the data source.
[**create_batch_find_by_id**](CreateBatchApi.md#create_batch_find_by_id) | **GET** /CreateBatch/{id} | Find a model instance by {{id}} from the data source.


# **create_batch_create**
> CreateBatch create_batch_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.CreateBatchApi()
data = fund_clearing_python_sdk.CreateBatch() # CreateBatch | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.create_batch_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateBatchApi->create_batch_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CreateBatch**](CreateBatch.md)| Model instance data | [optional] 

### Return type

[**CreateBatch**](CreateBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_find**
> list[CreateBatch] create_batch_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.CreateBatchApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.create_batch_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateBatchApi->create_batch_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[CreateBatch]**](CreateBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_find_by_id**
> CreateBatch create_batch_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.CreateBatchApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.create_batch_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateBatchApi->create_batch_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**CreateBatch**](CreateBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

