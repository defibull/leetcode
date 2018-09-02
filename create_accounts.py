import requests
import json
import random
def id_list():
    r = requests.get("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b")
    customers = json.loads(r.text)
    customer_ids = [customer['_id'] for customer in customers]
    return customer_ids

def nickname(cust_id):
    url = "".join(["http://api.reimaginebanking.com/customers/",cust_id,"?key=0328041e3591473db2c6d492ba8aff2b"])
    r = requests.get(url)
    customer = json.loads(r.text)
    return "".join([customer["first_name"],customer["last_name"]])

def balance():
    return random.randrange(2500, 500000)

def create_account(account_num, cust_id):
    payload = {
    "type": "Credit Card",
    "nickname": nickname(cust_id),
    "rewards": 0,
    "balance": balance(),
    "account_number": str(account_num)
    }
    headers = {"Content-Type": "application/json","Accept": "application/json"}
    url = "".join(["http://api.reimaginebanking.com/customers/", cust_id,"/accounts?key=0328041e3591473db2c6d492ba8aff2b"])

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.text)
#http://api.reimaginebanking.com/customers/5883b7c21756fc834d8eba8e/accounts?key=0328041e3591473db2c6d492ba8aff2b



def open_accounts(id_list):
    count = 5000000000000001
    for cust_id in id_list:
        create_account(count,cust_id)
        count+=1


ids = id_list()
open_accounts(ids)
