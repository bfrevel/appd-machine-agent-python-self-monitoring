import configparser
import asyncio
import aiohttp
import apis.account
import apis.application

parser = configparser.ConfigParser()
parser.read("config.ini")
config = parser['DEFAULT']

accountApi = apis.account.AccountApi(config)
applicationApi = apis.application.ApplicationApi(config)

async def load_applications_information():
    async with aiohttp.ClientSession(headers = {'Content-Type': "application/vnd.appd.cntrl+protobuf;v=1"}) as session:
        oauth_token = await asyncio.ensure_future(accountApi.access_token(session))

    async with aiohttp.ClientSession(headers = {'Authorization': f"Bearer {oauth_token}"}) as session:
        applications = await asyncio.ensure_future(applicationApi.applications(session))
        application_tasks = []
        for application in applications:
            application_tasks.append(asyncio.ensure_future(applicationApi.business_transactions(session, application)))
            application_tasks.append(asyncio.ensure_future(applicationApi.tiers(session, application)))
        await asyncio.gather(*application_tasks)


asyncio.run(load_applications_information())
