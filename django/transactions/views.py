from django.shortcuts import render
from solana.rpc.api import Client
from solders.pubkey import Pubkey

def index(request):
    return render(request, 'index.html')

def get_transactions(request):
    client = Client("https://api.mainnet-beta.solana.com")
    public_key = "MoonCVVNZFSYkqNXP6bxHLPL6QQJiMagDL3qcqUQTrG"
    public_key_obj = Pubkey.from_string(public_key)
    
    # Solana 계정의 최근 트랜잭션 기록 조회
    limit = 5
    transactions_resp = client.get_signatures_for_address(public_key_obj, limit=limit)
    transactions = transactions_resp.value  # 올바른 접근 방식 사용
    
    return render(request, 'transactions.html', {'transactions': transactions})
