"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/26

      Filename: user.py
"""

class User:

    def __init__(self):
        self.username = "this_is_invalid_username_length_provided"
        self.password = "password"
        self.email = "chandra@example"

    # takes username and returns TRUE if username length is less than 30
    def is_username_length_valid(self):
        # username length less than 30 is valid
        if len(self.username) < 30:
            return True

    # takes username and returns TRUE if there is no empty space in it
    def has_username_empty_space(self):
        # no empty space
        if ' ' not in self.username:
            return True

    # takes username and returns TRUE if username is string
    def is_username_type_str(self):
        # username is string
        if type(self.username) is str:
            return True

    # verifies username with above username criteria
    def verify_username(self):
        if self.is_username_length_valid() \
                and self.has_username_empty_space() \
                and self.is_username_type_str():
            return True

    # takes email and returns TRUE if it contains '@' and '.' dot
    def is_email_valid(self):
        if '@' and '.' in self.email:
            return True

    # takes password and returns TRUE if it contains uppercase
    def password_contains_uppercase(self):
        if any(letter.isupper() for letter in self.password):
            return True

    # takes password and returns TRUE if it contains lowercase
    def password_contains_lowercase(self):
        if any(letter.islower() for letter in self.password):
            return True

    # takes password and returns TRUE if it contains a number
    def password_contains_number(self):
        if any(number.isdigit() for number in self.password):
            return True

    # verify password it it contains upper, lower, number
    def verify_password(self):
        if self.password_contains_uppercase() \
                and self.password_contains_lowercase() \
                and self.password_contains_number():
            return True

    # takes confirm_password and returns TRUE if they match
    def match_password(self, user_password):
        if self.password == user_password:
            return True

    # takes old password and new password as parameters and returns TRUE if
    # old password matches with previously set password as well as new password meets password requirements
    def update_password(self, old_password, new_password):
        if self.match_password(old_password) \
            and any(letter.isupper() for letter in new_password) \
                and any(number.isdigit() for number in new_password):
            return True

    # returns TRUE if user info (username, password, email) are valid
    def create_user_account(self):
        if self.verify_username() \
            and self.verify_password() \
                and self.is_email_valid():
            return True

    # takes username and password and returns TRUE
    # if username and password match with initialized username and password
    def authenticate_user(self, username, password):
        if self.username == username and self.password == password:
            return True

    # takes user account info (username, password, email) and
    # returns TRUE if user info is verified to be updated
    @staticmethod
    def user_account_update(username, password, email):
        if len(username) < 30 \
                and ' ' not in username \
                and any(letter.isupper() for letter in password) \
                and any(number.isdigit() for number in password) \
                and '@' and '.' in email:
            return True

    # takes a unique user identifier
    # returns None as it is implemented in test_user module itself
    @staticmethod
    def delete_user_account(user_id):
        return None



