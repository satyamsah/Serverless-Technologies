# import subprocess
# import requests
# import urllib2
# import json
# import boto3
#
# # url = 'https://function123467.azurewebsites.net/api/HttpTriggerJS1?code=k8fl2keEAaoe5tC9H7jj2KZMh5ikJiFLVs3AY3ESM4sl9/xF/hbC9A=='
#
# # headers={'content-type': 'application/json'}
#
# client = boto3.client(
#     'lambda', aws_access_key_id='AKIAJNMAG2GT3LFOINUQ',
#     aws_secret_access_key='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')
#
#     # Hard coded strings as credentials, not recommended.
#
# resposelist=[]
# data = {"httpMethod": "POST","queryStringParameters": {"TableName": "MyTable"}}
# req = urllib2.Request('https://qz1skemd1d.execute-api.us-east-2.amazonaws.com/prod/languagecomparison')
# req.add_header('Content-Type', 'application/json')
# for i in range(10):
#     response = urllib2.urlopen(req, json.dumps(data))
#     resposelist.append(response)
#
#
# download_dir = "output100MB.csv"
# csv = open(download_dir, "w")
# columnTitleRow="functionexecutontime, writexecutiontime,language\n"
# csv.write(columnTitleRow)
# for singleresponse in resposelist:
#     for resp in singleresponse:
#         csv.write(resp.strip('"'))
#         csv.write("\n")

import os
import sys
import time
import json
import botocore.session
from multiprocessing.pool import ThreadPool

region = "us-east-2"
itype = "RequestResponse" #"Event"
s = botocore.session.get_session()
c = s.create_client('lambda', region_name=region)

# res = c.invoke(FunctionName='testfunctionlanguagespeedcompariosn', Payload='{ "fsize" : "1"}',InvocationType=itype)
# end = time.time()
# print(res['Payload'].read().decode("utf-8"))



responselist=[]
data = '{"fsize" : "102400"}'
for i in range(100):
    res = c.invoke(FunctionName='testfunctionlanguagespeedcompariosn', Payload=data,InvocationType=itype)
    responselist.append(res['Payload'].read().decode("utf-8"))

download_dir = "output100MB-aws-py.csv"
csv = open(download_dir, "w")
columnTitleRow="fsize,func_elapsed,fwrite_elapsed,provider,lang\n"
csv.write(columnTitleRow)
for singleresponse in responselist:
    csv.write(singleresponse.strip('"'))
    csv.write(",aws")
    csv.write(",python")
    csv.write("\n")
