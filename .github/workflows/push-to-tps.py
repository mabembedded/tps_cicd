import os
import requests

oauth_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
}

oauth_data = {
        'grant_type': 'client_credentials',
}

api_key=os.environ.get("API_KEY")
print(api_key)
api_secret=os.environ.get("API_SECRET")
print(api_secret)
oauth_data['client_id'] = api_key
oauth_data['client_secret'] = api_secret

r = requests.post('https://kc.torizon.io/auth/realms/ota-users/protocol/openid-connect/token', headers=oauth_headers, data=oauth_data)

print(r.text)
