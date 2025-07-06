import requests
import json
import os
import time
from pprint import pprint


def save_to_database(ip_data, sun_data, user_choice):
    record = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "ip_api_response": ip_data,
        "sun_api_response": sun_data,
        "user_choice": "sunrise" if user_choice == '1' else "sunset"
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


def start_app(lat, lon, ip_data):
    sun_response = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}')
    sun_data = sun_response.json()

    user_choice = input('See sunrise time(1) or sunset time(2)? ')
    if user_choice == '1':
        print(f"Today's sunrise time is at: {sun_data['results']['sunrise']}")
        save_to_database(ip_data, sun_data, user_choice)
        start_app(lat, lon, ip_data)

    elif user_choice == '2':
        print(f"Today's sunset time is at: {sun_data['results']['sunset']}")
        save_to_database(ip_data, sun_data, user_choice)
        start_app(lat, lon, ip_data)


def get_longlat(IP):
    response = requests.get(f'http://ip-api.com/json/{IP}')
    ip_data = response.json()
    lat = ip_data['lat']
    lon = ip_data['lon']
    return lat, lon, ip_data


def view_database():
    file_path = 'database.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                pprint(data)
            except json.JSONDecodeError:
                print("JSON file is empty or corrupted.")
    if print(input("Do you want to view saved data? (y/n): ")).lower() == 'y':
        view_database()



lat, lon, ip_data = get_longlat('188.159.253.226')
start_app(lat, lon, ip_data)

