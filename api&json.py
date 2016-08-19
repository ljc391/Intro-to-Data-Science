import json
import requests
    if __name__==“__main__”:
        url = “”
        data = requests.get(url).text
        data = json.loads(data)
        print type(data)
        print data
