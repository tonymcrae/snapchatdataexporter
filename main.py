import json
import os
import requests
from pathlib import Path
from parsejson import load_json

### Config ###
JSON_PATH = Path("memories_history.json")
ITEMS_KEY = "Saved Media"
DOWNLOAD_FOLDER = Path("downloads")
MEDIA_URL_KEY = "Media Download Url"
TIMESTAMP_KEY = "Date"
MEDIA_TYPE_KEY = "Media Type"

def download_media(item, index):
    media_url = item.get(MEDIA_URL_KEY)
    timestamp = item.get(TIMESTAMP_KEY)
    media_type = item.get(MEDIA_TYPE_KEY)
    safe_timestamp = timestamp.replace(":", "-").replace(" ", "_")
    
    if media_type == "Image":
        type = "image"
        ext = ".jpg"
    elif media_type == "Video":
        type = "video"
        ext = ".mp4"
    else:
        type = "fixme"
        ext = ".fixme"

    filename = f"{safe_timestamp}_{type}_{index}{ext}"
    output_path = DOWNLOAD_FOLDER / filename

    print(f"Downloading media from to {output_path}")
    response = requests.get(media_url)
    print("HTTP status:", response.status_code)
    output_path.write_bytes(response.content)

def main():
    items = load_json(JSON_PATH, ITEMS_KEY)
    index = 1
    for item in items:
        ok = download_media(item, index)
        index += 1
main()