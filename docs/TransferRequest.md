# TransferRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The class identifier for this type | [optional] [default to 'org.clearing.TransferRequest']
**request_id** | **str** | The instance identifier for this type | 
**details** | [**Transfer**](Transfer.md) |  | 
**from_bank_state** | **str** |  | [default to 'PRE_PROCESS_COMPLETE']
**to_bank_state** | **str** |  | 
**state** | **str** |  | 
**from_bank** | [**XAny**](XAny.md) | The identifier of an instance of fromBank | 
**to_bank** | [**XAny**](XAny.md) | The identifier of an instance of toBank | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


