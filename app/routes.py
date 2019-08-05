from app import app
from flask import request

import kin
import asyncio

MASTER_PUBLIC_KEY = 'GAUR7M7GKXZ6UZLGOZ2ZC7SSRLL4YLRRNLJ2UAJLRYYFLYJCI7ELD3MB'
MASTER_SEED = 'SCMWVESSHCT63VPRV4DR424FZDYUHVV76JGVLYJJNMDZ6C3GIARO6ZGR'
BOUNTY = 10


WIDTH = 4
HEIGHT = 4
games = []

async def isAccountExists(address):
    async with kin.KinClient(kin.TEST_ENVIRONMENT) as client:
        try:
            exists = await client.does_account_exists(address)
        except:
            exists = False
        return exists

async def createAccount(address):
    async with kin.KinClient(kin.TEST_ENVIRONMENT) as client:
        masterAccount = client.kin_account(MASTER_SEED)
        txHash = await masterAccount.create_account(address,1000,100)
        return txHash

loop = asyncio.get_event_loop()

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/login')
def login():
    # keypair = kin.Keypair()
    publicKey = request.args.get('public_key')
    # publicKey = keypair.public_address
    exists = loop.run_until_complete(isAccountExists(publicKey))
    if exists:
        print("account already exists")
    if not exists:
        print("creating account")
        txHash = loop.run_until_complete(createAccount(publicKey))
        print(txHash)

    return MASTER_PUBLIC_KEY
