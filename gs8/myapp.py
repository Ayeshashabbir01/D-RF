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
        'name': 'Ayesha',
        'roll': '15',
        'city': 'Kot'
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, headers=headers, data=json_data)
    print("POST Status Code:", response.status_code)
    print("Response:", response.json())

def update_data():
    data = {
        'id': 4,
        'name': 'Iqra',
        'roll':'104',
        'city': 'Kts',
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, headers=headers, data=json_data)  # Use PUT for updates 
    print("PUT Status Code:", response.status_code)
    print("Response:", response.json())

def delete_data():
    data = {'id': 4}
    json_data = json.dumps(data)
    response = requests.delete(url=URL, headers=headers, data=json_data)
    print("DELETE Status Code:", response.status_code)
    print("Response:", response.json())

# Example function calls
#get_data(1)
post_data()
# update_data()
# delete_data()
