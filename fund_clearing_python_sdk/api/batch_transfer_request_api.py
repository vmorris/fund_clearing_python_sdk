# coding: utf-8

"""
    LoopBack Application

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fund_clearing_python_sdk.api_client import ApiClient


class BatchTransferRequestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_transfer_request_create(self, **kwargs):  # noqa: E501
        """Create a new instance of the model and persist it into the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_create(async=True)
        >>> result = thread.get()

        :param async bool
        :param BatchTransferRequest data: Model instance data
        :return: BatchTransferRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.batch_transfer_request_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.batch_transfer_request_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def batch_transfer_request_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new instance of the model and persist it into the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_create_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param BatchTransferRequest data: Model instance data
        :return: BatchTransferRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_transfer_request_create" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/BatchTransferRequest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchTransferRequest',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def batch_transfer_request_delete_by_id(self, id, **kwargs):  # noqa: E501
        """Delete a model instance by {{id}} from the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_delete_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.batch_transfer_request_delete_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_transfer_request_delete_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def batch_transfer_request_delete_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a model instance by {{id}} from the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_delete_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_transfer_request_delete_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `batch_transfer_request_delete_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/BatchTransferRequest/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def batch_transfer_request_exists(self, id, **kwargs):  # noqa: E501
        """Check whether a model instance exists in the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_exists(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.batch_transfer_request_exists_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_transfer_request_exists_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def batch_transfer_request_exists_with_http_info(self, id, **kwargs):  # noqa: E501
        """Check whether a model instance exists in the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_exists_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_transfer_request_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `batch_transfer_request_exists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/BatchTransferRequest/{id}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def batch_transfer_request_find(self, **kwargs):  # noqa: E501
        """Find all instances of the model matched by filter from the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_find(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: list[BatchTransferRequest]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.batch_transfer_request_find_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.batch_transfer_request_find_with_http_info(**kwargs)  # noqa: E501
            return data

    def batch_transfer_request_find_with_http_info(self, **kwargs):  # noqa: E501
        """Find all instances of the model matched by filter from the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_find_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Filter defining fields, where, include, order, offset, and limit - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: list[BatchTransferRequest]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_transfer_request_find" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/BatchTransferRequest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BatchTransferRequest]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def batch_transfer_request_find_by_id(self, id, **kwargs):  # noqa: E501
        """Find a model instance by {{id}} from the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_find_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :param str filter: Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: BatchTransferRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.batch_transfer_request_find_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_transfer_request_find_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def batch_transfer_request_find_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Find a model instance by {{id}} from the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_find_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :param str filter: Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"})
        :return: BatchTransferRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'filter']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_transfer_request_find_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `batch_transfer_request_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/BatchTransferRequest/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchTransferRequest',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def batch_transfer_request_replace_by_id(self, id, **kwargs):  # noqa: E501
        """Replace attributes for a model instance and persist it into the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_replace_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :param BatchTransferRequest data: Model instance data
        :return: BatchTransferRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.batch_transfer_request_replace_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_transfer_request_replace_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def batch_transfer_request_replace_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Replace attributes for a model instance and persist it into the data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.batch_transfer_request_replace_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Model id (required)
        :param BatchTransferRequest data: Model instance data
        :return: BatchTransferRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_transfer_request_replace_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `batch_transfer_request_replace_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/BatchTransferRequest/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchTransferRequest',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
