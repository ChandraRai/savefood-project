"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/21

      Filename: _db_.py
"""
import json
import smtplib


class SaveFoodDB:
    def __init__(self):
        self._data = None

    # connect to Save Food DB (data.json)
    def connect(self, data_file):
        with open(data_file) as json_file:
            self._data = json.load(json_file)

    # takes food name and returns TRUE if found
    def get_data(self, food_name):
        for item in self._data['food']:
            if item['foodName'] == food_name:
                return True

    # takes food name and returns its status if found
    def get_food_status(self, food_name):
        for item in self._data['food']:
            if item['foodName'] == food_name:
                return item['status']

    # returns TRUE if food item status is "Reserved" as to indicate email sent
    def send_email_alert(self, food_name):
        for item in self._data['food']:
            if item['foodName'] == food_name \
                    and item['status'] == 'reserved':
                # send email
                msg = "Hello, your food item is reserved"
                msg['Subject'] = 'The food item is reserved!'
                msg['From'] = "admin@example.com"
                msg['To'] = "chandra@example.com"

                s = smtplib.SMTP('localhost')
                s.sendmail(msg)
                s.quit()
                # returns True after email sent
                return True









