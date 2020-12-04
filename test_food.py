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
# Requirement No. 4.4 - Viewing Food
#
food = dict()
def test_view_food():
    expected_food_item_number = 1

    # assert fails as there is no food item in the food list
    assert food.__len__() is expected_food_item_number, f"there is {food.__len__()} item in the food item list"

#
# System Features
# Requirement No. 4.3 - Uploading Food
#
def test_fail_upload_food():
    my_item = {"food": [{'foodName': 'apple',
                         'foodType': 'fruit',
                         'amount': '6 lbs'
                         }]}
    food_info = FoodItem(food)
    food_info.upload_food(my_item)
    food_info_fields = 4

    # assert fails as food item to be uploaded is missing 1 food item detail ('expiry: 2020/11/12')
    assert food_info.__len__() == food_info_fields, "field values are missing"

def test_pass_upload_food():
    my_item = {"food": [{'foodName': 'apple',
                         'foodType': 'fruit',
                         'amount': '6 lbs',
                         'expiry': '2020/11/12'
                         }]}
    food_info = FoodItem(food)
    food_info.upload_food(my_item)
    food_info_fields = 4

    # assert passes as food item has all necessary details
    assert food_info.__len__() == food_info_fields, "field values are missing"

#
# System Features
# Requirement No. 4.5 - Searching Food
#
def test_fail_search_food_item():
    db = SaveFoodDB()
    db.connect('project/data.json')
    search_item = db.get_data('guava')

    # assert fails as searched food item is not found in the food item list
    assert search_item is True, "food item not found!"

def test_pass_search_food_item():
    db = SaveFoodDB()
    db.connect('project/data.json')
    search_item = db.get_data('apple')

    # assert passes as searched food item is in the food item list
    assert search_item is True, "food item not found!"

#
# System Features
# Requirement No. 4.6 - Reserving Food
#
def test_fail_reserve_food():
    # connect to db (data.json file)
    db_file = open("project/data.json")
    obj = json.load(db_file)
    db_file = open("project/data.json", "w")
    food_to_reserve = "apple"

    for item in obj['food']:
        if item['foodName'] == food_to_reserve:
            item['status'] = 'reserved'
            json.dump(obj, db_file, indent=4)
            db_file.close()

            # assert fails as it finds food item is no more available
            assert item['status'] == "available", "Ops! food is already reserved."


def test_pass_reserve_food():
    # connect to db (data.json file)
    db_file = open("project/data.json", "r")
    obj = json.load(db_file)
    food_to_reserve = "lettuce"

    for item in obj['food']:
        if item['foodName'] == food_to_reserve:

            # assert passes as food item is available
            assert item['status'] == "available", "Ops! food is already reserved."

#
# System Features
# Requirement No. 4.7 - Placing Food Request
#
def test_place_request_with_incomplete_food_item_details():
    request_list = dict()
    food_item = {"fooType": "fruit",
            "foodDetails": "apple"
            }
    expected_request_placed = True
    request = RequestItem(request_list)
    actual_request_placed = request.place_request(food_item)

    # assert fails as 1 food item detail ("quantity" : "6 lbs") is missing
    assert actual_request_placed is expected_request_placed, "food request can not be placed"

def test_place_request_with_empty_food_item():
    request_list = dict()
    food_item = {}
    expected_request_placed = True
    request = RequestItem(request_list)
    actual_request_placed = request.place_request(food_item)

    # assert fails as it is missing food item details - fields empty
    assert actual_request_placed is expected_request_placed, "please, provide food item details"

def test_pass_place_request():
    request_list = dict()
    food_item = {"fooType": "fruit",
                 "foodDetails": "apple",
                 "quantity": "6 lbs"
                }
    expected_request_placed = True
    request = RequestItem(request_list)
    actual_request_placed = request.place_request(food_item)

    # assert passes as food item contains all required food item details
    assert actual_request_placed is expected_request_placed, "food request can not be placed"

#
# System Features
# Requirement No. 4.8 - Email Alert
#
def test_fail_send_email_alert():
    db = SaveFoodDB()
    db.connect('project/data.json')
    actual_send_email_status = db.send_email_alert('lettuce')
    expected_send_email_status = True

    # assert fails as food item 'status' is available (send email is triggered for food item successfully reserved)
    assert actual_send_email_status is \
           expected_send_email_status, f"email not sent, food status: {db.get_food_status('lettuce')}, "


#
# System Features
# Requirement No. 4.9 - Cancelling Food
#
def test_fail_cancel_food():
    db = FoodItem(food)

    # assert fails as to cancel searched food item ('Guava')  is not in the food item list
    assert db.cancel_food('Guava') is True, "food item can not be cancelled"

def test_pass_cancel_food():
    db = FoodItem(food)

    # assert passes as to cancel searched food item ('Guava')  is in the food item list
    assert db.cancel_food('apple') is True, "food item can not be cancelled"















