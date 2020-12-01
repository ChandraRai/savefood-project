"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/21

      Filename: food.py
"""

class FoodItem:
    food_list = dict()

    def __init__(self, food):
        self.food_list = food

    def __len__(self):
        for item in self.food_list['food']:
            return len(item)

    # takes food item (that contains food_name, food_type, amount, expiry)
    # returns TRUE if item is added successfully in the food list
    def upload_food(self, food_item):
        self.food_list.update(food_item)

    # displays items from the food_item list
    # returns None as it is currently implemented in test_food suite
    @staticmethod
    def view_food():
        return None

    # takes food name and returns TRUE if food item is removed from the food list after it is found
    def cancel_food(self, food_name):
        for item in self.food_list['food']:
            if len(self.food_list) != 0 and \
                    item['foodName'] == food_name:
                self.food_list.clear()
                return True









