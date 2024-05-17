import requests


def get_currency_data(currency):
    """Fetch currency data from the API."""
    url = f"http://www.floatrates.com/daily/{currency}.json"
    response = requests.get(url)
    return response.json()


def update_cache(cache, cached_items, currency):
    """Update the cache with new currency data if not already cached."""
    if currency not in cached_items:
        print(f"{currency} is not in the cache. Fetching new data...")
        cache[currency] = get_currency_data(currency)
        cached_items.append(currency)
    else:
        print(f"{currency} is already in the cache.")


def main():
    cache = {}
    cached_items = ["eur", "usd"]

    # Pre-fetching data for initial cached items
    for item in cached_items:
        cache[item] = get_currency_data(item)

    cur_owned = input("Which currency do you own?\n> ").lower()

    while True:
        cur_exchange = input("Which currency do you want to buy?\n> ").lower()
        if not cur_exchange or cur_exchange == "exit":
            print("Exiting program.")
            break

        try:
            sum_exchange = float(input("Enter amount:\n> "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

        update_cache(cache, cached_items, cur_exchange)

        try:
            received_amount = cache[cur_exchange][cur_owned]["inverseRate"] * sum_exchange
            print(f"You received {round(received_amount, 2)} {cur_exchange.upper()}.")
        except KeyError:
            print(f"Error: Currency data not available for {cur_exchange} or {cur_owned}.")


if __name__ == "__main__":
    main()