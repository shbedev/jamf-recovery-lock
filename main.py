from random import randint
from computers import get_arm64, get_mgmt_id
from recovery_lock import set_key

computers_id = get_arm64('filter=general.name=="jdoe-mbp"') # remove argument to get all computers 
computers_mgmt_id = get_mgmt_id(computers_id)

for computer in computers_mgmt_id:
    
    computer_name = computer['name']
    computer_mgmt_id = computer['mgmt_id']
    recovery_lock_key = randint(1000000000,9999999999) # random int to be used as key
    
    set_key(computer_name, computer_mgmt_id, recovery_lock_key)