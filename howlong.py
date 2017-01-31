import sys
import json
import requests

req_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={}&destinations={}"

try:
    r = requests.get(req_url.format(str(sys.argv[1].replace(" ", "+")), str(sys.argv[2].replace(" ", "+"))))
    data = json.loads(r.text)
    if data["status"] == "OK":
        if data["rows"][0]["elements"][0]["status"] != "NOT_FOUND":
            print(data["rows"][0]["elements"][0]["distance"]["text"])
            print(data["rows"][0]["elements"][0]["duration"]["text"])
        else:
            print("Distance data not found")
    else:
        print("There is some error with the request")
except:
    print("Program exited with error", sys.exc_info()[0])
