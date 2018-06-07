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


class Transfer(object):
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
        'currency': 'str',
        'amount': 'float',
        'from_account': 'float',
        'to_account': 'float',
        'id': 'str'
    }

    attribute_map = {
        '_class': '$class',
        'currency': 'currency',
        'amount': 'amount',
        'from_account': 'fromAccount',
        'to_account': 'toAccount',
        'id': 'id'
    }

    def __init__(self, _class='org.clearing.Transfer', currency=None, amount=None, from_account=None, to_account=None, id=None):  # noqa: E501
        """Transfer - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self._currency = None
        self._amount = None
        self._from_account = None
        self._to_account = None
        self._id = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        self.currency = currency
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account
        if id is not None:
            self.id = id

    @property
    def _class(self):
        """Gets the _class of this Transfer.  # noqa: E501

        The class identifier for this type  # noqa: E501

        :return: The _class of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Transfer.

        The class identifier for this type  # noqa: E501

        :param _class: The _class of this Transfer.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def currency(self):
        """Gets the currency of this Transfer.  # noqa: E501


        :return: The currency of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Transfer.


        :param currency: The currency of this Transfer.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        allowed_values = ["EURO", "STERLING", "USD", "YEN", "CHF", "CAD"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this Transfer.  # noqa: E501


        :return: The amount of this Transfer.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transfer.


        :param amount: The amount of this Transfer.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def from_account(self):
        """Gets the from_account of this Transfer.  # noqa: E501


        :return: The from_account of this Transfer.  # noqa: E501
        :rtype: float
        """
        return self._from_account

    @from_account.setter
    def from_account(self, from_account):
        """Sets the from_account of this Transfer.


        :param from_account: The from_account of this Transfer.  # noqa: E501
        :type: float
        """
        if from_account is None:
            raise ValueError("Invalid value for `from_account`, must not be `None`")  # noqa: E501

        self._from_account = from_account

    @property
    def to_account(self):
        """Gets the to_account of this Transfer.  # noqa: E501


        :return: The to_account of this Transfer.  # noqa: E501
        :rtype: float
        """
        return self._to_account

    @to_account.setter
    def to_account(self, to_account):
        """Sets the to_account of this Transfer.


        :param to_account: The to_account of this Transfer.  # noqa: E501
        :type: float
        """
        if to_account is None:
            raise ValueError("Invalid value for `to_account`, must not be `None`")  # noqa: E501

        self._to_account = to_account

    @property
    def id(self):
        """Gets the id of this Transfer.  # noqa: E501


        :return: The id of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transfer.


        :param id: The id of this Transfer.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, Transfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
