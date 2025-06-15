import requests

URL = "http://127.0.0.1:8000/stuinfo/1"
headers = {
    'Content-Type': 'application/json',
}

r = requests.get(url=URL, headers=headers)
data = r.json()
print(data)