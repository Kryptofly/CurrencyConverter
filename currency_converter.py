import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_exchange_rates(base_currency):
    response = requests.get(API_URL + base_currency)
    if response.status_code != 200:
        raise Exception("Error fetching exchange rates.")
    return response.json()

def convert_currency(amount, base_currency, target_currency, rates):
    if target_currency not in rates:
        raise Exception(f"Currency {target_currency} not supported.")
    conversion_rate = rates[target_currency]
    return amount * conversion_rate

def main():
    base_currency = input("Enter the base currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    amount = float(input("Enter the amount to convert: "))

    try:
        data = get_exchange_rates(base_currency)
        rates = data['rates']
        converted_amount = convert_currency(amount, base_currency, target_currency, rates)
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
