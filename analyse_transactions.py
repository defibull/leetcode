import requests
import json
import random
import time
from decimal import Decimal
import pyrebase

class Customer(object):
    def __init__(self,name,email,password,id,zip): # balance
        self.name = name
        self.email = email
        self.password = password
        self.id = id
        self.streak = random.randrange(0,7)
        self.zip = zip
config = {
    "apiKey": "AIzaSyC6GK4lbZeM-MmtdGsLF3m5GLCWsTmOtBA",
    "authDomain": "deaddict-8321f.firebaseapp.com",
    "databaseURL" : "https://deaddict-8321f.firebaseio.com",
    "storageBucket" : "deaddict-8321f.appspot.com",
    # messagingSenderId: "585605368899"
}

firebase_app = pyrebase.initialize_app(config)
firebase = firebase_app.database()



def check_balances():
    r = requests.get("http://api.reimaginebanking.com/accounts?key=0328041e3591473db2c6d492ba8aff2b")
    accounts = json.loads(r.text)
    low_balance = []
    for account in accounts:
        if int(account['balance']) < 5000:
            print account['balance']
            low_balance.append([account['_id'], account['customer_id']])
    return low_balance
def check_transactions(low_balance):
    suspision = []
    for ac in low_balance:
        url = "".join(["http://api.reimaginebanking.com/accounts/", ac[0],"/purchases?key=0328041e3591473db2c6d492ba8aff2b"])
        r = requests.get(url)
        transactions = json.loads(r.text)
        for transaction in transactions:
            if transaction['amount'] > 1000:
                suspision.append(ac[1])
                break
    return suspision

def add_to_firebase(susp_people):
    formatted_customer_list = []
    for id in susp_people:
        url = "".join(["http://api.reimaginebanking.com/customers/", id, "?key=0328041e3591473db2c6d492ba8aff2b"])
        r = requests.get(url)
        customer = json.loads(r.text)
        name = " ".join([customer['first_name'], customer['last_name']])
        email = "".join([customer['first_name'], customer['last_name'], "@addicted2u.com"])
        current_cust = Customer(name, email, "123", customer['_id'], customer['address']['zip'])
        formatted_customer_list.append(current_cust)
    return formatted_customer_list

less_than_5k = check_balances()
print len(less_than_5k)
susp_people = check_transactions(less_than_5k)
print susp_people
customer_list = add_to_firebase(susp_people)

for customer in customer_list:
    data = {"email": customer.email,
            "password": customer.password,
            "customer_number": customer.id,
            "zip" : customer.zip,
            "streak" : customer.streak,
            }
    res = firebase.child("suspicious").child(customer.name).set(data)

    print res
