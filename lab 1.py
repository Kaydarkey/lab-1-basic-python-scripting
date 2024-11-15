# Step 1: Import Required Modules
import requests
import os
import shutil
from datetime import datetime

# Step 2: Clean Up Previous Directory
dir_name = 'sylvester_darkey'
if os.path.exists(dir_name):
    try:
        shutil.rmtree(dir_name)
        print(f"Directory '{dir_name}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Step 3: Create a New Directory
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created.")

# Step 4: Define the Local File Path
local_file_path = os.path.join(dir_name, "sylvester_darkey.txt")

# Step 5: Download the File
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

if response.status_code == 200:
    print("File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
        print("File saved successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# Step 6: Overwrite File Content
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified.")

# Step 7: Display the Updated File Content
with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end=' ')
    print(file.read())
