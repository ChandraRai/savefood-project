"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/21

      Filename: _db_.py
"""
import json

class SaveFoodDB:
    def __init__(self):
        self._data = None

    # connect to mock DB (data.json)
    def connect(self, data_file):
        with open(data_file) as json_file:
            self._data = json.load(json_file)

    # takes food name and returns TRUE if found
    def get_data(self, food_name):
        for item in self._data['food']:
            if item['foodName'] == food_name:
                return True

    # returns TRUE as to set flag to email sent if food item status is "Reserved"
    def send_email_alert(self, food_name):
        for item in self._data['food']:
            if item['foodName'] == food_name and item['status'] == 'reserved':
                return True











