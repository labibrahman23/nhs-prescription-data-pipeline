import requests
import json

#Number of records, extracted from API
DATA_LIMIT = 5000

def download_data():

    """This downloads NHS Prescription Data from NHS OPEN API,
    This is saved locally as a JSON file,
    DATA_LIMIT gives the number of records extracted,
    Exception handling is used to catch specific API errors.

    """

    url = f"https://opendata.nhsbsa.net/api/3/action/datastore_search?resource_id=EPD_SNOMED_202604&limit={DATA_LIMIT}"

    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        data = response.json()
            
        with open("data/raw/epd1.json", "w") as json_file:
            json.dump(data, json_file, indent = 4)
            print("Succesfully saved the data to file")
                
            
    except requests.exceptions.ConnectionError as e:
        raise(f"There was a Connection error: {e}")

    except requests.exceptions.Timeout:
        print("Data took too long to load")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error, code: {e} ")

    except requests.exceptions.RequestException as e:
        print(f"Fail, Exception: {e}")


