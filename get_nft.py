from importlib import import_module
import requests
from halo import Halo
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()
API_KEY = os.getenv('API_KEY')

@Halo(text='Looking for all the NFTs in the collection, have a coffee till then', spinner='line')
def get_nft_collection(contract_address):
    cursor_val = None
    nft_data = []
    while True:
        headers = {
        'accept': 'application/json',
        'X-API-Key': API_KEY,
        }

        params = {
            'chain': 'eth',
            'format': 'decimal',
            'cursor': cursor_val,
        }

        try:
            response = requests.get(
                'https://deep-index.moralis.io/api/v2/nft/{}'.format(contract_address), 
                headers=headers, 
                params=params
            )
            data = response.json()
            if len(data['result']) <= 0:
                break
            else:
                for i in data['result']:
                    nft_data.append({
                        'id': i['token_id'],
                        'link': i['token_uri'],
                    })
                cursor_val = data['cursor']
        except:
            break
        sleep(1)
    print()
    print("The collection {} have been scanned & {} NFTs have been found and indexed".format(contract_address, len(nft_data)))
    return nft_data