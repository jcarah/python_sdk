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


class LDAPConfigTestResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, details=None, issues=None, message=None, status=None, trace=None, user=None, url=None, can=None):
        """
        LDAPConfigTestResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'details': 'str',
            'issues': 'list[LDAPConfigTestIssue]',
            'message': 'str',
            'status': 'str',
            'trace': 'str',
            'user': 'LDAPUser',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'details': 'details',
            'issues': 'issues',
            'message': 'message',
            'status': 'status',
            'trace': 'trace',
            'user': 'user',
            'url': 'url',
            'can': 'can'
        }

        self._details = details
        self._issues = issues
        self._message = message
        self._status = status
        self._trace = trace
        self._user = user
        self._url = url
        self._can = can

    @property
    def details(self):
        """
        Gets the details of this LDAPConfigTestResult.
        Additional details for error cases

        :return: The details of this LDAPConfigTestResult.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this LDAPConfigTestResult.
        Additional details for error cases

        :param details: The details of this LDAPConfigTestResult.
        :type: str
        """

        self._details = details

    @property
    def issues(self):
        """
        Gets the issues of this LDAPConfigTestResult.
        Array of issues/considerations about the result

        :return: The issues of this LDAPConfigTestResult.
        :rtype: list[LDAPConfigTestIssue]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """
        Sets the issues of this LDAPConfigTestResult.
        Array of issues/considerations about the result

        :param issues: The issues of this LDAPConfigTestResult.
        :type: list[LDAPConfigTestIssue]
        """

        self._issues = issues

    @property
    def message(self):
        """
        Gets the message of this LDAPConfigTestResult.
        Short human readable test about the result

        :return: The message of this LDAPConfigTestResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this LDAPConfigTestResult.
        Short human readable test about the result

        :param message: The message of this LDAPConfigTestResult.
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """
        Gets the status of this LDAPConfigTestResult.
        Test status code: always 'success' or 'error'

        :return: The status of this LDAPConfigTestResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LDAPConfigTestResult.
        Test status code: always 'success' or 'error'

        :param status: The status of this LDAPConfigTestResult.
        :type: str
        """

        self._status = status

    @property
    def trace(self):
        """
        Gets the trace of this LDAPConfigTestResult.
        A more detailed trace of incremental results during auth tests

        :return: The trace of this LDAPConfigTestResult.
        :rtype: str
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """
        Sets the trace of this LDAPConfigTestResult.
        A more detailed trace of incremental results during auth tests

        :param trace: The trace of this LDAPConfigTestResult.
        :type: str
        """

        self._trace = trace

    @property
    def user(self):
        """
        Gets the user of this LDAPConfigTestResult.
        User details from LDAP server for auth tests

        :return: The user of this LDAPConfigTestResult.
        :rtype: LDAPUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this LDAPConfigTestResult.
        User details from LDAP server for auth tests

        :param user: The user of this LDAPConfigTestResult.
        :type: LDAPUser
        """

        self._user = user

    @property
    def url(self):
        """
        Gets the url of this LDAPConfigTestResult.
        Link to ldap config

        :return: The url of this LDAPConfigTestResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this LDAPConfigTestResult.
        Link to ldap config

        :param url: The url of this LDAPConfigTestResult.
        :type: str
        """

        self._url = url

    @property
    def can(self):
        """
        Gets the can of this LDAPConfigTestResult.
        Operations the current user is able to perform on this object

        :return: The can of this LDAPConfigTestResult.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this LDAPConfigTestResult.
        Operations the current user is able to perform on this object

        :param can: The can of this LDAPConfigTestResult.
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
        if not isinstance(other, LDAPConfigTestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
