import requests
import pandas as pd
from datetime import datetime
import os



""" official_id, message, (link is optional - research about payload """
""" Take that in, merge on playerID, send notification """


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


# 1. Read in file
print("Input file format is [official_id, message, link (optional)], do not have commas in message as this will cause errors)")
file_name = input("Name of csv: ")
input_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Input")
file_path = os.path.join(input_folder, file_name)

# Try catch block to handle any errors which could happen during automation
try:
    notification_df = pd.read_csv(file_path)
    print("Input File read successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{file_path}' contains parsing errors.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# 2. Merge on playerIDS
cache_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Cache")
file_path = os.path.join(cache_folder, "PlayerID_cache.csv")
print(file_path)

# Try catch block to handle any errors which could happen during automation
try:
    playerID_df = pd.read_csv(file_path)
    print("Player ID File read successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{file_path}' contains parsing errors.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

merged_df = pd.merge(notification_df, playerID_df, on="official_id", how="inner")
print(merged_df)
print(merged_df.columns)


# 3. Send message
""" 
count = 0

for index, row in notification_info.iterrows():
    notification_info["link"] = notification_info["link"].fillna("")
    if notification_info["link"].eq(""):
        payload = {
            "app_id": APP_ID,
            "contents": {"en": row["message"]},
            "include_player_ids": [row["data"]]
        }
    else:
        payload = {
            "app_id": APP_ID,
            "contents": {"en": row["message"]},
            "include_player_ids": [row["data"]]
            "url": row["link]
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

"""
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Now at:", os.getcwd())

#output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Output")

output_folder = "Output"

# Check and create if missing
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created folder: {output_folder}")
else:
    print(f"Folder already exists: {output_folder}")


print("Sending to output file...")
output_path = os.path.join(output_folder, f"{file_name}-output.csv")
notification_df.to_csv(output_path, index=False)

print(f"✅ File saved at: {output_path}")




""" 

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

print(f"Column logged to {file_output}")"""