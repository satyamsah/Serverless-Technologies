import subprocess
import requests
import urllib2
import json
# url = 'https://function123467.azurewebsites.net/api/HttpTriggerJS1?code=k8fl2keEAaoe5tC9H7jj2KZMh5ikJiFLVs3AY3ESM4sl9/xF/hbC9A=='

# headers={'content-type': 'application/json'}
resposelist=[]
data = { 'fsize' : '102400' }
req = urllib2.Request('https://function123467.azurewebsites.net/api/HttpTriggerPython31?code=qFP4dbU2Oti0q67OkuGAMUcpdpG9YYPQa2cDpLvZMn8Xs/LrIVBcTw==')
req.add_header('Content-Type', 'application/json')
for i in range(100):
    response = urllib2.urlopen(req, json.dumps(data))# each response was an list
    resposelist.append(response)


download_dir = "output100MB-py-azure.csv"
csv = open(download_dir, "w")
columnTitleRow="fsize,func_elapsed,fwrite_elapsed,provider,lang\n"
csv.write(columnTitleRow)
for singleresponse in resposelist:
    for resp in singleresponse:
        csv.write(resp.strip('"'))
        csv.write(",azure")
        csv.write(",python")
        csv.write("\n")
