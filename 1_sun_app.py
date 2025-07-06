import requests
import json
import os
import time
from pprint import pprint

def check_time(ip_data, lat, lon):
    user_choice = input("See sunrise time (1) or sunset time (2)? ")
    sun_response = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}')
    sun_data = sun_response.json()

    if user_choice == '1':
        print(f"Today's sunrise time is at: {sun_data['results']['sunrise']}")
    else:
        print(f"Today's sunset time is at: {sun_data['results']['sunset']}")

    save_to_database(ip_data, sun_data, user_choice)

def save_to_database(ip_data, sun_data, user_choice):
    record = {
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "ip_api_response": ip_data,
    "sun_api_response": sun_data,
    "user_choice": "sunrise" if user_choice == "1" else 'sunset'
    }

    file_path = 'database.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(record)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def view_database():
    file_path = 'database.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                pprint(data)
            except json.JSONDecodeError:
                print("JSON file is empty or corrupted.")
    else:
        print("No database file found.")


def get_longlat(IP):
    response = requests.get(f'http://ip-api.com/json/{IP}')
    ip_data = response.json()
    lat = ip_data['lat']
    lon = ip_data['lon']
    return lat, lon, ip_data


def start_app():
    while True:
        next_action = input("\nWhat would you like to do?\n"
                            "1. View saved data\n"
                            "2. Check another time\n"
                            "3. Exit\n"
                            "Choose 1, 2, or 3: ")

        if next_action == '1':
            view_database()
        elif next_action == '2':
            lat, lon, ip_data = get_longlat('188.159.253.226')
            check_time(ip_data, lat, lon)
        elif next_action == '3':
            print("Goodbye!")
            break
            
# start_app()
print(time.strftime("%H:%M:%S:%W %Y-%m-%d"), time.localtime())