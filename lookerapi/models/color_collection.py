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


class ColorCollection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, categorical_palettes=None, sequential_palettes=None, diverging_palettes=None):
        """
        ColorCollection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'label': 'str',
            'categorical_palettes': 'list[DiscretePalette]',
            'sequential_palettes': 'list[ContinuousPalette]',
            'diverging_palettes': 'list[ContinuousPalette]'
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'categorical_palettes': 'categoricalPalettes',
            'sequential_palettes': 'sequentialPalettes',
            'diverging_palettes': 'divergingPalettes'
        }

        self._id = id
        self._label = label
        self._categorical_palettes = categorical_palettes
        self._sequential_palettes = sequential_palettes
        self._diverging_palettes = diverging_palettes

    @property
    def id(self):
        """
        Gets the id of this ColorCollection.
        Unique Id

        :return: The id of this ColorCollection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ColorCollection.
        Unique Id

        :param id: The id of this ColorCollection.
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this ColorCollection.
        Label of color collection

        :return: The label of this ColorCollection.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ColorCollection.
        Label of color collection

        :param label: The label of this ColorCollection.
        :type: str
        """

        self._label = label

    @property
    def categorical_palettes(self):
        """
        Gets the categorical_palettes of this ColorCollection.
        Array of categorical palette definitions

        :return: The categorical_palettes of this ColorCollection.
        :rtype: list[DiscretePalette]
        """
        return self._categorical_palettes

    @categorical_palettes.setter
    def categorical_palettes(self, categorical_palettes):
        """
        Sets the categorical_palettes of this ColorCollection.
        Array of categorical palette definitions

        :param categorical_palettes: The categorical_palettes of this ColorCollection.
        :type: list[DiscretePalette]
        """

        self._categorical_palettes = categorical_palettes

    @property
    def sequential_palettes(self):
        """
        Gets the sequential_palettes of this ColorCollection.
        Array of discrete palette definitions

        :return: The sequential_palettes of this ColorCollection.
        :rtype: list[ContinuousPalette]
        """
        return self._sequential_palettes

    @sequential_palettes.setter
    def sequential_palettes(self, sequential_palettes):
        """
        Sets the sequential_palettes of this ColorCollection.
        Array of discrete palette definitions

        :param sequential_palettes: The sequential_palettes of this ColorCollection.
        :type: list[ContinuousPalette]
        """

        self._sequential_palettes = sequential_palettes

    @property
    def diverging_palettes(self):
        """
        Gets the diverging_palettes of this ColorCollection.
        Array of diverging palette definitions

        :return: The diverging_palettes of this ColorCollection.
        :rtype: list[ContinuousPalette]
        """
        return self._diverging_palettes

    @diverging_palettes.setter
    def diverging_palettes(self, diverging_palettes):
        """
        Sets the diverging_palettes of this ColorCollection.
        Array of diverging palette definitions

        :param diverging_palettes: The diverging_palettes of this ColorCollection.
        :type: list[ContinuousPalette]
        """

        self._diverging_palettes = diverging_palettes

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
        if not isinstance(other, ColorCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
