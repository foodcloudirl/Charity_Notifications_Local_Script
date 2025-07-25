import requests
import pandas as pd
from datetime import datetime

# Can have this work auto-matically by putting file with todays date in folder
# Have error handling if no file there

# OneSignal credentials
API_KEY = ""  
APP_ID = "a338bb1a-ad03-48ae-9f14-aa6582380430"   

url = "https://onesignal.com/api/v1/notifications"

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Basic {API_KEY}"
}

# change file path to todays date naming convention for auto-mation
file_path = "Irish_Food_Recall_msg.csv"

# Try catch block to handle any errors which could happen during automation
try:
    notification_info = pd.read_csv(file_path)
    print("File read successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{file_path}' contains parsing errors.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



# Notification details (ignore - used for tests)
#msg = "Your notification message here"  # Replace with the message you want to send
#player_id = "8d2519c1-c65b-44a3-8041-a5a86f4e5ff2"  # Replace with the player ID
count = 0

for index, row in notification_info.iterrows():
    payload = {
        "app_id": APP_ID,
        "contents": {"en": row["message"]},
        "include_player_ids": [row["data"]]
    }
    # Send POST request
    response = requests.post(url, json=payload, headers=headers)

    # Handle the response
    if response.status_code == 200:
        print("Notification sent successfully!")
        print(response.json())
        print("\n")
        count +=1
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")
        print(response.json())
        print("\n")

print("\n")
current_date = datetime.now().strftime("%Y-%m-%d")
file_output = "./logs/comms-" + str(current_date) + ".log"

print(file_output)
print(f"COUNT: {count}")
print(f"Len df {len(df)}")
print(f"% successfully sent: {len(count) / len(df)}")

# Write the column to the log file
with open(file_output, "w") as log_file:
    for value in notification_info["data"]:
        log_file.write(f"{value}\n")

print(f"Column logged to {file_output}")
