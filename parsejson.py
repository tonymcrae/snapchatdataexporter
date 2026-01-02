import json
import os
import requests
from pathlib import Path

### Config ###
JSON_PATH = Path("memories_history.json")
ITEMS_KEY = "Saved Media"
PARSE_LIMIT = 3
DOWNLOAD_FOLDER = Path("downloads")
MEDIA_URL_KEY = "Media Download Url"
TIMESTAMP_KEY = "Date"
MEDIA_TYPE_KEY = "Media Type"

def download_media(item, index):
    media_url = item.get(MEDIA_URL_KEY)
    timestamp = item.get(TIMESTAMP_KEY)
    media_type = item.get(MEDIA_TYPE_KEY)

    if media_type == "Image":
        ext = ".jpg"
    elif media_type == "Video":
        ext = ".mp4"
    else:
        ext = ".fixme"

    filename = f"{index}{ext}"
    output_path = DOWNLOAD_FOLDER / filename

    print(f"Downloading media from to {output_path}")
    response = requests.get(media_url)
    print("HTTP status:", response.status_code)
    output_path.write_bytes(response.content)



def main():
    DOWNLOAD_FOLDER.mkdir(exist_ok=True)
    file = JSON_PATH.open("r", encoding="utf-8")
    data = json.load(file)
    file.close()
    items = data[ITEMS_KEY]
    count = 0
    for item in items:
        download_media(item, count)
        count += 1
        if count >= PARSE_LIMIT:
            break
main()
