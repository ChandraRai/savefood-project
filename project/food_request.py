"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/21

      Filename: food_request.py
"""

class RequestItem:
    request_list = dict()

    def __init__(self, request_list):
        self.request_list = request_list

    def __len__(self):
        return len(self.request_list)

    # takes a food item (that contains food_type, food_details, quantity)
    # then updates and returns TRUE if the food item contains all 3 food item details
    def place_request(self, food_item):
        if len(food_item) == 4:
            self.request_list.update(food_item)
            return True

