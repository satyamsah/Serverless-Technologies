import asyncio
import requests
import json
import concurrent.futures
from datetime import datetime

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        loop1 = asyncio.get_event_loop()
        res=[]

        data = {"operation":"create","tableName":"LambdaTable","payload":{"Item":{"Id":"google-","name":"mountain view-"}}}
        url="https://80u64utx9j.execute-api.us-east-2.amazonaws.com/prod/DynamoDBManage"
        res.append(
        loop1.run_in_executor(executor,
                                 requests.post,
                                 url,
                                 json.dumps(data)
                                )
        )

        for response in await asyncio.gather(*res):
            print(response)

loop = asyncio.get_event_loop()
date1= datetime.now()
#print(date)
loop.run_until_complete(main())
date2= datetime.now()
print("time diff",date2-date1)
#print(date)



