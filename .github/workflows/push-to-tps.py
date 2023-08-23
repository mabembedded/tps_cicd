import os
import requests

oauth_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
}

oauth_data = {
        'grant_type': 'client_credentials',
}

api_key=os.environ.get("API_KEY")
api_secret=os.environ.get("API_SECRET")
oauth_data['client_id'] = api_key
oauth_data['api_secret'] = api_secret

r = requests.post('https://kc.torizon.io/auth/realms/ota-users/protocol/openid-connect/token', headers=oauth_headers, json=oauth_data)

print(r.text)
