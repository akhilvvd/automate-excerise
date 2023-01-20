# import requests
# from datetime import datetime
#
# application_id = "4b976c75"
# application_key = "a5fec9e643c68b99b92094cf682d3cc5"
# sheet = "https://api.sheety.co/e81f9c2318f46ed57ad5b723b6da4a4d/myWorkouts/workouts"
#
# exercise_text = input("Tell me which exercise you did: ")
# params = {
#     "query": exercise_text,
#     "gender": "male",
#     "weight_kg": 65,
#     "height_cm": 180,
#     "age": 22
# }
#
# headers = {
#     "x-app-id": application_id,
#     "x-app-key": application_key
# }
#
# ex = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
# response = requests.post(url=ex, json=params, headers=headers)
# data = response.json()
# print(data)
#
# today_date = datetime.now().strftime("%d%m%Y")
# time_now = datetime.now().strftime("%X")
# auth = {
#     "Authorization": "Basic YmF0bWFudjpBa2hpbDk5OUA="
# }
# for exercise in data["exercises"]:
#     sheet_input = {
#         "workout": {
#             "Date": today_date,
#             "Time": time_now,
#             "Exercise": exercise["name"].title(),
#             "Duration": exercise["duration_min"],
#             "Calories": exercise["nf_calories"]
#
#         }
#     }
#     res = requests.post(url=sheet, json=sheet_input, headers=auth)
#     print(res.text)
#
#
#
import requests
from datetime import datetime

GENDER = "m"
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 22

APP_ID = "4b976c75"
API_KEY = "a5fec9e643c68b99b92094cf682d3cc5"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e81f9c2318f46ed57ad5b723b6da4a4d/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
auth = {
    "Authorization": "Basic YmF0bWFudjpBa2hpbDk5OUA="
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=auth)

    print(sheet_response.text)