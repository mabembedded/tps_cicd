import os
import requests

base_url = 'https://app.torizon.io/api/v2beta/'

oauth_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
}

oauth_data = {
        'grant_type': 'client_credentials',
}

api_key=os.environ.get("API_KEY")
api_secret=os.environ.get("API_SECRET")
oauth_data['client_id'] = api_key
oauth_data['client_secret'] = api_secret

r = requests.post('https://kc.torizon.io/auth/realms/ota-users/protocol/openid-connect/token', headers=oauth_headers, data=oauth_data)
response = r.json()
access_token = response['access_token']

secure_headers = dict()
secure_headers = {
        'Authorization': 'Bearer ' + access_token
}

url = base_url + '/devices'
response = requests.get(url, headers=secure_headers)
print(response.json())
