import requests
import json
import random
import time
from decimal import Decimal

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)




def ac_id_list():
    r = requests.get("http://api.reimaginebanking.com/accounts?key=0328041e3591473db2c6d492ba8aff2b")
    accounts = json.loads(r.text)
    account_ids = [account['_id'] for account in accounts]
    return account_ids

def populate_transactions(ids):
    count = 0
    for i in ids:
        for j in range(25):
            create_withdrawal(i)
            count+=1
        print count

def populate_addicts(ids):
    count = 0
    for j in range(5):
        for i, id in enumerate(ids):
            if i % 2 == 0:
                create_withdrawal(id)
                count+=1
        print count

def create_withdrawal(ac_id):
    reasons = ["personal", "cash", "druga", "shiv"]

    payload = {
    "merchant_id": "57cf75cea73e494d8675ec4e",
    "medium": "balance",
    "purchase_date": str(randomDate("2017-01-01", "2017-01-22", random.random())) ,
    "amount": (random.randrange(60000,100000,2)/3.0),
    "description": reasons[random.randrange(0,len(reasons))]
    }
    print payload["purchase_date"]
    headers = {"Content-Type": "application/json","Accept": "application/json"}
    url = "".join(["http://api.reimaginebanking.com/accounts/", ac_id,"/purchases?key=0328041e3591473db2c6d492ba8aff2b"])
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r.text


def analyse_transactions():
    pass

def create_suspicious_persons_list():
    pass

ac_ids = ac_id_list()
#populate_transactions(ac_ids)
populate_addicts(ac_ids)
