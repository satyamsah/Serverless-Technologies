import pydocumentdb.document_client as document_client
client=document_client.DocumentClient("https://abhi8888.documents.azure.com:443/", {'masterKey': "YCcmmm5EbNxn3VS93OHZ38DUN25qboZYaA4t05ftzPRDrWIvySrAnqQNN61hnhtBIETEQt1rh0n7ew2Y0rUEvw=="})
try:
    db = next((data for data in client.ReadDatabases() if data['id'] == "Tasks"))

except:
    pass




# # Create database
# db = client.CreateDatabase({ 'id': "Tasks" })

# Create collection
collection = client.CreateCollection(db['_self'],{ 'id': "Items" })

for i in range(5):
    # Create document
    document = client.CreateDocument(collection['_self'],
                                     { 'id': "task"+str(i),
                                       'Web Site': 0,
                                       'Cloud Service': 0,
                                       'Virtual Machine': 0,
                                       'name': "task"+str(i)
                                       })
