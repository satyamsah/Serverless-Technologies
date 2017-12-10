from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

import concurrent.futures
from datetime import datetime
import asyncio

block_blob_service = BlockBlobService(account_name='function123467acdd', account_key='UIk1s/ZaWXZtlmcCFAzqz0puPPp26iZ4lLTCKbCK3XXFl+X4U/xew6iRl2wwPkwTDU8aC0Q4utQ+MPM5O1wNww==')
#block_blob_service.create_container('mycontainer')

# for i in  range(5):
#     block_blob_service.create_blob_from_path(
#         'mycontainer',
#         'myblockblob'+str(i),
#         'ELK.PNG',
#         content_settings=ContentSettings(content_type='image/png')
#            )
async def main():
    loop1=asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for i in range(3000):
            loop1.run_in_executor(executor, block_blob_service.create_blob_from_path,'mycontainer','myblockblob'+str(i), 'ELK.PNG')


date1= datetime.now()
loop=asyncio.get_event_loop().run_until_complete(main())
date2= datetime.now()
print("time diff",date2-date1)

