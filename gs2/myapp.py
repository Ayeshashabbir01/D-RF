import requests
import json
URL ="http://127.0.0.1:8000/stucreate/"
headers={
    'Content-Type':'application/json'
}
data = {
'name':'james',
'roll': 43,
'city':'ryk'
}
json_data = json.dumps(data)
r = requests.post(url = URL,headers=headers, data = json_data)
data = r.json()
print(data)