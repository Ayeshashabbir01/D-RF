import requests
import json

URL = "http://127.0.0.1:8000/studentapi/" 

headers = {
    'Content-Type': 'application/json'
}

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}  # Pass 'id' as a query parameter
    response = requests.get(url=URL, headers=headers, params=params)  # Use 'params' instead of 'json'
    print("GET Status Code:", response.status_code)
    if response.status_code == 200:
        try:
            print("Response:", response.json())  # Safely parse JSON response
        except json.decoder.JSONDecodeError:
            print("Error: Unable to parse JSON response")
    else:
        print("Error: Server returned status code", response.status_code)

def post_data():
    data = {
        'name': 'ayesha',
        'roll': '109',
        'city': 'sdk'
    }
    response = requests.post(url=URL, headers=headers, json=data)
    print("POST Status Code:", response.status_code)
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error: Server returned status code", response.status_code)

def update_data():
    data = {
        'id': 3,
        'name': 'Aisha',
        'roll': '102',
        'city': 'Kts',
    }
    response = requests.put(url=URL, headers=headers, json=data)
    print("PUT Status Code:", response.status_code)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error: Server returned status code", response.status_code)

def delete_data():
    data = {'id': 3}
    response = requests.delete(url=URL, headers=headers, json=data)
    print("DELETE Status Code:", response.status_code)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error: Server returned status code", response.status_code)

# Example function calls
#get_data()
#post_data()
#update_data()
delete_data()