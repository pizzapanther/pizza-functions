import os

import requests
from filecache import filecache

@filecache(5 * 60)
def main():
  RELEASE_URL = os.environ['RELEASE_URL']
  resp = requests.get(RELEASE_URL)
  data = resp.json()
  print("retrieved new data")

  version = data["tag_name"].replace("v", "")
  url = data["assets"][0]["browser_download_url"]

  return {
    "body": {
      "version": version,
      "url": url
    }
  }
