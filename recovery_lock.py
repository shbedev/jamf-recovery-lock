import requests

from auth.bearer_auth import get_token
from auth.creds import instance_id

headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {get_token()}',
    'Content-Type': 'application/json',
}

def set_key(computer_name, management_id, recovery_lock_key):
    """Sets a Recovery Lock key for a given computer"""
    
    print(f'Settings recovery lock key: {recovery_lock_key} for {computer_name}')

    payload = {
        'clientData': [
            {
            'managementId': f'{management_id}',
            'clientType': 'COMPUTER'
            }
        ],
        'commandData': {
            'commandType': 'SET_RECOVERY_LOCK',
            'newPassword': f'{recovery_lock_key}'
        }
    }

    try:
        response = requests.request("POST", f'https://{instance_id}/api/preview/mdm/commands', headers=headers, json=payload)

        response.raise_for_status()
        
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)