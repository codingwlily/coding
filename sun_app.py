import requests

def start_app(lat, lon):
    sunset_api = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}')
    user_choice = input('See sunrise time(1) or sunset time(2)?')
    if user_choice == '1':
        sunrise_time = sunset_api.json()['results']['sunrise']
        print(f'Todays sunrise time is at: {sunrise_time}')
        start_app(lat, lon)
    elif user_choice == '2':
        sunset_time = sunset_api.json()['results']['sunset']
        print(f'Todays sunset time is at: {sunset_time}')
        start_app(lat, lon)   
    
def get_longlat(IP):
    data = requests.get(f'http://ip-api.com/json/{IP}')
    data = data.json()
    lat = data['lat']
    lon = data['lon']
    return lat, lon
208
lat, lon = get_longlat('188.159.253.226')

start_app(lat, lon)
