import boto3
from datetime import datetime
import  concurrent.futures
import asyncio
# Get the service resource.
dynamodb = boto3.resource('dynamodb')


# Create the DynamoDB table.
table = dynamodb.Table('dynamodbupdate')
print(table.creation_date_time);
async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        with table.batch_writer() as batch:
            loop1 = asyncio.get_event_loop()
            for i in range(0,10):
                Item={
                         'firstname': 'XXXX-'+str(i),
                         'lastname': 'YYYY-'+str(i),
                         'date_added': str(datetime.now()),
                    }

                loop1.run_in_executor(executor,batch.put_item,Item)


loop = asyncio.get_event_loop()
date1= datetime.now()
#print(date)
loop.run_until_complete(main())
date2= datetime.now()
print(date2-date1)
