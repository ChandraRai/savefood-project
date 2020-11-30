"""
      Designed by: Chandra K. Rai
      Student ID: 400351588
      Submitted to: Prof. Sean Watson
      Date: 2020/11/21

      Filename: test_food.py
"""
import json
from project.__db__ import SaveFoodDB
from project.food import FoodItem
from project.food_request import RequestItem

#
# System Features
# Requirement No. 4.3 - Uploading Food
#
food = dict()
def test_upload_food():
    my_item = {"food": [{'foodName': 'apple',
                         'foodType': 'fruit',
                         'amount': '6 lbs',
                         'expiry': '2020/11/12'
                         }]}
    food_info = FoodItem(food)
    food_info.upload_food(my_item)
    food_info_fields = 4

    assert food_info.__len__() == food_info_fields, "field values are missing"

#
# System Features
# Requirement No. 4.4 - Viewing Food
#
def test_view_food():

    # assert fails as there is 1 item in the food list
    assert food.__len__() == 0, f"there is {food.__len__()} item in the list"

#
# System Features
# Requirement No. 4.5 - Searching Food
#
def test_search_food_item():
    search_item = 'apple'
    db = SaveFoodDB()
    db.connect('project/data.json')
    data = db.get_data('apple')

    # assert passes as search item is found in the food list
    assert data['foodName'] == search_item, "value not matching"

#
# System Features
# Requirement No. 4.6 - Reserving Food
#
def test_reserve_food():
    # connect to db (data.json file)
    db_file = open("project/data.json")
    obj = json.load(db_file)
    db_file = open("project/data.json", "w")

    food_to_reserve = "apple"
    # find food to reserve and check if food is reserved
    for item in obj['food']:
        if item['foodName'] == food_to_reserve:
            item['status'] = 'reserved'
            json.dump(obj, db_file, indent=4)

            assert item['status'] == "reserved"

#
# System Features
# Requirement No. 4.7 - Placing Food Request
#
def test_place_request():
    request_list = dict()
    item = {"fooType": "fruit",
            "foodDetails": "apple",
            "Quantity": "6 lbs"}
    expected_request_placed = True
    request = RequestItem(request_list)
    actual_request_placed = request.place_request(item)

    assert actual_request_placed == expected_request_placed, "food request can not be placed"

#
# System Features
# Requirement No. 4.8 - Email Alert
#
def test_send_email_alert():
    expected_send_email = True
    db = SaveFoodDB()
    db.connect('project/data.json')
    actual_send_email = db.send_email_alert()

    assert actual_send_email == expected_send_email, "email not sent as food status: available"

#
# System Features
# Requirement No. 4.9 - Cancelling Food
#
def test_cancel_food():
    db = FoodItem(food)

    assert db.cancel_food('apple') == True, "food item can not be cancelled"















