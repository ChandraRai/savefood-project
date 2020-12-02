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
def test_user_account_update():
    invalid_user_info = {
        "username": "chandra",
        "password": "Password123",
        "email": "aaa@aaa"
    }

    # assert fails as user account info is invalid - not matching the requirement
    assert User.update_user_account(invalid_user_info['username'], invalid_user_info['password'],
                                    invalid_user_info['email']) == True, f"invalid user info {invalid_user_info}"

#
# System Features
# Requirement No. 4.11 - Password Update
#
def test_password_update():
    user = User()
    old_password = "Password"
    new_password = "Chandra"
    update_password = user.update_password(old_password, new_password)

    # assert fails as new password does not meet password requirements
    assert update_password == True, "invalid password"

#
# System Features
# Requirement No. 4.12 - User Account Deletion
#
def test_delete_user_account():
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

    # this is a pass test case
    # asserts passes as user id (101) is found in the user list
    assert user_list is True, 'user account not deleted'
