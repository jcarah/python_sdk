# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserAttributeApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def all_user_attribute_group_values(self, user_attribute_id, **kwargs):
        """
        Get User Attribute Group Values
        ### Returns all values of a user attribute defined by user groups, in precedence order.  A user may be a member of multiple groups which define different values for a given user attribute. The order of group-values in the response determines precedence for selecting which group-value applies to a given user.  For more information, see [Set User Attribute Group Values](#!/UserAttribute/set_user_attribute_group_values).  Results will only include groups that the caller's user account has permission to see. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_user_attribute_group_values(user_attribute_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param str fields: Requested fields.
        :return: list[UserAttributeGroupValue]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.all_user_attribute_group_values_with_http_info(user_attribute_id, **kwargs)
        else:
            (data) = self.all_user_attribute_group_values_with_http_info(user_attribute_id, **kwargs)
            return data

    def all_user_attribute_group_values_with_http_info(self, user_attribute_id, **kwargs):
        """
        Get User Attribute Group Values
        ### Returns all values of a user attribute defined by user groups, in precedence order.  A user may be a member of multiple groups which define different values for a given user attribute. The order of group-values in the response determines precedence for selecting which group-value applies to a given user.  For more information, see [Set User Attribute Group Values](#!/UserAttribute/set_user_attribute_group_values).  Results will only include groups that the caller's user account has permission to see. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_user_attribute_group_values_with_http_info(user_attribute_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param str fields: Requested fields.
        :return: list[UserAttributeGroupValue]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_attribute_id', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_user_attribute_group_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_attribute_id' is set
        if ('user_attribute_id' not in params) or (params['user_attribute_id'] is None):
            raise ValueError("Missing the required parameter `user_attribute_id` when calling `all_user_attribute_group_values`")


        collection_formats = {}

        resource_path = '/user_attributes/{user_attribute_id}/group_values'.replace('{format}', 'json')
        path_params = {}
        if 'user_attribute_id' in params:
            path_params['user_attribute_id'] = params['user_attribute_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[UserAttributeGroupValue]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def all_user_attributes(self, **kwargs):
        """
        Get All User Attributes
        ### Get information about all user attributes. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_user_attributes(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param str sorts: Fields to sort by.
        :return: list[UserAttribute]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.all_user_attributes_with_http_info(**kwargs)
        else:
            (data) = self.all_user_attributes_with_http_info(**kwargs)
            return data

    def all_user_attributes_with_http_info(self, **kwargs):
        """
        Get All User Attributes
        ### Get information about all user attributes. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_user_attributes_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param str sorts: Fields to sort by.
        :return: list[UserAttribute]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'sorts']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_user_attributes" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/user_attributes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'sorts' in params:
            query_params['sorts'] = params['sorts']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[UserAttribute]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_user_attribute(self, **kwargs):
        """
        Create User Attribute
        ### Create a new user attribute. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_attribute(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserAttribute body: User Attribute
        :param str fields: Requested fields.
        :return: UserAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_user_attribute_with_http_info(**kwargs)
        else:
            (data) = self.create_user_attribute_with_http_info(**kwargs)
            return data

    def create_user_attribute_with_http_info(self, **kwargs):
        """
        Create User Attribute
        ### Create a new user attribute. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_attribute_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserAttribute body: User Attribute
        :param str fields: Requested fields.
        :return: UserAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_attribute" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/user_attributes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserAttribute',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_user_attribute(self, user_attribute_id, **kwargs):
        """
        Delete User Attribute
        ### Delete a user attribute (admin only). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_attribute(user_attribute_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user_attribute (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_user_attribute_with_http_info(user_attribute_id, **kwargs)
        else:
            (data) = self.delete_user_attribute_with_http_info(user_attribute_id, **kwargs)
            return data

    def delete_user_attribute_with_http_info(self, user_attribute_id, **kwargs):
        """
        Delete User Attribute
        ### Delete a user attribute (admin only). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_user_attribute_with_http_info(user_attribute_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user_attribute (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_attribute_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_attribute_id' is set
        if ('user_attribute_id' not in params) or (params['user_attribute_id'] is None):
            raise ValueError("Missing the required parameter `user_attribute_id` when calling `delete_user_attribute`")


        collection_formats = {}

        resource_path = '/user_attributes/{user_attribute_id}'.replace('{format}', 'json')
        path_params = {}
        if 'user_attribute_id' in params:
            path_params['user_attribute_id'] = params['user_attribute_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_user_attribute_group_values(self, user_attribute_id, body, **kwargs):
        """
        Set User Attribute Group Values
        ### Define values for a user attribute across a set of groups, in priority order.  This function defines all values for a user attribute defined by user groups. This is a global setting, potentially affecting all users in the system. This function replaces any existing group value definitions for the indicated user attribute.  The value of a user attribute for a given user is determined by searching the following locations, in this order:  1. the user's account settings 2. the groups that the user is a member of 3. the default value of the user attribute, if any  The user may be a member of multiple groups which define different values for that user attribute. The order of items in the group_values parameter determines which group takes priority for that user. Lowest array index wins.  An alternate method to indicate the selection precedence of group-values is to assign numbers to the 'rank' property of each group-value object in the array. Lowest 'rank' value wins. If you use this technique, you must assign a rank value to every group-value object in the array.  To set a user attribute value for a single user, see [Set User Attribute User Value](#!/User/set_user_attribute_user_value). To set a user attribute value for all members of a group, see [Set User Attribute Group Value](#!/Group/update_user_attribute_group_value). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_user_attribute_group_values(user_attribute_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param list[UserAttributeGroupValue] body: Array of group values. (required)
        :return: list[UserAttributeGroupValue]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_user_attribute_group_values_with_http_info(user_attribute_id, body, **kwargs)
        else:
            (data) = self.set_user_attribute_group_values_with_http_info(user_attribute_id, body, **kwargs)
            return data

    def set_user_attribute_group_values_with_http_info(self, user_attribute_id, body, **kwargs):
        """
        Set User Attribute Group Values
        ### Define values for a user attribute across a set of groups, in priority order.  This function defines all values for a user attribute defined by user groups. This is a global setting, potentially affecting all users in the system. This function replaces any existing group value definitions for the indicated user attribute.  The value of a user attribute for a given user is determined by searching the following locations, in this order:  1. the user's account settings 2. the groups that the user is a member of 3. the default value of the user attribute, if any  The user may be a member of multiple groups which define different values for that user attribute. The order of items in the group_values parameter determines which group takes priority for that user. Lowest array index wins.  An alternate method to indicate the selection precedence of group-values is to assign numbers to the 'rank' property of each group-value object in the array. Lowest 'rank' value wins. If you use this technique, you must assign a rank value to every group-value object in the array.  To set a user attribute value for a single user, see [Set User Attribute User Value](#!/User/set_user_attribute_user_value). To set a user attribute value for all members of a group, see [Set User Attribute Group Value](#!/Group/update_user_attribute_group_value). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_user_attribute_group_values_with_http_info(user_attribute_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param list[UserAttributeGroupValue] body: Array of group values. (required)
        :return: list[UserAttributeGroupValue]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_attribute_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_user_attribute_group_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_attribute_id' is set
        if ('user_attribute_id' not in params) or (params['user_attribute_id'] is None):
            raise ValueError("Missing the required parameter `user_attribute_id` when calling `set_user_attribute_group_values`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_user_attribute_group_values`")


        collection_formats = {}

        resource_path = '/user_attributes/{user_attribute_id}/group_values'.replace('{format}', 'json')
        path_params = {}
        if 'user_attribute_id' in params:
            path_params['user_attribute_id'] = params['user_attribute_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[UserAttributeGroupValue]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_user_attribute(self, user_attribute_id, body, **kwargs):
        """
        Update User Attribute
        ### Update a user attribute definition. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user_attribute(user_attribute_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param UserAttribute body: User Attribute (required)
        :param str fields: Requested fields.
        :return: UserAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_user_attribute_with_http_info(user_attribute_id, body, **kwargs)
        else:
            (data) = self.update_user_attribute_with_http_info(user_attribute_id, body, **kwargs)
            return data

    def update_user_attribute_with_http_info(self, user_attribute_id, body, **kwargs):
        """
        Update User Attribute
        ### Update a user attribute definition. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_user_attribute_with_http_info(user_attribute_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param UserAttribute body: User Attribute (required)
        :param str fields: Requested fields.
        :return: UserAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_attribute_id', 'body', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_attribute_id' is set
        if ('user_attribute_id' not in params) or (params['user_attribute_id'] is None):
            raise ValueError("Missing the required parameter `user_attribute_id` when calling `update_user_attribute`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_attribute`")


        collection_formats = {}

        resource_path = '/user_attributes/{user_attribute_id}'.replace('{format}', 'json')
        path_params = {}
        if 'user_attribute_id' in params:
            path_params['user_attribute_id'] = params['user_attribute_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserAttribute',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def user_attribute(self, user_attribute_id, **kwargs):
        """
        Get User Attribute
        ### Get information about a user attribute. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_attribute(user_attribute_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param str fields: Requested fields.
        :return: UserAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.user_attribute_with_http_info(user_attribute_id, **kwargs)
        else:
            (data) = self.user_attribute_with_http_info(user_attribute_id, **kwargs)
            return data

    def user_attribute_with_http_info(self, user_attribute_id, **kwargs):
        """
        Get User Attribute
        ### Get information about a user attribute. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_attribute_with_http_info(user_attribute_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_attribute_id: Id of user attribute (required)
        :param str fields: Requested fields.
        :return: UserAttribute
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_attribute_id', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_attribute_id' is set
        if ('user_attribute_id' not in params) or (params['user_attribute_id'] is None):
            raise ValueError("Missing the required parameter `user_attribute_id` when calling `user_attribute`")


        collection_formats = {}

        resource_path = '/user_attributes/{user_attribute_id}'.replace('{format}', 'json')
        path_params = {}
        if 'user_attribute_id' in params:
            path_params['user_attribute_id'] = params['user_attribute_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserAttribute',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)