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


class ProjectFile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, path=None, title=None, type=None, extension=None, mime_type=None, editable=None, git_status=None, can=None):
        """
        ProjectFile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'path': 'str',
            'title': 'str',
            'type': 'str',
            'extension': 'str',
            'mime_type': 'str',
            'editable': 'bool',
            'git_status': 'GitStatus',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'path': 'path',
            'title': 'title',
            'type': 'type',
            'extension': 'extension',
            'mime_type': 'mime_type',
            'editable': 'editable',
            'git_status': 'git_status',
            'can': 'can'
        }

        self._id = id
        self._path = path
        self._title = title
        self._type = type
        self._extension = extension
        self._mime_type = mime_type
        self._editable = editable
        self._git_status = git_status
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this ProjectFile.
        An opaque token uniquely identifying a file within a project. Avoid parsing or decomposing the text of this token. This token is stable within a Looker release but may change between Looker releases

        :return: The id of this ProjectFile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectFile.
        An opaque token uniquely identifying a file within a project. Avoid parsing or decomposing the text of this token. This token is stable within a Looker release but may change between Looker releases

        :param id: The id of this ProjectFile.
        :type: str
        """

        self._id = id

    @property
    def path(self):
        """
        Gets the path of this ProjectFile.
        Path, file name, and extension of the file relative to the project root directory

        :return: The path of this ProjectFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ProjectFile.
        Path, file name, and extension of the file relative to the project root directory

        :param path: The path of this ProjectFile.
        :type: str
        """

        self._path = path

    @property
    def title(self):
        """
        Gets the title of this ProjectFile.
        Display name

        :return: The title of this ProjectFile.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProjectFile.
        Display name

        :param title: The title of this ProjectFile.
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this ProjectFile.
        File type: model, view, etc

        :return: The type of this ProjectFile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProjectFile.
        File type: model, view, etc

        :param type: The type of this ProjectFile.
        :type: str
        """

        self._type = type

    @property
    def extension(self):
        """
        Gets the extension of this ProjectFile.
        The extension of the file: .view.lkml, .model.lkml, etc

        :return: The extension of this ProjectFile.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this ProjectFile.
        The extension of the file: .view.lkml, .model.lkml, etc

        :param extension: The extension of this ProjectFile.
        :type: str
        """

        self._extension = extension

    @property
    def mime_type(self):
        """
        Gets the mime_type of this ProjectFile.
        File mime type

        :return: The mime_type of this ProjectFile.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this ProjectFile.
        File mime type

        :param mime_type: The mime_type of this ProjectFile.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def editable(self):
        """
        Gets the editable of this ProjectFile.
        State of editability for the file.

        :return: The editable of this ProjectFile.
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """
        Sets the editable of this ProjectFile.
        State of editability for the file.

        :param editable: The editable of this ProjectFile.
        :type: bool
        """

        self._editable = editable

    @property
    def git_status(self):
        """
        Gets the git_status of this ProjectFile.
        Status of the file according to git

        :return: The git_status of this ProjectFile.
        :rtype: GitStatus
        """
        return self._git_status

    @git_status.setter
    def git_status(self, git_status):
        """
        Sets the git_status of this ProjectFile.
        Status of the file according to git

        :param git_status: The git_status of this ProjectFile.
        :type: GitStatus
        """

        self._git_status = git_status

    @property
    def can(self):
        """
        Gets the can of this ProjectFile.
        Operations the current user is able to perform on this object

        :return: The can of this ProjectFile.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this ProjectFile.
        Operations the current user is able to perform on this object

        :param can: The can of this ProjectFile.
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
        if not isinstance(other, ProjectFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
