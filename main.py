import urllib.request, json
from dotenv import load_dotenv
import os


def main():
    # Load environment variables
    load_dotenv()
    API_KEY = os.getenv("NPS_API_KEY")
    # Configure API request
    endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=fl"
    HEADERS = {"X-Api-Key": API_KEY}
    req = urllib.request.Request(endpoint, headers=HEADERS)
    # Make API request
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())

    # write to file
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
