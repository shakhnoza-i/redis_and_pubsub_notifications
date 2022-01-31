import redis
import requests
import json

from datetime import timedelta


API_HOST = "https://api.coingecko.com/api/v3"  # www.api.coingecko.com/api/v3"

coin_to_notification_prices = {
    "bitcoin": 35000,
    'ethereum': 2200,
}

coin_ids = ["bitcoin", "ethereum"]
coins_query_string = ','.join(coin_ids)

coin_data = {coin_id: {} for coin_id in coin_ids}
coin_json_response = requests.get(
    f"{API_HOST}/coins/markets?vs_currency=usd&ids={coins_query_string}").json()


for coin in coin_json_response:
    to_parse_coin_id = coin["id"]
    coin_data[to_parse_coin_id]["symbol"] = coin["symbol"]
    coin_data[to_parse_coin_id]["name"] = coin["name"]
    coin_data[to_parse_coin_id]["current_price"] = coin["current_price"]
    coin_data[to_parse_coin_id]["high_24h"] = coin["high_24h"]
    coin_data[to_parse_coin_id]["low_24h"] = coin["low_24h"]
    coin_data[to_parse_coin_id]["price_change_percentage_24h"] = coin["price_change_percentage_24h"]


r = redis.Redis(host="127.0.0.1", port=6379)

for coin_id, coin_details in coin_data.items():
    r.set(f"{coin_id}|last_known_price", coin_details["current_price"])

    if not r.get(f"{coin_id}|price_5_minutes_ago"):
        r.setex(
            f"{coin_id}|price_5_minutes_ago",
            timedelta(minutes=5),
            coin_details['current_price']
        )

    if not r.get(f"{coin_id}|lowest_24h"):
        r.setex(
            f"{coin_id}|lowest_24h",
            timedelta(hours=24),
            coin_details['current_price']
        )

for coin in coin_ids:
    print(coin)
    last_scraped_price = float(r.get)
