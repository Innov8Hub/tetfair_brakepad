from django.test import TestCase
import requests


# Create your tests here.
#test quickrun
speed = input("Enter speed in km/h: ")
brakePower = input("Enter brake power in PSI: ")
brakeTime = input("Enter brake time in seconds: ")
restTime = input("Enter rest time in seconds: ")
repeat = input("Enter how many times to repeat quickrun: ")

data = {
    'speed': speed,
    'brakePower': brakePower,
    'brakeTime': brakeTime,
    'restTime': restTime,
    'repeat': repeat
}

response = requests.post('http://127.0.0.1:8000/api/submit_quickrun/', json=data)

print(response.json())