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


class ContentView(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, look_id=None, dashboard_id=None, content_metadata_id=None, user_id=None, group_id=None, view_count=None, favorite_count=None, last_viewed_at=None, start_of_week_date=None, can=None):
        """
        ContentView - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'look_id': 'int',
            'dashboard_id': 'int',
            'content_metadata_id': 'int',
            'user_id': 'int',
            'group_id': 'int',
            'view_count': 'int',
            'favorite_count': 'int',
            'last_viewed_at': 'str',
            'start_of_week_date': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'look_id': 'look_id',
            'dashboard_id': 'dashboard_id',
            'content_metadata_id': 'content_metadata_id',
            'user_id': 'user_id',
            'group_id': 'group_id',
            'view_count': 'view_count',
            'favorite_count': 'favorite_count',
            'last_viewed_at': 'last_viewed_at',
            'start_of_week_date': 'start_of_week_date',
            'can': 'can'
        }

        self._id = id
        self._look_id = look_id
        self._dashboard_id = dashboard_id
        self._content_metadata_id = content_metadata_id
        self._user_id = user_id
        self._group_id = group_id
        self._view_count = view_count
        self._favorite_count = favorite_count
        self._last_viewed_at = last_viewed_at
        self._start_of_week_date = start_of_week_date
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this ContentView.
        Unique Id

        :return: The id of this ContentView.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContentView.
        Unique Id

        :param id: The id of this ContentView.
        :type: int
        """

        self._id = id

    @property
    def look_id(self):
        """
        Gets the look_id of this ContentView.
        Id of viewed Look

        :return: The look_id of this ContentView.
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """
        Sets the look_id of this ContentView.
        Id of viewed Look

        :param look_id: The look_id of this ContentView.
        :type: int
        """

        self._look_id = look_id

    @property
    def dashboard_id(self):
        """
        Gets the dashboard_id of this ContentView.
        Id of the viewed Dashboard

        :return: The dashboard_id of this ContentView.
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """
        Sets the dashboard_id of this ContentView.
        Id of the viewed Dashboard

        :param dashboard_id: The dashboard_id of this ContentView.
        :type: int
        """

        self._dashboard_id = dashboard_id

    @property
    def content_metadata_id(self):
        """
        Gets the content_metadata_id of this ContentView.
        Content metadata id of the Look or Dashboard

        :return: The content_metadata_id of this ContentView.
        :rtype: int
        """
        return self._content_metadata_id

    @content_metadata_id.setter
    def content_metadata_id(self, content_metadata_id):
        """
        Sets the content_metadata_id of this ContentView.
        Content metadata id of the Look or Dashboard

        :param content_metadata_id: The content_metadata_id of this ContentView.
        :type: int
        """

        self._content_metadata_id = content_metadata_id

    @property
    def user_id(self):
        """
        Gets the user_id of this ContentView.
        Id of user content was viewed by

        :return: The user_id of this ContentView.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ContentView.
        Id of user content was viewed by

        :param user_id: The user_id of this ContentView.
        :type: int
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this ContentView.
        Id of group content was viewed by

        :return: The group_id of this ContentView.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this ContentView.
        Id of group content was viewed by

        :param group_id: The group_id of this ContentView.
        :type: int
        """

        self._group_id = group_id

    @property
    def view_count(self):
        """
        Gets the view_count of this ContentView.
        Number of times piece of content was viewed

        :return: The view_count of this ContentView.
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """
        Sets the view_count of this ContentView.
        Number of times piece of content was viewed

        :param view_count: The view_count of this ContentView.
        :type: int
        """

        self._view_count = view_count

    @property
    def favorite_count(self):
        """
        Gets the favorite_count of this ContentView.
        Number of times piece of content was favorited

        :return: The favorite_count of this ContentView.
        :rtype: int
        """
        return self._favorite_count

    @favorite_count.setter
    def favorite_count(self, favorite_count):
        """
        Sets the favorite_count of this ContentView.
        Number of times piece of content was favorited

        :param favorite_count: The favorite_count of this ContentView.
        :type: int
        """

        self._favorite_count = favorite_count

    @property
    def last_viewed_at(self):
        """
        Gets the last_viewed_at of this ContentView.
        Date the piece of content was last viewed

        :return: The last_viewed_at of this ContentView.
        :rtype: str
        """
        return self._last_viewed_at

    @last_viewed_at.setter
    def last_viewed_at(self, last_viewed_at):
        """
        Sets the last_viewed_at of this ContentView.
        Date the piece of content was last viewed

        :param last_viewed_at: The last_viewed_at of this ContentView.
        :type: str
        """

        self._last_viewed_at = last_viewed_at

    @property
    def start_of_week_date(self):
        """
        Gets the start_of_week_date of this ContentView.
        Week start date for the view and favorite count during that given week

        :return: The start_of_week_date of this ContentView.
        :rtype: str
        """
        return self._start_of_week_date

    @start_of_week_date.setter
    def start_of_week_date(self, start_of_week_date):
        """
        Sets the start_of_week_date of this ContentView.
        Week start date for the view and favorite count during that given week

        :param start_of_week_date: The start_of_week_date of this ContentView.
        :type: str
        """

        self._start_of_week_date = start_of_week_date

    @property
    def can(self):
        """
        Gets the can of this ContentView.
        Operations the current user is able to perform on this object

        :return: The can of this ContentView.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this ContentView.
        Operations the current user is able to perform on this object

        :param can: The can of this ContentView.
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
        if not isinstance(other, ContentView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
