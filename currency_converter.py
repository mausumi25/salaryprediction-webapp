import requests

# Country -> Currency mapping
country_currency = {
    "India": "INR",
    "United States": "USD",
    "United Kingdom": "GBP",
    "Germany": "EUR",
    "France": "EUR",
    "Canada": "CAD",
    "Australia": "AUD",
    "Japan": "JPY",
    "China": "CNY",
    "Brazil": "BRL",
    "Pakistan": "PKR",
    "Bangladesh": "BDT",
    "Nepal": "NPR"
}

def convert_currency(amount, currency):
    """
    Convert USD amount to the selected currency.
    """
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        data = response.json()

        rate = data["rates"].get(currency, 1)

        return amount * rate

    except Exception:
        return amount