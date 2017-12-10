from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
block_blob_service = BlockBlobService(account_name='function123467acdd', account_key='UIk1s/ZaWXZtlmcCFAzqz0puPPp26iZ4lLTCKbCK3XXFl+X4U/xew6iRl2wwPkwTDU8aC0Q4utQ+MPM5O1wNww==')
#block_blob_service.create_container('mycontainer')

for i in  range(3000):
    block_blob_service.delete_blob('mycontainer', 'myblockblob'+str(i))
