# fund_clearing_python_sdk.BankingParticipantApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**banking_participant_create**](BankingParticipantApi.md#banking_participant_create) | **POST** /BankingParticipant | Create a new instance of the model and persist it into the data source.
[**banking_participant_delete_by_id**](BankingParticipantApi.md#banking_participant_delete_by_id) | **DELETE** /BankingParticipant/{id} | Delete a model instance by {{id}} from the data source.
[**banking_participant_exists**](BankingParticipantApi.md#banking_participant_exists) | **HEAD** /BankingParticipant/{id} | Check whether a model instance exists in the data source.
[**banking_participant_find**](BankingParticipantApi.md#banking_participant_find) | **GET** /BankingParticipant | Find all instances of the model matched by filter from the data source.
[**banking_participant_find_by_id**](BankingParticipantApi.md#banking_participant_find_by_id) | **GET** /BankingParticipant/{id} | Find a model instance by {{id}} from the data source.
[**banking_participant_replace_by_id**](BankingParticipantApi.md#banking_participant_replace_by_id) | **PUT** /BankingParticipant/{id} | Replace attributes for a model instance and persist it into the data source.


# **banking_participant_create**
> BankingParticipant banking_participant_create(data=data)

Create a new instance of the model and persist it into the data source.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BankingParticipant**](BankingParticipant.md)| Model instance data | [optional] 

### Return type

[**BankingParticipant**](BankingParticipant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banking_participant_delete_by_id**
> object banking_participant_delete_by_id(id)

Delete a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.BankingParticipantApi()
id = 'id_example' # str | Model id

try:
    # Delete a model instance by {{id}} from the data source.
    api_response = api_instance.banking_participant_delete_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankingParticipantApi->banking_participant_delete_by_id: %s\n" % e)
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

# **banking_participant_exists**
> InlineResponse200 banking_participant_exists(id)

Check whether a model instance exists in the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.BankingParticipantApi()
id = 'id_example' # str | Model id

try:
    # Check whether a model instance exists in the data source.
    api_response = api_instance.banking_participant_exists(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankingParticipantApi->banking_participant_exists: %s\n" % e)
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

# **banking_participant_find**
> list[BankingParticipant] banking_participant_find(filter=filter)

Find all instances of the model matched by filter from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.BankingParticipantApi()
filter = 'filter_example' # str | Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find all instances of the model matched by filter from the data source.
    api_response = api_instance.banking_participant_find(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankingParticipantApi->banking_participant_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**list[BankingParticipant]**](BankingParticipant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banking_participant_find_by_id**
> BankingParticipant banking_participant_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.BankingParticipantApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.banking_participant_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankingParticipantApi->banking_participant_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**BankingParticipant**](BankingParticipant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **banking_participant_replace_by_id**
> BankingParticipant banking_participant_replace_by_id(id, data=data)

Replace attributes for a model instance and persist it into the data source.

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.BankingParticipantApi()
id = 'id_example' # str | Model id
data = fund_clearing_python_sdk.BankingParticipant() # BankingParticipant | Model instance data (optional)

try:
    # Replace attributes for a model instance and persist it into the data source.
    api_response = api_instance.banking_participant_replace_by_id(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankingParticipantApi->banking_participant_replace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **data** | [**BankingParticipant**](BankingParticipant.md)| Model instance data | [optional] 

### Return type

[**BankingParticipant**](BankingParticipant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

