import requests
import math

from auth.creds import instance_id
from auth.bearer_auth import get_token

headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {get_token()}',
    'Content-Type': 'application/json',
}

def get_computer_count():
    """
    Returns the number of computers in Jamf Pro
    """

    try:
        response = requests.get(
            url=f'https://{instance_id}.jamfcloud.com/api/v1/computers-inventory?section=HARDWARE&page=0&page-size=1&sort=id%3Aasc',
            headers=headers
        )
        response.raise_for_status()
    
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    count = response.json()['totalCount']

    return count

computers_per_page = 1000
number_of_pages = math.ceil(get_computer_count() / computers_per_page)

def get_arm64(filter = None):
    """
    Returns Jamf IDs of all arm64 type computers
    
    Parameters:
        filter - (e.g. 'filter=general.name=="jdoe-mbp"'). If empty, returns all computers.
        Computer name in filter is not case sensitive 
    """

    computers_id = []

    for pageIndex in range(number_of_pages):

        try:
            response = requests.get(
                url=f'https://{instance_id}.jamfcloud.com/api/v1/computers-inventory?section=HARDWARE&page={pageIndex}&page-size={computers_per_page}&sort=id%3Aasc&{filter}',
                headers=headers
            )
            response.raise_for_status()
        
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        computers = response.json()['results']

        for computer in computers:
            if computer['hardware']['processorArchitecture'] == 'arm64':
                computers_id.append(computer['id'])

    return computers_id


def get_mgmt_id(computers_id):
    """
    Returns Jamf computers management id
    
    Parameters:
        computers_id - (e.g. ['10', '12']]). List of Jamf computers id 
    """

    for pageIndex in range(number_of_pages):
        try:
            response = requests.get(
                url = f'https://{instance_id}.jamfcloud.com/api/preview/computers?page={pageIndex}&page-size={computers_per_page}&sort=name%3Aasc',
                headers=headers
            )
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        computers_mgmt_id = []

        computers = response.json()['results']

        for computer_id in computers_id:
            for computer in computers:
                # Find computers that given computer id in list of computers
                if computer['id'] == computer_id:
                    computer_mgmt_id = computer['managementId']
                    computer_name = computer['name']
                    # Add computer to list
                    computers_mgmt_id.append({
                        'id': computer_id,
                        'name': computer_name,
                        'mgmt_id': computer_mgmt_id
                    })
                    break

    return computers_mgmt_id