import os
import requests

with open("api.txt","r") as file:
    for line in file:
        if line.strip():  # ignore empty lines
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

api_id = os.environ.get('api_id')
api_key = os.environ.get('api_key')

GENDER = "male"
WEIGHT_KG = "90"
HEIGHT_CM = "178"
AGE = "24"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
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
print(result)