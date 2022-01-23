import base64
from auth.creds import username, password

def auth_token():
    # create base64 encoded string of jamf API user credetinals
    credentials_str = f'{username}:{password}'
    data_bytes = credentials_str.encode("utf-8")
    encoded_bytes = base64.b64encode(data_bytes)
    encoded_str = encoded_bytes.decode("utf-8")

    return encoded_str