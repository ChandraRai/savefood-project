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
                         'amount': '6 lbs'
                         }]}
    food_info = FoodItem(food)
    food_info.upload_food(my_item)
    food_info_fields = 4

    # assert fails as food item ('my_item') is missing 1 food item detail ('expiry: 2020/11/12')
    assert food_info.__len__() == food_info_fields, "field values are missing"

#
# System Features
# Requirement No. 4.4 - Viewing Food
#
def test_view_food():

    # assert fails as there is 1 food item in the food list
    assert food.__len__() == 0, f"there is {food.__len__()} item in the list"

#
# System Features
# Requirement No. 4.5 - Searching Food
#
def test_search_food_item():
    db = SaveFoodDB()
    db.connect('project/data.json')
    search_item = db.get_data('guava')

    # assert fails as search food item is not found in the food list
    assert search_item == True, "Food item not found!"

#
# System Features
# Requirement No. 4.7 - Placing Food Request
#
def test_place_request():
    request_list = dict()
    item = {"fooType": "fruit",
            "foodDetails": "apple"
            }
    expected_request_placed = True
    request = RequestItem(request_list)
    actual_request_placed = request.place_request(item)

    # assert fails as 1 food item info ("quantity" : "6 lbs") is missing
    assert actual_request_placed is expected_request_placed, "food request can not be placed"

#
# System Features
# Requirement No. 4.8 - Email Alert
#
def test_send_email_alert():
    db = SaveFoodDB()
    db.connect('project/data.json')
    actual_send_email_status = db.send_email_alert('lettuce')
    expected_send_email_status = True

    # assert fails as food item 'status' is available
    assert actual_send_email_status is expected_send_email_status, "food status: available, email not sent"

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

    for item in obj['food']:
        if item['foodName'] == food_to_reserve:
            item['status'] = 'reserved'
            json.dump(obj, db_file, indent=4)

            # assert fails as it finds food item is no more available
            assert item['status'] == "available", "Ops! food is already reserved."

#
# System Features
# Requirement No. 4.9 - Cancelling Food
#
def test_cancel_food():
    db = FoodItem(food)

    # assert fails as to cancel searched food item ('Guava')  is not in the food list
    assert db.cancel_food('Guava') == True, "food item can not be cancelled"















