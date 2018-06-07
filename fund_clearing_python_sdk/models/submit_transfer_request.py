# coding: utf-8

"""
    LoopBack Application

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from fund_clearing_python_sdk.models.transfer import Transfer  # noqa: F401,E501


class SubmitTransferRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_class': 'str',
        'transfer_id': 'str',
        'to_bank': 'str',
        'state': 'str',
        'details': 'Transfer',
        'transaction_id': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        '_class': '$class',
        'transfer_id': 'transferId',
        'to_bank': 'toBank',
        'state': 'state',
        'details': 'details',
        'transaction_id': 'transactionId',
        'timestamp': 'timestamp'
    }

    def __init__(self, _class='org.clearing.SubmitTransferRequest', transfer_id=None, to_bank=None, state=None, details=None, transaction_id=None, timestamp=None):  # noqa: E501
        """SubmitTransferRequest - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self._transfer_id = None
        self._to_bank = None
        self._state = None
        self._details = None
        self._transaction_id = None
        self._timestamp = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        self.transfer_id = transfer_id
        self.to_bank = to_bank
        self.state = state
        self.details = details
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def _class(self):
        """Gets the _class of this SubmitTransferRequest.  # noqa: E501

        The class identifier for this type  # noqa: E501

        :return: The _class of this SubmitTransferRequest.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this SubmitTransferRequest.

        The class identifier for this type  # noqa: E501

        :param _class: The _class of this SubmitTransferRequest.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def transfer_id(self):
        """Gets the transfer_id of this SubmitTransferRequest.  # noqa: E501


        :return: The transfer_id of this SubmitTransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._transfer_id

    @transfer_id.setter
    def transfer_id(self, transfer_id):
        """Sets the transfer_id of this SubmitTransferRequest.


        :param transfer_id: The transfer_id of this SubmitTransferRequest.  # noqa: E501
        :type: str
        """
        if transfer_id is None:
            raise ValueError("Invalid value for `transfer_id`, must not be `None`")  # noqa: E501

        self._transfer_id = transfer_id

    @property
    def to_bank(self):
        """Gets the to_bank of this SubmitTransferRequest.  # noqa: E501


        :return: The to_bank of this SubmitTransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_bank

    @to_bank.setter
    def to_bank(self, to_bank):
        """Sets the to_bank of this SubmitTransferRequest.


        :param to_bank: The to_bank of this SubmitTransferRequest.  # noqa: E501
        :type: str
        """
        if to_bank is None:
            raise ValueError("Invalid value for `to_bank`, must not be `None`")  # noqa: E501

        self._to_bank = to_bank

    @property
    def state(self):
        """Gets the state of this SubmitTransferRequest.  # noqa: E501


        :return: The state of this SubmitTransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubmitTransferRequest.


        :param state: The state of this SubmitTransferRequest.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING", "PROCESSING", "PRE_PROCESS_COMPLETE", "COMPLETE", "ERROR"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def details(self):
        """Gets the details of this SubmitTransferRequest.  # noqa: E501


        :return: The details of this SubmitTransferRequest.  # noqa: E501
        :rtype: Transfer
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SubmitTransferRequest.


        :param details: The details of this SubmitTransferRequest.  # noqa: E501
        :type: Transfer
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def transaction_id(self):
        """Gets the transaction_id of this SubmitTransferRequest.  # noqa: E501

        The instance identifier for this type  # noqa: E501

        :return: The transaction_id of this SubmitTransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this SubmitTransferRequest.

        The instance identifier for this type  # noqa: E501

        :param transaction_id: The transaction_id of this SubmitTransferRequest.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def timestamp(self):
        """Gets the timestamp of this SubmitTransferRequest.  # noqa: E501


        :return: The timestamp of this SubmitTransferRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SubmitTransferRequest.


        :param timestamp: The timestamp of this SubmitTransferRequest.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubmitTransferRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other