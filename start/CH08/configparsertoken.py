import requests
import configparser

def get_api_key(key_name):
    # create configuration parser object amd load file
    config = configparser.ConfigParser()
    config.read("/home/kali/secrets.ini")
    # get the API key and return
    api_key = config["APIkeys"][key_name]
    return api_key
# Get API key from file
token = get_api_key("GitHub")

url = "https://api.github.com/user/repos"

payload={}
headers = {
  'Authorization': 'token' + token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
