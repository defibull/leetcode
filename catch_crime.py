import requests
import json
import random
import time
from decimal import Decimal
import pyrebase
config = {
    "apiKey": "AIzaSyC6GK4lbZeM-MmtdGsLF3m5GLCWsTmOtBA",
    "authDomain": "deaddict-8321f.firebaseapp.com",
    "databaseURL" : "https://deaddict-8321f.firebaseio.com",
    "storageBucket" : "deaddict-8321f.appspot.com",
    # messagingSenderId: "585605368899"
}

firebase_app = pyrebase.initialize_app(config)
firebase = firebase_app.database()
users = firebase.child("users").get()
suspicious = firebase.child("suspicious").get()

criminals = list()

for user in users.each():
    for susp in suspicious.each():
        if user.key() == susp.key():
            heart_rates = user.val()['heartrate']
            for rate in heart_rates:
                if rate > 100 or rate < 60:
                    criminals.append([user.key(), heart_rates])
crime_list = list(criminals)

for criminal in crime_list:
    data = {"heart_rates": criminal[1]}
    res = firebase.child("criminals").child(criminal[0]).set(data)
    print res
