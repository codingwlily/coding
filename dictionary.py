from list import save_to_file
import requests
from pprint import pprint

sunset_api = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400')
# sunrise_time = sunset_api.json()['results']['sunrise']
# print(f'Hello, todays sunrise time is at: {sunrise_time}')
def start_app():
  user_choice = input('Would you like to see sunrise time(1) or sunset time(2)?')
  if user_choice == '1':
    sunrise_time = sunset_api.json()['results']['sunrise']
    print(f'Hello, todays sunrise time is at: {sunrise_time}')
    start_app()
  elif user_choice == '2':
    sunset_time = sunset_api.json()['results']['sunset']
    print(f'Hello, todays sunset time is at: {sunset_time}')
    start_app()
  
start_app()

status_code = sunset_api.status_code
if status_code == 200:
  start_app()
else: 
  print('unidentified error')




  



