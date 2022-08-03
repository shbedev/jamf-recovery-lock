import os, time, requests
from auth.creds import instance_id
from auth.basic_auth import auth_token

# current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

# path of token file in current working directory
token_file = f'{cwd}/token.txt'

def request_token():
    """Generate an auth token from API"""
    
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Basic {auth_token()}',
        'Content-Type': 'application/json',
    } 

    try:
        response = requests.request("POST", f'https://{instance_id}/api/v1/auth/token', headers=headers)
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return response.json()['token']

def get_token():
    """Returns a token from local cache or API request"""
    current_time = int(time.time())

    # check if token is cached and if it is less than 30 minutes old
    if os.path.exists(token_file) and ((current_time - 1800) < os.stat(token_file)[-1]):
        # return a cached token from file
        return read_token_from_local()
    else:
        # return a token from API
        return get_token_from_api()

def get_token_from_api():
    """Returns a token from an API request"""
    token = request_token()
    cache_token(token)
    return token

def cache_token(token):
    """
    Cache token to local file
    Parameters:
        token - str
    """
    with open(token_file, 'w') as file_obj:
        file_obj.write(token)

def read_token_from_local():
    """Read cached token from local file"""
    with open(token_file, 'r') as file_obj:
        token = file_obj.read().strip()
    return token