# jamf-recovery-lock
Python script to set Recovery Lock key for Apple M1 computers.

### Prerequisites:
- Python3
- Python package: **requests** (can be installed by running `python3 -m pip install requests`)
- Username and password from *Jamf Pro (https://[company].jamfcloud.com) -> System Settings -> Jamf Pro User Accounts & Groups*

### How to use?
1. Clone this repo: `git clone https://github.com/shbedev/jamf-recovery-lock.git`
2. Edit [auth/creds.py](auth/creds.py) and fill the required info
3. Before running this on all computers, test the script by editing [main.py](main.py) and filtering for 1 computer (you can just change the name of the computer from "jdoe-mbp" to the computer name you are testing on).
4. Open command line and run `python3 main.py`

The recovery key will now be showen under *Jamf Pro > Computer > Inventory > Security > Recovery Lock Password* (Show Password)

👉 Note that the Recovery Lock status will be shown as *Not Enabled* until the next inventory collection.
