import requests

activity_id = "123456789"  # Replace with your activity ID
access_token = "your_access_token"

url = f"https://www.strava.com/api/v3/activities/{activity_id}/export_gpx"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open("activity.gpx", "wb") as f:
        f.write(response.content)
    print("GPX file downloaded.")
else:
    print(f"Failed to download GPX: {response.status_code} - {response.text}")
