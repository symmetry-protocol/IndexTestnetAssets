
from pprint import pprint
from time import sleep
import json, requests

URL_TOP_COINS = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page={}&sparkline=false"
URL_SOLANA_COINS = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=solana-ecosystem&order=market_cap_desc&per_page=250&page={}&sparkline=false"


def get_top(n):
    """ gets list of top n coins by market cap """
    
    coins = []
    coin_count = 0
    page = 1
    while coin_count < n:
        data = json.loads(requests.get(URL_TOP_COINS.format(page)).text)
        for coin in data:
            coins.append({"gecko_id": coin['id'], 'symbol': coin['symbol'].upper()})
        page += 1
        coin_count += len(data)
        sleep(0.3)
    return coins[:n]

def get_solana():
    """ gets all solana ecosystem coins """
    coins = []
    page = 1
    while True:
        data = json.loads(requests.get(URL_SOLANA_COINS.format(page)).text)
        for coin in data:
            coins.append({"gecko_id": coin['id'], 'symbol': coin['symbol'].upper()})
        page += 1
        if len(data) == 0: break
        sleep(0.3)
    print('found {} solana coins'.format(len(coins)))
    return coins


def combine_with_assets(coins):
    """ combines the given coins to index_assets.json coins
        will ignore repeats and will give each new coin a uid """
    
    with open('index_assets.json', encoding='utf-8') as f:
    
        data = json.loads(f.read())
    
        for coin in coins:
            if coin['gecko_id'] not in [
                asset['gecko_id'] for asset in data['assets'].values()
            ]:
                data['highest_id'] += 1
                data['assets'][ data['highest_id'] ] = {
                    'gecko_id': coin['gecko_id'],
                    'symbol': coin['symbol']
                }

    with open('index_assets.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))
        print('wrote to file')

        

if __name__ == "__main__":
    count_top_coins = 250

    top_coins = get_top(count_top_coins)
    solana_coins = get_solana()

    all_coins = top_coins + solana_coins
    combine_with_assets(all_coins)

