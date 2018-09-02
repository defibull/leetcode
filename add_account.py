import requests
import random
import json

def nickname():
    r = requests.get("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b")
    customers = json.loads(r.text)
    nickname_list = [customer['first_name'][0] + customer['last_name'] for customer in customers]
    return nickname_list

def balance():
    return random.randrange(2500, 500000)
    
def random_accountNo():
    return str(random.randrange(5000000000000000, 5999999999999999))
    

def getCustomerID():
    r = requests.get("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b")
    customers = json.loads(r.text)
    id_list = [customer['_id'] for customer in customers]
    return id_list
     
def create_account():
    payload = {
    "type": "Credit Card",
    "nickname": nickname(), 
    "rewards": 0,
    "balance": banlance(),
    "account_number": random_accountNo()
    }
    headers = {"Content-Type": "application/json","Accept": "application/json"}
    print payload
    r = requests.post("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b", data=json.dumps(payload), headers=headers)
    print(r.text)


for i in range(1000):
    create_account()
