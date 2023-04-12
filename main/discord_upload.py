import requests

def upload_to_discord(webhook_url, gif_file):
    files = {"file": open(gif_file, "rb")}
    response = requests.post(webhook_url, files=files)
    response.raise_for_status()