# py
import json
import boto3
from botocore.vendored import requests
from alib import IPPULL
#api=IPPULL()
#api.foo('instance call')
###Calls call
IPPULL.cfoo()

obj = IPPULL('ipinfo.io')
t = IPPULL.changeColor
t(obj)
print (obj)
##response = requests.get("http://ipinfo.io").json()
response = requests.get(obj).json()
print (response)
#myhostip = response['ip']
#print (myhostip)
