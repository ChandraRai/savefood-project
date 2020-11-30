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
# Requirement No. 4.1 - Account Registration
#
def test_create_account():
    user = User()
    assert user.create_account() == True, "invalid credentials"

#
# System Features
# Requirement No. 4.2 - Account Authentication
#
def test_authenticate_user():
    username = "Chandra123"
    password = "password"
    user = User()
    # assert fails as password does not match
    assert user.authenticate_user(username, password), "invalid username or password"

#
# System Features
# Requirement No. 4.9 - Account Update
#
def test_account_update():
    account_info = [
        "Chandra",
        "Chandra123",
        "chandra@example.com"
    ]
    for info in account_info:
        assert User.update_account(info) == True, "invalid account info"

