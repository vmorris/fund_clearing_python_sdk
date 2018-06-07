# fund_clearing_python_sdk.CompleteSettlementApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_settlement_create**](CompleteSettlementApi.md#complete_settlement_create) | **POST** /CompleteSettlement | Create a new instance of the model and persist it into the data source.
[**complete_settlement_find**](CompleteSettlementApi.md#complete_settlement_find) | **GET** /CompleteSettlement | Find all instances of the model matched by filter from the data source.
[**complete_settlement_find_by_id**](CompleteSettlementApi.md#complete_settlement_find_by_id) | **GET** /CompleteSettlement/{id} | Find a model instance by {{id}} from the data source.


# **complete_settlement_create**
> CompleteSettlement complete_settlement_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.CompleteSettlementApi()
data = fund_clearing_python_sdk.CompleteSettlement() # CompleteSettlement | Model instance data (optional)

try:
    # Create a new instance of the model and persist it into the data source.
    api_response = api_instance.complete_settlement_create(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompleteSettlementApi->complete_settlement_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CompleteSettlement**](CompleteSettlement.md)| Model instance data | [optional] 

### Return type

[**CompleteSettlement**](CompleteSettlement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_settlement_find**
> list[CompleteSettlement] complete_settlement_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.CompleteSettlementApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.complete_settlement_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompleteSettlementApi->complete_settlement_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[CompleteSettlement]**](CompleteSettlement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_settlement_find_by_id**
> CompleteSettlement complete_settlement_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.CompleteSettlementApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.complete_settlement_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompleteSettlementApi->complete_settlement_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**CompleteSettlement**](CompleteSettlement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

