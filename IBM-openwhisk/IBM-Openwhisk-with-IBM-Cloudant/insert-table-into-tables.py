from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from datetime import datetime
import  concurrent.futures
import asyncio

client=Cloudant("e8425b33-b22d-46b2-810d-99ddd319e9b9-bluemix","52743ce84f5e992bf1682440998c43138b44873bda027b138b6f7cd714c10cef",url="https://e8425b33-b22d-46b2-810d-99ddd319e9b9-bluemix:52743ce84f5e992bf1682440998c43138b44873bda027b138b6f7cd714c10cef@e8425b33-b22d-46b2-810d-99ddd319e9b9-bluemix.cloudant.com")
client.connect();
databaseName = "names"


print(client.all_dbs());
print(type(client.all_dbs()));

#'_id': 'julia30'+str(i), # Setting _id is optional

if databaseName in client.all_dbs():
    my_database=client[databaseName]
else:
    my_database=client.create_database(databaseName)


# for i in range(0,100):
#     data = {
#    '_id':'id'+str(i),
#     'name': 'XXXX'+str(i),
#     'lastname': 'YYYY'+str(i),
#     'date': str(datetime.now())
#     }
#     # Create a document using the Database API
#     my_document = my_database.create_document(data)
#     # if my_document.exists():
#     #     print ('SUCCESS!!')


async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            loop1 = asyncio.get_event_loop()
            for i in range(0,5000):
                data = {
                        '_id':'id'+str(i),
                        'name': 'XXXX'+str(i),
                        'lastname': 'YYYY'+str(i),
                         'date': str(datetime.now())
                        }

                loop1.run_in_executor(executor,my_database.create_document,data)

loop = asyncio.get_event_loop()
date1= datetime.now()
#print(date)
loop.run_until_complete(main())
date2= datetime.now()
print(date2-date1)
