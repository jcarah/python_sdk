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


class LookmlModelExplore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, label=None, scopes=None, can_total=None, can_save=None, can_explain=None, can_pivot_in_db=None, can_subtotal=None, has_timezone_support=None, supports_cost_estimate=None, connection_name=None, null_sort_treatment=None, files=None, source_file=None, project_name=None, model_name=None, view_name=None, hidden=None, sql_table_name=None, access_filter_fields=None, access_filters=None, aliases=None, always_filter=None, conditionally_filter=None, index_fields=None, sets=None, errors=None, fields=None, joins=None, group_label=None, supported_measure_types=None):
        """
        LookmlModelExplore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'label': 'str',
            'scopes': 'list[str]',
            'can_total': 'bool',
            'can_save': 'bool',
            'can_explain': 'bool',
            'can_pivot_in_db': 'bool',
            'can_subtotal': 'bool',
            'has_timezone_support': 'bool',
            'supports_cost_estimate': 'bool',
            'connection_name': 'str',
            'null_sort_treatment': 'str',
            'files': 'list[str]',
            'source_file': 'str',
            'project_name': 'str',
            'model_name': 'str',
            'view_name': 'str',
            'hidden': 'bool',
            'sql_table_name': 'str',
            'access_filter_fields': 'list[str]',
            'access_filters': 'list[LookmlModelExploreAccessFilter]',
            'aliases': 'list[LookmlModelExploreAlias]',
            'always_filter': 'list[LookmlModelExploreAlwaysFilter]',
            'conditionally_filter': 'list[LookmlModelExploreConditionallyFilter]',
            'index_fields': 'list[str]',
            'sets': 'list[LookmlModelExploreSet]',
            'errors': 'list[LookmlModelExploreError]',
            'fields': 'LookmlModelExploreFieldset',
            'joins': 'list[LookmlModelExploreJoins]',
            'group_label': 'str',
            'supported_measure_types': 'list[LookmlModelExploreSupportedMeasureType]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'label': 'label',
            'scopes': 'scopes',
            'can_total': 'can_total',
            'can_save': 'can_save',
            'can_explain': 'can_explain',
            'can_pivot_in_db': 'can_pivot_in_db',
            'can_subtotal': 'can_subtotal',
            'has_timezone_support': 'has_timezone_support',
            'supports_cost_estimate': 'supports_cost_estimate',
            'connection_name': 'connection_name',
            'null_sort_treatment': 'null_sort_treatment',
            'files': 'files',
            'source_file': 'source_file',
            'project_name': 'project_name',
            'model_name': 'model_name',
            'view_name': 'view_name',
            'hidden': 'hidden',
            'sql_table_name': 'sql_table_name',
            'access_filter_fields': 'access_filter_fields',
            'access_filters': 'access_filters',
            'aliases': 'aliases',
            'always_filter': 'always_filter',
            'conditionally_filter': 'conditionally_filter',
            'index_fields': 'index_fields',
            'sets': 'sets',
            'errors': 'errors',
            'fields': 'fields',
            'joins': 'joins',
            'group_label': 'group_label',
            'supported_measure_types': 'supported_measure_types'
        }

        self._id = id
        self._name = name
        self._description = description
        self._label = label
        self._scopes = scopes
        self._can_total = can_total
        self._can_save = can_save
        self._can_explain = can_explain
        self._can_pivot_in_db = can_pivot_in_db
        self._can_subtotal = can_subtotal
        self._has_timezone_support = has_timezone_support
        self._supports_cost_estimate = supports_cost_estimate
        self._connection_name = connection_name
        self._null_sort_treatment = null_sort_treatment
        self._files = files
        self._source_file = source_file
        self._project_name = project_name
        self._model_name = model_name
        self._view_name = view_name
        self._hidden = hidden
        self._sql_table_name = sql_table_name
        self._access_filter_fields = access_filter_fields
        self._access_filters = access_filters
        self._aliases = aliases
        self._always_filter = always_filter
        self._conditionally_filter = conditionally_filter
        self._index_fields = index_fields
        self._sets = sets
        self._errors = errors
        self._fields = fields
        self._joins = joins
        self._group_label = group_label
        self._supported_measure_types = supported_measure_types

    @property
    def id(self):
        """
        Gets the id of this LookmlModelExplore.
        Fully qualified name model plus explore name

        :return: The id of this LookmlModelExplore.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LookmlModelExplore.
        Fully qualified name model plus explore name

        :param id: The id of this LookmlModelExplore.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this LookmlModelExplore.
        Explore name

        :return: The name of this LookmlModelExplore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LookmlModelExplore.
        Explore name

        :param name: The name of this LookmlModelExplore.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LookmlModelExplore.
        Description

        :return: The description of this LookmlModelExplore.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LookmlModelExplore.
        Description

        :param description: The description of this LookmlModelExplore.
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """
        Gets the label of this LookmlModelExplore.
        Label

        :return: The label of this LookmlModelExplore.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this LookmlModelExplore.
        Label

        :param label: The label of this LookmlModelExplore.
        :type: str
        """

        self._label = label

    @property
    def scopes(self):
        """
        Gets the scopes of this LookmlModelExplore.
        Scopes

        :return: The scopes of this LookmlModelExplore.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this LookmlModelExplore.
        Scopes

        :param scopes: The scopes of this LookmlModelExplore.
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def can_total(self):
        """
        Gets the can_total of this LookmlModelExplore.
        Can Total

        :return: The can_total of this LookmlModelExplore.
        :rtype: bool
        """
        return self._can_total

    @can_total.setter
    def can_total(self, can_total):
        """
        Sets the can_total of this LookmlModelExplore.
        Can Total

        :param can_total: The can_total of this LookmlModelExplore.
        :type: bool
        """

        self._can_total = can_total

    @property
    def can_save(self):
        """
        Gets the can_save of this LookmlModelExplore.
        Can Save

        :return: The can_save of this LookmlModelExplore.
        :rtype: bool
        """
        return self._can_save

    @can_save.setter
    def can_save(self, can_save):
        """
        Sets the can_save of this LookmlModelExplore.
        Can Save

        :param can_save: The can_save of this LookmlModelExplore.
        :type: bool
        """

        self._can_save = can_save

    @property
    def can_explain(self):
        """
        Gets the can_explain of this LookmlModelExplore.
        Can Explain

        :return: The can_explain of this LookmlModelExplore.
        :rtype: bool
        """
        return self._can_explain

    @can_explain.setter
    def can_explain(self, can_explain):
        """
        Sets the can_explain of this LookmlModelExplore.
        Can Explain

        :param can_explain: The can_explain of this LookmlModelExplore.
        :type: bool
        """

        self._can_explain = can_explain

    @property
    def can_pivot_in_db(self):
        """
        Gets the can_pivot_in_db of this LookmlModelExplore.
        Can pivot in the DB

        :return: The can_pivot_in_db of this LookmlModelExplore.
        :rtype: bool
        """
        return self._can_pivot_in_db

    @can_pivot_in_db.setter
    def can_pivot_in_db(self, can_pivot_in_db):
        """
        Sets the can_pivot_in_db of this LookmlModelExplore.
        Can pivot in the DB

        :param can_pivot_in_db: The can_pivot_in_db of this LookmlModelExplore.
        :type: bool
        """

        self._can_pivot_in_db = can_pivot_in_db

    @property
    def can_subtotal(self):
        """
        Gets the can_subtotal of this LookmlModelExplore.
        Can use subtotals

        :return: The can_subtotal of this LookmlModelExplore.
        :rtype: bool
        """
        return self._can_subtotal

    @can_subtotal.setter
    def can_subtotal(self, can_subtotal):
        """
        Sets the can_subtotal of this LookmlModelExplore.
        Can use subtotals

        :param can_subtotal: The can_subtotal of this LookmlModelExplore.
        :type: bool
        """

        self._can_subtotal = can_subtotal

    @property
    def has_timezone_support(self):
        """
        Gets the has_timezone_support of this LookmlModelExplore.
        Has timezone support

        :return: The has_timezone_support of this LookmlModelExplore.
        :rtype: bool
        """
        return self._has_timezone_support

    @has_timezone_support.setter
    def has_timezone_support(self, has_timezone_support):
        """
        Sets the has_timezone_support of this LookmlModelExplore.
        Has timezone support

        :param has_timezone_support: The has_timezone_support of this LookmlModelExplore.
        :type: bool
        """

        self._has_timezone_support = has_timezone_support

    @property
    def supports_cost_estimate(self):
        """
        Gets the supports_cost_estimate of this LookmlModelExplore.
        Cost estimates supported

        :return: The supports_cost_estimate of this LookmlModelExplore.
        :rtype: bool
        """
        return self._supports_cost_estimate

    @supports_cost_estimate.setter
    def supports_cost_estimate(self, supports_cost_estimate):
        """
        Sets the supports_cost_estimate of this LookmlModelExplore.
        Cost estimates supported

        :param supports_cost_estimate: The supports_cost_estimate of this LookmlModelExplore.
        :type: bool
        """

        self._supports_cost_estimate = supports_cost_estimate

    @property
    def connection_name(self):
        """
        Gets the connection_name of this LookmlModelExplore.
        Connection name

        :return: The connection_name of this LookmlModelExplore.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """
        Sets the connection_name of this LookmlModelExplore.
        Connection name

        :param connection_name: The connection_name of this LookmlModelExplore.
        :type: str
        """

        self._connection_name = connection_name

    @property
    def null_sort_treatment(self):
        """
        Gets the null_sort_treatment of this LookmlModelExplore.
        How nulls are sorted, possible values are \"low\", \"high\", \"first\" and \"last\"

        :return: The null_sort_treatment of this LookmlModelExplore.
        :rtype: str
        """
        return self._null_sort_treatment

    @null_sort_treatment.setter
    def null_sort_treatment(self, null_sort_treatment):
        """
        Sets the null_sort_treatment of this LookmlModelExplore.
        How nulls are sorted, possible values are \"low\", \"high\", \"first\" and \"last\"

        :param null_sort_treatment: The null_sort_treatment of this LookmlModelExplore.
        :type: str
        """

        self._null_sort_treatment = null_sort_treatment

    @property
    def files(self):
        """
        Gets the files of this LookmlModelExplore.
        List of model source files

        :return: The files of this LookmlModelExplore.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this LookmlModelExplore.
        List of model source files

        :param files: The files of this LookmlModelExplore.
        :type: list[str]
        """

        self._files = files

    @property
    def source_file(self):
        """
        Gets the source_file of this LookmlModelExplore.
        Primary source_file file

        :return: The source_file of this LookmlModelExplore.
        :rtype: str
        """
        return self._source_file

    @source_file.setter
    def source_file(self, source_file):
        """
        Sets the source_file of this LookmlModelExplore.
        Primary source_file file

        :param source_file: The source_file of this LookmlModelExplore.
        :type: str
        """

        self._source_file = source_file

    @property
    def project_name(self):
        """
        Gets the project_name of this LookmlModelExplore.
        Name of project

        :return: The project_name of this LookmlModelExplore.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """
        Sets the project_name of this LookmlModelExplore.
        Name of project

        :param project_name: The project_name of this LookmlModelExplore.
        :type: str
        """

        self._project_name = project_name

    @property
    def model_name(self):
        """
        Gets the model_name of this LookmlModelExplore.
        Name of model

        :return: The model_name of this LookmlModelExplore.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """
        Sets the model_name of this LookmlModelExplore.
        Name of model

        :param model_name: The model_name of this LookmlModelExplore.
        :type: str
        """

        self._model_name = model_name

    @property
    def view_name(self):
        """
        Gets the view_name of this LookmlModelExplore.
        Name of view

        :return: The view_name of this LookmlModelExplore.
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """
        Sets the view_name of this LookmlModelExplore.
        Name of view

        :param view_name: The view_name of this LookmlModelExplore.
        :type: str
        """

        self._view_name = view_name

    @property
    def hidden(self):
        """
        Gets the hidden of this LookmlModelExplore.
        Is hidden

        :return: The hidden of this LookmlModelExplore.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """
        Sets the hidden of this LookmlModelExplore.
        Is hidden

        :param hidden: The hidden of this LookmlModelExplore.
        :type: bool
        """

        self._hidden = hidden

    @property
    def sql_table_name(self):
        """
        Gets the sql_table_name of this LookmlModelExplore.
        A sql_table_name expression that defines what sql table the view/explore maps onto. Example: \"prod_orders2 AS orders\" in a view named orders.

        :return: The sql_table_name of this LookmlModelExplore.
        :rtype: str
        """
        return self._sql_table_name

    @sql_table_name.setter
    def sql_table_name(self, sql_table_name):
        """
        Sets the sql_table_name of this LookmlModelExplore.
        A sql_table_name expression that defines what sql table the view/explore maps onto. Example: \"prod_orders2 AS orders\" in a view named orders.

        :param sql_table_name: The sql_table_name of this LookmlModelExplore.
        :type: str
        """

        self._sql_table_name = sql_table_name

    @property
    def access_filter_fields(self):
        """
        Gets the access_filter_fields of this LookmlModelExplore.
        (DEPRECATED) Array of access filter field names

        :return: The access_filter_fields of this LookmlModelExplore.
        :rtype: list[str]
        """
        return self._access_filter_fields

    @access_filter_fields.setter
    def access_filter_fields(self, access_filter_fields):
        """
        Sets the access_filter_fields of this LookmlModelExplore.
        (DEPRECATED) Array of access filter field names

        :param access_filter_fields: The access_filter_fields of this LookmlModelExplore.
        :type: list[str]
        """

        self._access_filter_fields = access_filter_fields

    @property
    def access_filters(self):
        """
        Gets the access_filters of this LookmlModelExplore.
        Access filters

        :return: The access_filters of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreAccessFilter]
        """
        return self._access_filters

    @access_filters.setter
    def access_filters(self, access_filters):
        """
        Sets the access_filters of this LookmlModelExplore.
        Access filters

        :param access_filters: The access_filters of this LookmlModelExplore.
        :type: list[LookmlModelExploreAccessFilter]
        """

        self._access_filters = access_filters

    @property
    def aliases(self):
        """
        Gets the aliases of this LookmlModelExplore.
        Aliases

        :return: The aliases of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreAlias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this LookmlModelExplore.
        Aliases

        :param aliases: The aliases of this LookmlModelExplore.
        :type: list[LookmlModelExploreAlias]
        """

        self._aliases = aliases

    @property
    def always_filter(self):
        """
        Gets the always_filter of this LookmlModelExplore.
        Always filter

        :return: The always_filter of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreAlwaysFilter]
        """
        return self._always_filter

    @always_filter.setter
    def always_filter(self, always_filter):
        """
        Sets the always_filter of this LookmlModelExplore.
        Always filter

        :param always_filter: The always_filter of this LookmlModelExplore.
        :type: list[LookmlModelExploreAlwaysFilter]
        """

        self._always_filter = always_filter

    @property
    def conditionally_filter(self):
        """
        Gets the conditionally_filter of this LookmlModelExplore.
        Conditionally filter

        :return: The conditionally_filter of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreConditionallyFilter]
        """
        return self._conditionally_filter

    @conditionally_filter.setter
    def conditionally_filter(self, conditionally_filter):
        """
        Sets the conditionally_filter of this LookmlModelExplore.
        Conditionally filter

        :param conditionally_filter: The conditionally_filter of this LookmlModelExplore.
        :type: list[LookmlModelExploreConditionallyFilter]
        """

        self._conditionally_filter = conditionally_filter

    @property
    def index_fields(self):
        """
        Gets the index_fields of this LookmlModelExplore.
        Array of index fields

        :return: The index_fields of this LookmlModelExplore.
        :rtype: list[str]
        """
        return self._index_fields

    @index_fields.setter
    def index_fields(self, index_fields):
        """
        Sets the index_fields of this LookmlModelExplore.
        Array of index fields

        :param index_fields: The index_fields of this LookmlModelExplore.
        :type: list[str]
        """

        self._index_fields = index_fields

    @property
    def sets(self):
        """
        Gets the sets of this LookmlModelExplore.
        Sets

        :return: The sets of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreSet]
        """
        return self._sets

    @sets.setter
    def sets(self, sets):
        """
        Sets the sets of this LookmlModelExplore.
        Sets

        :param sets: The sets of this LookmlModelExplore.
        :type: list[LookmlModelExploreSet]
        """

        self._sets = sets

    @property
    def errors(self):
        """
        Gets the errors of this LookmlModelExplore.
        Errors

        :return: The errors of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this LookmlModelExplore.
        Errors

        :param errors: The errors of this LookmlModelExplore.
        :type: list[LookmlModelExploreError]
        """

        self._errors = errors

    @property
    def fields(self):
        """
        Gets the fields of this LookmlModelExplore.
        Fields

        :return: The fields of this LookmlModelExplore.
        :rtype: LookmlModelExploreFieldset
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this LookmlModelExplore.
        Fields

        :param fields: The fields of this LookmlModelExplore.
        :type: LookmlModelExploreFieldset
        """

        self._fields = fields

    @property
    def joins(self):
        """
        Gets the joins of this LookmlModelExplore.
        Views joined into this explore

        :return: The joins of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreJoins]
        """
        return self._joins

    @joins.setter
    def joins(self, joins):
        """
        Sets the joins of this LookmlModelExplore.
        Views joined into this explore

        :param joins: The joins of this LookmlModelExplore.
        :type: list[LookmlModelExploreJoins]
        """

        self._joins = joins

    @property
    def group_label(self):
        """
        Gets the group_label of this LookmlModelExplore.
        Label used to group explores in the navigation menus

        :return: The group_label of this LookmlModelExplore.
        :rtype: str
        """
        return self._group_label

    @group_label.setter
    def group_label(self, group_label):
        """
        Sets the group_label of this LookmlModelExplore.
        Label used to group explores in the navigation menus

        :param group_label: The group_label of this LookmlModelExplore.
        :type: str
        """

        self._group_label = group_label

    @property
    def supported_measure_types(self):
        """
        Gets the supported_measure_types of this LookmlModelExplore.
        An array of items describing which custom measure types are supported for creating a custom measure 'baed_on' each possible dimension type.

        :return: The supported_measure_types of this LookmlModelExplore.
        :rtype: list[LookmlModelExploreSupportedMeasureType]
        """
        return self._supported_measure_types

    @supported_measure_types.setter
    def supported_measure_types(self, supported_measure_types):
        """
        Sets the supported_measure_types of this LookmlModelExplore.
        An array of items describing which custom measure types are supported for creating a custom measure 'baed_on' each possible dimension type.

        :param supported_measure_types: The supported_measure_types of this LookmlModelExplore.
        :type: list[LookmlModelExploreSupportedMeasureType]
        """

        self._supported_measure_types = supported_measure_types

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
        if not isinstance(other, LookmlModelExplore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
