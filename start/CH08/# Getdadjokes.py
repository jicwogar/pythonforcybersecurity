# Getdadjokes
import requests
import json

url = "https://icanhazdadjoke.com/"

payload={}
headers = { 
    'Accept': 'application/json'
    }

r = requests.request("GET", url, headers=headers, data=payload)
data = r.json()

print(data [ 'joke'])
