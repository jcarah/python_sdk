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


class ProjectValidation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, project_digest=None, models_not_validated=None, computation_time=None):
        """
        ProjectValidation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[ProjectError]',
            'project_digest': 'str',
            'models_not_validated': 'list[ModelsNotValidated]',
            'computation_time': 'float'
        }

        self.attribute_map = {
            'errors': 'errors',
            'project_digest': 'project_digest',
            'models_not_validated': 'models_not_validated',
            'computation_time': 'computation_time'
        }

        self._errors = errors
        self._project_digest = project_digest
        self._models_not_validated = models_not_validated
        self._computation_time = computation_time

    @property
    def errors(self):
        """
        Gets the errors of this ProjectValidation.
        A list of project errors

        :return: The errors of this ProjectValidation.
        :rtype: list[ProjectError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ProjectValidation.
        A list of project errors

        :param errors: The errors of this ProjectValidation.
        :type: list[ProjectError]
        """

        self._errors = errors

    @property
    def project_digest(self):
        """
        Gets the project_digest of this ProjectValidation.
        A hash value computed from the project's current state

        :return: The project_digest of this ProjectValidation.
        :rtype: str
        """
        return self._project_digest

    @project_digest.setter
    def project_digest(self, project_digest):
        """
        Sets the project_digest of this ProjectValidation.
        A hash value computed from the project's current state

        :param project_digest: The project_digest of this ProjectValidation.
        :type: str
        """

        self._project_digest = project_digest

    @property
    def models_not_validated(self):
        """
        Gets the models_not_validated of this ProjectValidation.
        A list of models which were not fully validated

        :return: The models_not_validated of this ProjectValidation.
        :rtype: list[ModelsNotValidated]
        """
        return self._models_not_validated

    @models_not_validated.setter
    def models_not_validated(self, models_not_validated):
        """
        Sets the models_not_validated of this ProjectValidation.
        A list of models which were not fully validated

        :param models_not_validated: The models_not_validated of this ProjectValidation.
        :type: list[ModelsNotValidated]
        """

        self._models_not_validated = models_not_validated

    @property
    def computation_time(self):
        """
        Gets the computation_time of this ProjectValidation.
        Duration of project validation in seconds

        :return: The computation_time of this ProjectValidation.
        :rtype: float
        """
        return self._computation_time

    @computation_time.setter
    def computation_time(self, computation_time):
        """
        Sets the computation_time of this ProjectValidation.
        Duration of project validation in seconds

        :param computation_time: The computation_time of this ProjectValidation.
        :type: float
        """

        self._computation_time = computation_time

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
        if not isinstance(other, ProjectValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
