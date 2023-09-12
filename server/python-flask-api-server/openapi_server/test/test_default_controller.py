# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.users_post_request import UsersPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_users_get(self):
        """Test case for users_get

        Get a list of users
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Create a new user
        """
        users_post_request = openapi_server.UsersPostRequest()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users',
            method='POST',
            headers=headers,
            data=json.dumps(users_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Get user by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
