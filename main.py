import time
import requests

# How often are the invitations checked? In seconds. Defaults to 30.
interval = 30

def main(username: str, token: str, verbose: bool) -> None:

  # Check that the token is valid
  try:
    auth = requests.get('https://api.github.com/user/repository_invitations', auth=(username,token))
    if (isinstance(auth.json(), dict) and auth.json()["message"] == "Requires authentication"):
      exit("Invalid token or username!")
  except Exception as e:
    print(e)
    exit("Authentication to Github failed!")

  while True:
    #print("Checking for invitations...")
    try:
      invitations = requests.get('https://api.github.com/user/repository_invitations', auth=(username,token))
      #print(invitations.json())
      for invitation in invitations.json():
        try:
          id = invitation["id"]
          requests.patch(f'https://api.github.com/user/repository_invitations/{id}', auth=(username,token))
          if verbose: print(f"Accepted invitation to repository {invitation['repository']['full_name']} ({id})")
        except Exception as e:
          print("Problem accepting invitation:")
          print(e)
    except Exception as e:
      print("Error:")
      print(e)
    #print(f"Sleeping {interval} seconds...")
    time.sleep(interval)

import json
import os
import re

# Open the settings file, remove all comments from it
if not os.path.exists("settings.json"):
  exit("settings.json not found. Please create the file first.")
with open("settings.json", 'r') as handle:
  fixed_json = ''.join(line for line in handle if not re.match(r'^\s*//.*', line))
settings = json.loads(fixed_json)

# Verify settings.json
if ("token" not in settings or settings["token"] == ""):
  exit("Please set your token in settings.json before running the script.")
if ("username" not in settings or settings["username"] == ""):
  exit("Please set your username in settings.json before running the script.")
if ("verbose" not in settings or settings["verbose"] == ""):
  exit("Please set the verbose parameter in settings.json before running the script.")

if __name__ == "__main__":
  print("This script will run forever and will accept all invitations to repositories that you receive.")
  main(settings["username"], settings["token"], settings["verbose"])