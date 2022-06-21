#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By import requests
import requests
url = "https://api.github.com/user/repos"

payload={}
headers = {
  'Authorization': 'token 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'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
