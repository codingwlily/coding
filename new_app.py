import requests
from mypackage import my_function1, my_function2
from dotenv import load_dotenv
import os

load_dotenv()

cat_key = os.getenv('cat_key')
print(cat_key)




def cat_facts():
    response = requests.post('https://api.thecatapi.com/v1/images/search', json={"mypass":"cat_key"})
    return response






