# coding: utf-8

"""
    Looker API 3.1 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  Note! With great power comes great responsibility: The \"Try It Out!\" button makes API calls to your live Looker instance. Be especially careful with destructive API operations such as `delete_user` or similar. There is no \"undo\" for API operations.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning (but we will try to avoid doing that). Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)  This **API 3.1** is in active development. This is where support for new Looker features will appear as non-breaking additions - new functions, new optional parameters on existing functions, or new optional properties in existing types. Additive changes should not impact your existing application code that calls the Looker API. Your existing application code will not be aware of any new Looker API functionality until you choose to upgrade your app to use a newer Looker API client SDK release.  The following are a few examples of noteworthy items that have changed between API 3.0 and API 3.1. For more comprehensive coverage of API changes, please see the release notes for your Looker release.   ### Examples of new things added in API 3.1:  * Dashboard construction APIs * Themes and custom color collections APIs * Create and run SQL_runner queries * Create and run merged results queries * Create and modify dashboard filters * Create and modify password requirements   ### Deprecated in API 3.0  The following functions and properties have been deprecated in API 3.0.  They continue to exist and work in API 3.0 for the next several Looker releases but they have not been carried forward to API 3.1:  * Dashboard Prefetch functions * User access_filter functions * User API 1.0 credentials functions * Space.is_root and Space.is_user_root properties. Use Space.is_shared_root and Space.is_users_root instead.   ### Semantic changes in API 3.1:  * `all_looks` no longer includes soft-deleted looks, matching `all_dashboards` behavior. You can find soft-deleted looks using `search_looks` with the `deleted` param set to True. * `all_spaces` no longer includes duplicate items * `search_users` no longer accepts Y,y,1,0,N,n for Boolean params, only \"true\" and \"false\". * For greater client and network compatibility, `render_task_results` now returns HTTP status ***202 Accepted*** instead of HTTP status ***102 Processing*** * `all_running_queries` and `kill_query` functions have moved into the `Query` function group.   If you have application code which relies on the old behavior of the APIs above, you may continue using the API 3.0 functions in this Looker release. We strongly suggest you update your code to use API 3.1 analogs as soon as possible.  

    OpenAPI spec version: 3.1.0
    Contact: support@looker.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LookmlModelExploreJoins(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, dependent_fields=None, fields=None, foreign_key=None, _from=None, outer_only=None, relationship=None, required_joins=None, sql_foreign_key=None, sql_on=None, sql_table_name=None, type=None, view_label=None):
        """
        LookmlModelExploreJoins - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'dependent_fields': 'list[str]',
            'fields': 'list[str]',
            'foreign_key': 'str',
            '_from': 'str',
            'outer_only': 'bool',
            'relationship': 'str',
            'required_joins': 'list[str]',
            'sql_foreign_key': 'str',
            'sql_on': 'str',
            'sql_table_name': 'str',
            'type': 'str',
            'view_label': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'dependent_fields': 'dependent_fields',
            'fields': 'fields',
            'foreign_key': 'foreign_key',
            '_from': 'from',
            'outer_only': 'outer_only',
            'relationship': 'relationship',
            'required_joins': 'required_joins',
            'sql_foreign_key': 'sql_foreign_key',
            'sql_on': 'sql_on',
            'sql_table_name': 'sql_table_name',
            'type': 'type',
            'view_label': 'view_label'
        }

        self._name = name
        self._dependent_fields = dependent_fields
        self._fields = fields
        self._foreign_key = foreign_key
        self.__from = _from
        self._outer_only = outer_only
        self._relationship = relationship
        self._required_joins = required_joins
        self._sql_foreign_key = sql_foreign_key
        self._sql_on = sql_on
        self._sql_table_name = sql_table_name
        self._type = type
        self._view_label = view_label

    @property
    def name(self):
        """
        Gets the name of this LookmlModelExploreJoins.
        Name of this join (and name of the view to join)

        :return: The name of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LookmlModelExploreJoins.
        Name of this join (and name of the view to join)

        :param name: The name of this LookmlModelExploreJoins.
        :type: str
        """

        self._name = name

    @property
    def dependent_fields(self):
        """
        Gets the dependent_fields of this LookmlModelExploreJoins.
        Fields referenced by the join

        :return: The dependent_fields of this LookmlModelExploreJoins.
        :rtype: list[str]
        """
        return self._dependent_fields

    @dependent_fields.setter
    def dependent_fields(self, dependent_fields):
        """
        Sets the dependent_fields of this LookmlModelExploreJoins.
        Fields referenced by the join

        :param dependent_fields: The dependent_fields of this LookmlModelExploreJoins.
        :type: list[str]
        """

        self._dependent_fields = dependent_fields

    @property
    def fields(self):
        """
        Gets the fields of this LookmlModelExploreJoins.
        Fields of the joined view to pull into this explore

        :return: The fields of this LookmlModelExploreJoins.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this LookmlModelExploreJoins.
        Fields of the joined view to pull into this explore

        :param fields: The fields of this LookmlModelExploreJoins.
        :type: list[str]
        """

        self._fields = fields

    @property
    def foreign_key(self):
        """
        Gets the foreign_key of this LookmlModelExploreJoins.
        Name of the dimension in this explore whose value is in the primary key of the joined view

        :return: The foreign_key of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._foreign_key

    @foreign_key.setter
    def foreign_key(self, foreign_key):
        """
        Sets the foreign_key of this LookmlModelExploreJoins.
        Name of the dimension in this explore whose value is in the primary key of the joined view

        :param foreign_key: The foreign_key of this LookmlModelExploreJoins.
        :type: str
        """

        self._foreign_key = foreign_key

    @property
    def _from(self):
        """
        Gets the _from of this LookmlModelExploreJoins.
        Name of view to join

        :return: The _from of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this LookmlModelExploreJoins.
        Name of view to join

        :param _from: The _from of this LookmlModelExploreJoins.
        :type: str
        """

        self.__from = _from

    @property
    def outer_only(self):
        """
        Gets the outer_only of this LookmlModelExploreJoins.
        Specifies whether all queries must use an outer join

        :return: The outer_only of this LookmlModelExploreJoins.
        :rtype: bool
        """
        return self._outer_only

    @outer_only.setter
    def outer_only(self, outer_only):
        """
        Sets the outer_only of this LookmlModelExploreJoins.
        Specifies whether all queries must use an outer join

        :param outer_only: The outer_only of this LookmlModelExploreJoins.
        :type: bool
        """

        self._outer_only = outer_only

    @property
    def relationship(self):
        """
        Gets the relationship of this LookmlModelExploreJoins.
        many_to_one, one_to_one, one_to_many, many_to_many

        :return: The relationship of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """
        Sets the relationship of this LookmlModelExploreJoins.
        many_to_one, one_to_one, one_to_many, many_to_many

        :param relationship: The relationship of this LookmlModelExploreJoins.
        :type: str
        """

        self._relationship = relationship

    @property
    def required_joins(self):
        """
        Gets the required_joins of this LookmlModelExploreJoins.
        Names of joins that must always be included in SQL queries

        :return: The required_joins of this LookmlModelExploreJoins.
        :rtype: list[str]
        """
        return self._required_joins

    @required_joins.setter
    def required_joins(self, required_joins):
        """
        Sets the required_joins of this LookmlModelExploreJoins.
        Names of joins that must always be included in SQL queries

        :param required_joins: The required_joins of this LookmlModelExploreJoins.
        :type: list[str]
        """

        self._required_joins = required_joins

    @property
    def sql_foreign_key(self):
        """
        Gets the sql_foreign_key of this LookmlModelExploreJoins.
        SQL expression that produces a foreign key

        :return: The sql_foreign_key of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._sql_foreign_key

    @sql_foreign_key.setter
    def sql_foreign_key(self, sql_foreign_key):
        """
        Sets the sql_foreign_key of this LookmlModelExploreJoins.
        SQL expression that produces a foreign key

        :param sql_foreign_key: The sql_foreign_key of this LookmlModelExploreJoins.
        :type: str
        """

        self._sql_foreign_key = sql_foreign_key

    @property
    def sql_on(self):
        """
        Gets the sql_on of this LookmlModelExploreJoins.
        SQL ON expression describing the join condition

        :return: The sql_on of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._sql_on

    @sql_on.setter
    def sql_on(self, sql_on):
        """
        Sets the sql_on of this LookmlModelExploreJoins.
        SQL ON expression describing the join condition

        :param sql_on: The sql_on of this LookmlModelExploreJoins.
        :type: str
        """

        self._sql_on = sql_on

    @property
    def sql_table_name(self):
        """
        Gets the sql_table_name of this LookmlModelExploreJoins.
        SQL table name to join

        :return: The sql_table_name of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._sql_table_name

    @sql_table_name.setter
    def sql_table_name(self, sql_table_name):
        """
        Sets the sql_table_name of this LookmlModelExploreJoins.
        SQL table name to join

        :param sql_table_name: The sql_table_name of this LookmlModelExploreJoins.
        :type: str
        """

        self._sql_table_name = sql_table_name

    @property
    def type(self):
        """
        Gets the type of this LookmlModelExploreJoins.
        The join type: left_outer, full_outer, inner, or cross

        :return: The type of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LookmlModelExploreJoins.
        The join type: left_outer, full_outer, inner, or cross

        :param type: The type of this LookmlModelExploreJoins.
        :type: str
        """

        self._type = type

    @property
    def view_label(self):
        """
        Gets the view_label of this LookmlModelExploreJoins.
        Label to display in UI selectors

        :return: The view_label of this LookmlModelExploreJoins.
        :rtype: str
        """
        return self._view_label

    @view_label.setter
    def view_label(self, view_label):
        """
        Sets the view_label of this LookmlModelExploreJoins.
        Label to display in UI selectors

        :param view_label: The view_label of this LookmlModelExploreJoins.
        :type: str
        """

        self._view_label = view_label

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LookmlModelExploreJoins):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
