import requests
import json

URL = "http://127.0.0.1:8000/studentapi/" 

headers = {
    'Content-Type': 'application/json'
}

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    response = requests.get(url=URL, headers=headers, json=data)
    print("GET Status Code:", response.status_code)
    print("Response:", response.json())

def post_data():
    data = {
        'name': 'Ayesha',
        'roll': '15',
        'city': 'Kot'
    }
    response = requests.post(url=URL, headers=headers, json=data)
    print("POST Status Code:", response.status_code)
    print("Response:", response.json())

def update_data():
    data = {
        'id': 4,
        'name': 'Iqra',
        'roll': '104',
        'city': 'Kts',
    }
    response = requests.put(url=URL, headers=headers, json=data)
    print("PUT Status Code:", response.status_code)
    print("Response:", response.json())

def delete_data():
    data = {'id': 4}
    response = requests.delete(url=URL, headers=headers, json=data)
    print("DELETE Status Code:", response.status_code)
    print("Response:", response.json())

# Example function calls
# get_data(2)
post_data()
# update_data()
# delete_data()
