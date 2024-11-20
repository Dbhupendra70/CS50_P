
import requests
import sys

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" )
    price=(response.json()["bpi"]["USD"]['rate_float'])
    amount=float(sys.argv[1])*price
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit()

