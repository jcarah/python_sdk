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


class Theme(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, begin_at=None, end_at=None, id=None, name=None, settings=None, can=None):
        """
        Theme - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'begin_at': 'datetime',
            'end_at': 'datetime',
            'id': 'int',
            'name': 'str',
            'settings': 'ThemeSettings',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'begin_at': 'begin_at',
            'end_at': 'end_at',
            'id': 'id',
            'name': 'name',
            'settings': 'settings',
            'can': 'can'
        }

        self._begin_at = begin_at
        self._end_at = end_at
        self._id = id
        self._name = name
        self._settings = settings
        self._can = can

    @property
    def begin_at(self):
        """
        Gets the begin_at of this Theme.
        Timestamp for when this theme becomes active. Null=always

        :return: The begin_at of this Theme.
        :rtype: datetime
        """
        return self._begin_at

    @begin_at.setter
    def begin_at(self, begin_at):
        """
        Sets the begin_at of this Theme.
        Timestamp for when this theme becomes active. Null=always

        :param begin_at: The begin_at of this Theme.
        :type: datetime
        """

        self._begin_at = begin_at

    @property
    def end_at(self):
        """
        Gets the end_at of this Theme.
        Timestamp for when this theme expires. Null=never

        :return: The end_at of this Theme.
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """
        Sets the end_at of this Theme.
        Timestamp for when this theme expires. Null=never

        :param end_at: The end_at of this Theme.
        :type: datetime
        """

        self._end_at = end_at

    @property
    def id(self):
        """
        Gets the id of this Theme.
        Unique Id

        :return: The id of this Theme.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Theme.
        Unique Id

        :param id: The id of this Theme.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Theme.
        Name of theme. Can only be alphanumeric and underscores.

        :return: The name of this Theme.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Theme.
        Name of theme. Can only be alphanumeric and underscores.

        :param name: The name of this Theme.
        :type: str
        """

        self._name = name

    @property
    def settings(self):
        """
        Gets the settings of this Theme.
        Hash of name/value pairs for theme settings. These names get validated.

        :return: The settings of this Theme.
        :rtype: ThemeSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this Theme.
        Hash of name/value pairs for theme settings. These names get validated.

        :param settings: The settings of this Theme.
        :type: ThemeSettings
        """

        self._settings = settings

    @property
    def can(self):
        """
        Gets the can of this Theme.
        Operations the current user is able to perform on this object

        :return: The can of this Theme.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Theme.
        Operations the current user is able to perform on this object

        :param can: The can of this Theme.
        :type: dict(str, bool)
        """

        self._can = can

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
        if not isinstance(other, Theme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
