import requests
import json
def id_list():
    r = requests.get("http://api.reimaginebanking.com/customers?key=0328041e3591473db2c6d492ba8aff2b")
    customers = json.loads(r.text)
    print customers
    customer_list = [customers for customer in customers]
    # return customer_list

def account_list(id_list):
    pass


# def transaction_differences(account):
#     for each account:
#         go through all
#
# # ids = id_list()
# accounts = account_list(ids)
id_list()
