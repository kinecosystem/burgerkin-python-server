from app import app
from kin import KinClient, TEST_ENVIRONMENT
import asyncio

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/login')
async def login():
    async with KinClient(TEST_ENVIRONMENT) as client:
        exists = await client.does_account_exists("dfdfdsfdsfsd")
    if exists:
        return "exists"
    else:
        return "doesnt exist"
