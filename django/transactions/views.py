from django.shortcuts import render
from solders.pubkey import Pubkey
from solana.rpc.async_api import AsyncClient
import asyncio

def index(request):
    return render(request, 'index.html')

async def fetch_transactions():
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    public_key = "MoonCVVNZFSYkqNXP6bxHLPL6QQJiMagDL3qcqUQTrG"
    public_key_obj = Pubkey.from_string(public_key)
    
    limit = 10
    transactions_resp = client.get_signatures_for_address(public_key_obj, limit=limit)
    transactions = transactions_resp

    
    await client.close()
    return transactions

def get_transactions(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    transactions = loop.run_until_complete(fetch_transactions())
    
    return render(request, 'transactions.html', {'transactions': transactions})
