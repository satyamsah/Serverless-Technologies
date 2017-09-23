from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from datetime import datetime

client=Cloudant("<username>","<password>",url="<http://username-bluemix.cloudant.com>")
client.connect();
databaseName = "names"


print(client.all_dbs());
print(type(client.all_dbs()));

#'_id': 'julia30'+str(i), # Setting _id is optional

if databaseName in client.all_dbs():
    my_database=client[databaseName]
else:
    my_database=client.create_database(databaseName)


for i in range(1,10):
    my_document = my_database['id'+str(i)]
    my_document.delete()

