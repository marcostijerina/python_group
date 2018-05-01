#marc7879
import boto3
import json
from botocore.vendored import requests
#import request
#def lambda_handler(event, context):
response = requests.get("https://dog.ceo/api/breeds/image/random").json()
pic_url = response['message']
print (pic_url)
jsonresponse = json.dumps(pic_url)
print (jsonresponse)
print (response)
