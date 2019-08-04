from app import app
import kin
import asyncio

async def isAccountExists(address):
    async with kin.KinClient(kin.TEST_ENVIRONMENT) as client:
        try:
            exists = await client.does_account_exists(address)
        except:
            exists = False
        return exists

async def createAccount(address):
    async with kin.KinClient(kin.TEST_ENVIRONMENT) as client:
        account = await client.friendbot(address)
        return account


loop = asyncio.get_event_loop()

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/login')
def login():
    keypair = kin.Keypair(seed="hello")
    #publicKey = request.args.get('public_key')
    #publicKey = "GDESKVL37Y26EV7YQGTKCB56ZTHAXLLDPYUCSQJSKKHIIQ5SWFZKKUSH"
    #publicKey = "GDESKVL37Y26EV7YQGTKCB56ZTHAXLLDPYUCSQJSKKHIIQ5SWFZKKUSJ"
    publicKey = keypair.public_address
    exists = loop.run_until_complete(isAccountExists(publicKey))
    if not exists:
        account = loop.run_until_complete(createAccount(publicKey))
        print(account)

    return "OK"
