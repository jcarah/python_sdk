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


class CredentialsGoogle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_at=None, domain=None, email=None, google_user_id=None, is_disabled=None, logged_in_at=None, type=None, url=None, can=None):
        """
        CredentialsGoogle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_at': 'str',
            'domain': 'str',
            'email': 'str',
            'google_user_id': 'str',
            'is_disabled': 'bool',
            'logged_in_at': 'str',
            'type': 'str',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'created_at': 'created_at',
            'domain': 'domain',
            'email': 'email',
            'google_user_id': 'google_user_id',
            'is_disabled': 'is_disabled',
            'logged_in_at': 'logged_in_at',
            'type': 'type',
            'url': 'url',
            'can': 'can'
        }

        self._created_at = created_at
        self._domain = domain
        self._email = email
        self._google_user_id = google_user_id
        self._is_disabled = is_disabled
        self._logged_in_at = logged_in_at
        self._type = type
        self._url = url
        self._can = can

    @property
    def created_at(self):
        """
        Gets the created_at of this CredentialsGoogle.
        Timestamp for the creation of this credential

        :return: The created_at of this CredentialsGoogle.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CredentialsGoogle.
        Timestamp for the creation of this credential

        :param created_at: The created_at of this CredentialsGoogle.
        :type: str
        """

        self._created_at = created_at

    @property
    def domain(self):
        """
        Gets the domain of this CredentialsGoogle.
        Google domain

        :return: The domain of this CredentialsGoogle.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this CredentialsGoogle.
        Google domain

        :param domain: The domain of this CredentialsGoogle.
        :type: str
        """

        self._domain = domain

    @property
    def email(self):
        """
        Gets the email of this CredentialsGoogle.
        EMail address

        :return: The email of this CredentialsGoogle.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CredentialsGoogle.
        EMail address

        :param email: The email of this CredentialsGoogle.
        :type: str
        """

        self._email = email

    @property
    def google_user_id(self):
        """
        Gets the google_user_id of this CredentialsGoogle.
        Google's Unique ID for this user

        :return: The google_user_id of this CredentialsGoogle.
        :rtype: str
        """
        return self._google_user_id

    @google_user_id.setter
    def google_user_id(self, google_user_id):
        """
        Sets the google_user_id of this CredentialsGoogle.
        Google's Unique ID for this user

        :param google_user_id: The google_user_id of this CredentialsGoogle.
        :type: str
        """

        self._google_user_id = google_user_id

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this CredentialsGoogle.
        Has this credential been disabled?

        :return: The is_disabled of this CredentialsGoogle.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this CredentialsGoogle.
        Has this credential been disabled?

        :param is_disabled: The is_disabled of this CredentialsGoogle.
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def logged_in_at(self):
        """
        Gets the logged_in_at of this CredentialsGoogle.
        Timestamp for most recent login using credential

        :return: The logged_in_at of this CredentialsGoogle.
        :rtype: str
        """
        return self._logged_in_at

    @logged_in_at.setter
    def logged_in_at(self, logged_in_at):
        """
        Sets the logged_in_at of this CredentialsGoogle.
        Timestamp for most recent login using credential

        :param logged_in_at: The logged_in_at of this CredentialsGoogle.
        :type: str
        """

        self._logged_in_at = logged_in_at

    @property
    def type(self):
        """
        Gets the type of this CredentialsGoogle.
        Short name for the type of this kind of credential

        :return: The type of this CredentialsGoogle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CredentialsGoogle.
        Short name for the type of this kind of credential

        :param type: The type of this CredentialsGoogle.
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """
        Gets the url of this CredentialsGoogle.
        Link to get this item

        :return: The url of this CredentialsGoogle.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CredentialsGoogle.
        Link to get this item

        :param url: The url of this CredentialsGoogle.
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """
        Gets the can of this CredentialsGoogle.
        Operations the current user is able to perform on this object

        :return: The can of this CredentialsGoogle.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this CredentialsGoogle.
        Operations the current user is able to perform on this object

        :param can: The can of this CredentialsGoogle.
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
        if not isinstance(other, CredentialsGoogle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
