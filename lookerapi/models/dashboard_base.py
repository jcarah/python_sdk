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


class DashboardBase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, content_favorite_id=None, content_metadata_id=None, description=None, hidden=None, id=None, model=None, query_timezone=None, readonly=None, refresh_interval=None, refresh_interval_to_i=None, space=None, title=None, user_id=None, can=None):
        """
        DashboardBase - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content_favorite_id': 'int',
            'content_metadata_id': 'int',
            'description': 'str',
            'hidden': 'bool',
            'id': 'str',
            'model': 'LookModel',
            'query_timezone': 'str',
            'readonly': 'bool',
            'refresh_interval': 'str',
            'refresh_interval_to_i': 'int',
            'space': 'SpaceBase',
            'title': 'str',
            'user_id': 'int',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'content_favorite_id': 'content_favorite_id',
            'content_metadata_id': 'content_metadata_id',
            'description': 'description',
            'hidden': 'hidden',
            'id': 'id',
            'model': 'model',
            'query_timezone': 'query_timezone',
            'readonly': 'readonly',
            'refresh_interval': 'refresh_interval',
            'refresh_interval_to_i': 'refresh_interval_to_i',
            'space': 'space',
            'title': 'title',
            'user_id': 'user_id',
            'can': 'can'
        }

        self._content_favorite_id = content_favorite_id
        self._content_metadata_id = content_metadata_id
        self._description = description
        self._hidden = hidden
        self._id = id
        self._model = model
        self._query_timezone = query_timezone
        self._readonly = readonly
        self._refresh_interval = refresh_interval
        self._refresh_interval_to_i = refresh_interval_to_i
        self._space = space
        self._title = title
        self._user_id = user_id
        self._can = can

    @property
    def content_favorite_id(self):
        """
        Gets the content_favorite_id of this DashboardBase.
        Content Favorite Id

        :return: The content_favorite_id of this DashboardBase.
        :rtype: int
        """
        return self._content_favorite_id

    @content_favorite_id.setter
    def content_favorite_id(self, content_favorite_id):
        """
        Sets the content_favorite_id of this DashboardBase.
        Content Favorite Id

        :param content_favorite_id: The content_favorite_id of this DashboardBase.
        :type: int
        """

        self._content_favorite_id = content_favorite_id

    @property
    def content_metadata_id(self):
        """
        Gets the content_metadata_id of this DashboardBase.
        Id of content metadata

        :return: The content_metadata_id of this DashboardBase.
        :rtype: int
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """
        Sets the content_metadata_id of this DashboardBase.
        Id of content metadata

        :param content_metadata_id: The content_metadata_id of this DashboardBase.
        :type: int
        """

        self._content_metadata_id = content_metadata_id

    @property
    def description(self):
        """
        Gets the description of this DashboardBase.
        Description

        :return: The description of this DashboardBase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DashboardBase.
        Description

        :param description: The description of this DashboardBase.
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """
        Gets the hidden of this DashboardBase.
        Is Hidden

        :return: The hidden of this DashboardBase.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """
        Sets the hidden of this DashboardBase.
        Is Hidden

        :param hidden: The hidden of this DashboardBase.
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """
        Gets the id of this DashboardBase.
        Unique Id

        :return: The id of this DashboardBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DashboardBase.
        Unique Id

        :param id: The id of this DashboardBase.
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """
        Gets the model of this DashboardBase.
        Model

        :return: The model of this DashboardBase.
        :rtype: LookModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this DashboardBase.
        Model

        :param model: The model of this DashboardBase.
        :type: LookModel
        """

        self._model = model

    @property
    def query_timezone(self):
        """
        Gets the query_timezone of this DashboardBase.
        Timezone in which the Dashboard will run by default.

        :return: The query_timezone of this DashboardBase.
        :rtype: str
        """
        return self._query_timezone

    @query_timezone.setter
    def query_timezone(self, query_timezone):
        """
        Sets the query_timezone of this DashboardBase.
        Timezone in which the Dashboard will run by default.

        :param query_timezone: The query_timezone of this DashboardBase.
        :type: str
        """

        self._query_timezone = query_timezone

    @property
    def readonly(self):
        """
        Gets the readonly of this DashboardBase.
        Is Read-only

        :return: The readonly of this DashboardBase.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """
        Sets the readonly of this DashboardBase.
        Is Read-only

        :param readonly: The readonly of this DashboardBase.
        :type: bool
        """

        self._readonly = readonly

    @property
    def refresh_interval(self):
        """
        Gets the refresh_interval of this DashboardBase.
        Refresh Interval

        :return: The refresh_interval of this DashboardBase.
        :rtype: str
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """
        Sets the refresh_interval of this DashboardBase.
        Refresh Interval

        :param refresh_interval: The refresh_interval of this DashboardBase.
        :type: str
        """

        self._refresh_interval = refresh_interval

    @property
    def refresh_interval_to_i(self):
        """
        Gets the refresh_interval_to_i of this DashboardBase.
        Refresh Interval as Integer

        :return: The refresh_interval_to_i of this DashboardBase.
        :rtype: int
        """
        return self._refresh_interval_to_i

    @refresh_interval_to_i.setter
    def refresh_interval_to_i(self, refresh_interval_to_i):
        """
        Sets the refresh_interval_to_i of this DashboardBase.
        Refresh Interval as Integer

        :param refresh_interval_to_i: The refresh_interval_to_i of this DashboardBase.
        :type: int
        """

        self._refresh_interval_to_i = refresh_interval_to_i

    @property
    def space(self):
        """
        Gets the space of this DashboardBase.
        Space

        :return: The space of this DashboardBase.
        :rtype: SpaceBase
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this DashboardBase.
        Space

        :param space: The space of this DashboardBase.
        :type: SpaceBase
        """

        self._space = space

    @property
    def title(self):
        """
        Gets the title of this DashboardBase.
        Dashboard Title

        :return: The title of this DashboardBase.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this DashboardBase.
        Dashboard Title

        :param title: The title of this DashboardBase.
        :type: str
        """

        self._title = title

    @property
    def user_id(self):
        """
        Gets the user_id of this DashboardBase.
        Id of User

        :return: The user_id of this DashboardBase.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this DashboardBase.
        Id of User

        :param user_id: The user_id of this DashboardBase.
        :type: int
        """

        self._user_id = user_id

    @property
    def can(self):
        """
        Gets the can of this DashboardBase.
        Operations the current user is able to perform on this object

        :return: The can of this DashboardBase.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this DashboardBase.
        Operations the current user is able to perform on this object

        :param can: The can of this DashboardBase.
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
        if not isinstance(other, DashboardBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
