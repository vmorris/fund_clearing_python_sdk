# fund_clearing_python_sdk.SystemApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_bind_identity**](SystemApi.md#system_bind_identity) | **POST** /system/identities/bind | Bind an identity to the specified participant
[**system_get_all_historian_records**](SystemApi.md#system_get_all_historian_records) | **GET** /system/historian | Get all Historian Records from the Historian
[**system_get_all_identities**](SystemApi.md#system_get_all_identities) | **GET** /system/identities | Get all identities from the identity registry
[**system_get_historian_record_by_id**](SystemApi.md#system_get_historian_record_by_id) | **GET** /system/historian/{id} | Get the specified Historian Record from the Historian
[**system_get_identity_by_id**](SystemApi.md#system_get_identity_by_id) | **GET** /system/identities/{id} | Get the specified identity from the identity registry
[**system_issue_identity**](SystemApi.md#system_issue_identity) | **POST** /system/identities/issue | Issue an identity to the specified participant
[**system_ping**](SystemApi.md#system_ping) | **GET** /system/ping | Test the connection to the business network
[**system_revoke_identity**](SystemApi.md#system_revoke_identity) | **POST** /system/identities/{id}/revoke | Revoke the specified identity


# **system_bind_identity**
> system_bind_identity(data)

Bind an identity to the specified participant

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()
data = fund_clearing_python_sdk.BindIdentityRequest() # BindIdentityRequest | 

try:
    # Bind an identity to the specified participant
    api_instance.system_bind_identity(data)
except ApiException as e:
    print("Exception when calling SystemApi->system_bind_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BindIdentityRequest**](BindIdentityRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_all_historian_records**
> list[object] system_get_all_historian_records()

Get all Historian Records from the Historian

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()

try:
    # Get all Historian Records from the Historian
    api_response = api_instance.system_get_all_historian_records()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_all_historian_records: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_all_identities**
> list[object] system_get_all_identities()

Get all identities from the identity registry

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()

try:
    # Get all identities from the identity registry
    api_response = api_instance.system_get_all_identities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_all_identities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_historian_record_by_id**
> object system_get_historian_record_by_id(id)

Get the specified Historian Record from the Historian

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()
id = 'id_example' # str | 

try:
    # Get the specified Historian Record from the Historian
    api_response = api_instance.system_get_historian_record_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_historian_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_identity_by_id**
> object system_get_identity_by_id(id)

Get the specified identity from the identity registry

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()
id = 'id_example' # str | 

try:
    # Get the specified identity from the identity registry
    api_response = api_instance.system_get_identity_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_identity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_issue_identity**
> file system_issue_identity(data)

Issue an identity to the specified participant

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()
data = fund_clearing_python_sdk.IssueIdentityRequest() # IssueIdentityRequest | 

try:
    # Issue an identity to the specified participant
    api_response = api_instance.system_issue_identity(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_issue_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**IssueIdentityRequest**](IssueIdentityRequest.md)|  | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_ping**
> PingResponse system_ping()

Test the connection to the business network

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()

try:
    # Test the connection to the business network
    api_response = api_instance.system_ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_revoke_identity**
> system_revoke_identity(id)

Revoke the specified identity

### Example
```python
from __future__ import print_function
import time
import fund_clearing_python_sdk
from fund_clearing_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fund_clearing_python_sdk.SystemApi()
id = 'id_example' # str | 

try:
    # Revoke the specified identity
    api_instance.system_revoke_identity(id)
except ApiException as e:
    print("Exception when calling SystemApi->system_revoke_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

