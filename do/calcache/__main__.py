import os

import requests
from filecache import filecache

@filecache(15 * 60)
def main():
  ICAL_URL = os.environ['ICAL_URL']
  resp = requests.get(ICAL_URL)
  return {
    "headers": {
      "Content-Type": "text/calendar"
    },
    "statusCode": 200,
    "body": resp.text
  }
