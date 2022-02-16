import requests

import json



james = open("Guest.txt", "r")

soloisnotcool = james.readlines()



yourkey = input("Please enter your key")
for x in soloisnotcool:
    response = requests.get("https://api.weleakinfo.to/api?value=" + x + "&type=email&key=" + yourkey)

    print(response.json())
