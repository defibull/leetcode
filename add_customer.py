import requests
import random
import json
def name_generator():
    color = ["Red","Blue","Black","White","Ried","Bliuie","Blgacjk","Wahite"]
    tool = ["Hammer","Drill","Cutter","Knife","Hammser","Darill","Cuftter","Kanife"]
    randomNumber1 = random.randrange(0,len(color))
    randomNumber2 = random.randrange(0,len(tool))
    name = color[randomNumber1] + " " + tool[randomNumber2]
    return name

def random_street():
    return str(random.randrange(0,1900))


def random_zip():
    zip_codes = [10065, 10075, 10022, 10056]
    return str(zip_codes[random.randrange(0,len(zip_codes))])

def create_customer():
    name = name_generator().split(" ")
    payload = {"first_name": name[0],
    "last_name": name[1],
    "address": {
        "street_number": random_street(),
        "street_name": "3rd Avenue",
        "city": "New York",
        "state": "NY",
        "zip": random_zip()
        }
    }
    headers = {"Content-Type": "application/json","Accept": "application/json"}
    print payload
    r = requests.post("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b", data=json.dumps(payload), headers=headers)
    print(r.text)

for i in range(1000):
    create_customer()
