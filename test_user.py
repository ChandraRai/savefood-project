"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/21

      Filename: test_user.py
"""
from project.user import User

#
# System Features
# Requirement No. 4.1 - User Account Registration
#
def test_is_username_length_valid():
    user = User()

    # assert fails as username is invalid
    assert user.is_username_length_valid() is True, "username length must be less than 30 characters"

def test_has_username_empty_space():
    user = User()

    # assert passes as username does not contain space
    assert user.has_username_empty_space() is True, "username cannot contain space"

def test_is_email_valid():
    user = User()

    # assert fails as it does not contain .
    assert user.is_email_valid() is True, "invalid email"


def test_password_contains_lowercase():
    user = User()

    # assert passes as it contains lowercase
    assert user.password_contains_lowercase() is True, "password does not contain lowercase"

def test_password_contains_number():
    user = User()

    # assert fails as it does not contain number
    assert user.password_contains_number() is True, "password does not contain numeric value(s)"

def test_create_user_account():
    user = User()

    # assert fails as user info is invalid : Password does not meet requirements
    assert user.create_user_account() == True, "invalid credentials"

#
# System Features
# Requirement No. 4.2 - User Account Authentication
#
def test_authenticate_user():
    username = "Chandra123"
    password = "password"
    user = User()

    # assert fails as password does not match
    assert user.authenticate_user(username, password), "invalid username or password"

#
# System Features
# Requirement No. 4.9 - User Account Update
#
def test_user_account_update_with_invalid_credentials():
    invalid_user_info = {
        "username": "chandra",
        "password": "Password123",
        "email": "aaa@aaa"
    }

    # assert fails as user account info is invalid - email not valid
    assert User.user_account_update(invalid_user_info['username'], invalid_user_info['password'],
                                    invalid_user_info['email']) is True, f"invalid user info - {invalid_user_info}"

def test_user_account_update_with_valid_credentials():
    invalid_user_info = {
        "username": "chandra",
        "password": "Password123",
        "email": "chandra@example.com"
    }

    # assert passes as user account info is valid - meet all username, password, and email requirements
    assert User.user_account_update(invalid_user_info['username'], invalid_user_info['password'],
                                    invalid_user_info['email']) is True, f"invalid user info - {invalid_user_info}"

#
# System Features
# Requirement No. 4.11 - Password Update
#
def test_fail_password_update():
    user = User()
    old_password = "Password"
    new_password = "Chandra"
    update_password = user.update_password(old_password, new_password)

    # assert fails as new password does not meet password requirements
    assert update_password is True, "invalid password"

def test_pass_password_update():
    user = User()
    old_password = "password"
    new_password = "Chandra123"
    update_password = user.update_password(old_password, new_password)

    # assert passes as old password matches with the system password
    # and new password meets password requirements
    assert update_password is True, "invalid password"

#
# System Features
# Requirement No. 4.12 - User Account Deletion
#
def test_fail_delete_user_account():
    user_info = {"user": [{
            "user_id": 101,
            "username": "chandra",
            "password": "Chandra123",
            "email": "chandra@example.com"
        }]
    }
    user_list = dict()
    user_list.update(user_info)

    for user in user_list['user']:
        if user['user_id'] is 102:
            user_list.clear()
            return True

    # assert fails as user id (102) is not found in the user list
    assert user_list is True, "user account could not be deleted, specified user id not found"

def test_pass_delete_user_account():
    user_info = {"user": [{
            "user_id": 101,
            "username": "chandra",
            "password": "Chandra123",
            "email": "chandra@example.com"
        }]
    }
    user_list = dict()
    user_list.update(user_info)

    for user in user_list['user']:
        if user['user_id'] is 101:
            user_list.clear()
            return True

    # assert passes as user id (101) is found in the user list
    assert user_list is True, "user account could not be deleted, specified user id not found"
