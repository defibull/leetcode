import time
import random
import requests,json
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
# result = firebase.get('/users', None)
# print result

def getCustomerID():
    r = requests.get("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b")
    customers = json.loads(r.text)
    formatted_customer_list = []
    for customer in customers:
        name = " ".join([customer['first_name'], customer['last_name']])
        email = "".join([customer['first_name'], customer['last_name'], "@addicted2u.com"])
        current_cust = Customer(name, email, "123", customer['_id'], customer['address']['zip'])
        formatted_customer_list.append(current_cust)

    # id_list = [Customer(),customer['id'], for customer in customers] # customer['_id']
    return formatted_customer_list

customer_list = getCustomerID()

for customer in customer_list:
    data = {"email": customer.email,
            "password": customer.password,
            "customer_number": customer.id,
            "zip" : customer.zip,
            "streak" : customer.streak,
            }
    res = firebase.child("users").child(customer.name).set(data)

    print res




# def update_health():
#     for item in id_list:
#         heart_rate = random.randrange(60,100)
#         pass
#
# print ids
#
# #infinite loop
#
# # while True:
# #     time.sleep(5)
