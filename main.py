import requests
import concurrent.futures
import time
def get_coin_to_usd_pairs():

    pairs = []
    url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(url)

    for pair in response.json()["symbols"]:
        if "USD" == pair["symbol"][-3:]:
            pairs.append(pair["symbol"])

    return pairs
def get_price(symbol):

    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + symbol
    response = requests.get(url)
    print(response.json())


if __name__ == '__main__':
    coin_to_usd_pairs = []
    if not coin_to_usd_pairs:
        coin_to_usd_pairs = get_coin_to_usd_pairs()
        print(coin_to_usd_pairs)

        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(get_price, coin_to_usd_pairs)

        duration = time.time() - start_time
        print(f"Acquired {len(coin_to_usd_pairs)} in {duration} seconds")
