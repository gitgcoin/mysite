from solana.rpc.api import Client
from solana.publickey import PublicKey

def get_token_balance(wallet_address, token_mint_address, rpc_url='https://api.mainnet-beta.solana.com'):
    # Convert the wallet address to a Pubkey object
    wallet_pubkey = PublicKey(wallet_address)

    # Connect to the Solana RPC endpoint
    rpc_client = Client(rpc_url)

    # Get the token balance
    response = rpc_client.get_token_account_balance(wallet_pubkey)
    
    # Parse the token balance from the response
    if 'result' in response and 'value' in response['result']:
        token_balance = response['result']['value']
        return token_balance
    else:
        return 0

if __name__ == "__main__":
    # Replace these with your actual wallet and token addresses
    wallet_address = "8Awvg2nAoV22VP9RLLDvzo7iQTKryquSDvp5aeAT65zY"
    token_mint_address = "StepAscQoEioFxxWGnh2sLBDFp9d8rvKz2Yp39iDpyT"

    # Get the token balance
    balance = get_token_balance(wallet_address, token_mint_address)
    
    print(f'Token Balance for {wallet_address}: {balance} tokens')
