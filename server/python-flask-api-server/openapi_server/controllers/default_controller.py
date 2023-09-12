import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.users_post_request import UsersPostRequest  # noqa: E501
from openapi_server import util


def users_get():  # noqa: E501
    """Get a list of users

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def users_post(users_post_request):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param users_post_request: 
    :type users_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        users_post_request = UsersPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'user added'


def users_user_id_get(user_id):  # noqa: E501
    """Get user by ID

     # noqa: E501

    :param user_id: ID of the user
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'
