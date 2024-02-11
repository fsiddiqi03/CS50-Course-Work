import requests
import json
import sys

if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])

    except:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)



try:
    bitcoin_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = bitcoin_price.json()
    bitcoin = x["bpi"]["USD"]["rate_float"]
    amount = float(bitcoin) * float(amount)
    print(f"${amount:,.4f}")




except requests.RequestException:
    print("RequestException")





