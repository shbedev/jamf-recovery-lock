# jamf-recovery-lock
Python script to set recovery lock key for Apple Silicon computers.

How to use?
1. Clone this repo: `git clone https://github.com/shbedev/jamf-recovery-lock.git`
2. Edit `auth/creds.py` and fill the required info
3. View `general.py` and update if needed
4. Test the script by editing `main.py` and filtering for 1 computer, before running this on all computers
5. Open command line and run `python3 main.py`

The recovery key will now be showen under *Jamf Pro > Computer > Inventory > Security > Recovery Lock Password* (Show Password)

👉 Note that the Recovery Lock status will be showen as *Not Eanbled* until the next inventory collection.
