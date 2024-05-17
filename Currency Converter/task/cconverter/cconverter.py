import requests


def _save_to_cache(cache_pass, cached_items_pass, user_prompt_pass):
    print("Checking the cache...")
    if user_prompt_pass in cached_items_pass:
        print("Oh! It is in the cache!")
        pass
    else:
        print("Sorry, but it is not in the cache!")
        get_cache = requests.get(f"http://www.floatrates.com/daily/{user_prompt_pass}.json").json()
        cached_items_pass.append(user_prompt_pass)
        cache_pass[user_prompt_pass] = get_cache


cached_items = ["eur", "usd"]
cache = {}

for item in cached_items:
    get_cache_item = requests.get(f"http://www.floatrates.com/daily/{item}.json").json()
    cache[item] = get_cache_item

cur_owned = input()

while True:
    cur_exchange = input()
    if cur_exchange == "":
        exit()
    else:
        sum_exchange = float(input())
        _save_to_cache(cache, cached_items, cur_exchange.lower())
        print(f'You received {round(cache[cur_exchange][cur_owned]["inverseRate"] * sum_exchange, 2)} {cur_exchange}.')
