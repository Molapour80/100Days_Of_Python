def currency_converter():
    exchange_rates = {
        'USD': {'EUR': 0.85, 'IRR': 42000},
        'EUR': {'USD': 1.18, 'IRR': 49000},
        'IRR': {'USD': 0.000024, 'EUR': 0.000020}
    }

    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("Enter the currency you want to convert from (e.g., USD, EUR, IRR): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, IRR): ").upper()

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Conversion not available for the specified currencies.")

if __name__ == "__main__":
    currency_converter()