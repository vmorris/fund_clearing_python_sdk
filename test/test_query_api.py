# coding: utf-8

"""
    LoopBack Application

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import fund_clearing_python_sdk
from fund_clearing_python_sdk.api.query_api import QueryApi  # noqa: E501
from fund_clearing_python_sdk.rest import ApiException


class TestQueryApi(unittest.TestCase):
    """QueryApi unit test stubs"""

    def setUp(self):
        self.api = fund_clearing_python_sdk.api.query_api.QueryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_batch_transfer_request_by_id(self):
        """Test case for query_batch_transfer_request_by_id

        Select a BatchTransferRequest by the UUID  # noqa: E501
        """
        pass

    def test_query_batch_transfer_request_for_banks_in_state(self):
        """Test case for query_batch_transfer_request_for_banks_in_state

        Select all BatchTransferRequests in a given state for two participating banks  # noqa: E501
        """
        pass

    def test_query_batch_transfer_requests_by_bank_in_state(self):
        """Test case for query_batch_transfer_requests_by_bank_in_state

        Select all BatchTransferRequests in a given state for a participating bank  # noqa: E501
        """
        pass

    def test_query_transfer_requests_by_bank_in_state(self):
        """Test case for query_transfer_requests_by_bank_in_state

        Select all TransferRequests for a participating bank in a given state  # noqa: E501
        """
        pass

    def test_query_transfer_requests_by_banks_in_state(self):
        """Test case for query_transfer_requests_by_banks_in_state

        Select all TransferRequests for a participating bank in a given state  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()