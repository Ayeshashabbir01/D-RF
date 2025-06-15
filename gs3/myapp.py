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
    json_data = json.dumps(data)
    response = requests.get(url=URL, headers=headers, data=json_data)
    print("GET Status Code:", response.status_code)
    print("Response:", response.json())

def post_data():
    data = {
        'name': 'faiza',
        'roll': '40',
        'city': 'ryk'
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, headers=headers, data=json_data)
    print("POST Status Code:", response.status_code)
    print("Response:", response.json())

def update_data():
    data = {
        'id': 3,
        'name': 'sana',
        'roll':'41',
        'city': 'sdk',
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, headers=headers, data=json_data)  # Use PUT for updates 
    print("PUT Status Code:", response.status_code)
    print("Response:", response.json())

def delete_data():
    data = {'id': 1}
    json_data = json.dumps(data)
    response = requests.delete(url=URL, headers=headers, data=json_data)
    print("DELETE Status Code:", response.status_code)

    if response.status_code==404:
        print('Data not found')
    else:
        print("Response:",response.json())

# Example function calls
get_data(3)
#post_data()
#update_data()
#delete_data()