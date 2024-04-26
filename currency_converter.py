from forex_python.converter import CurrencyRates
from decimal import Decimal
def convertcurrency(amount, before_currency, after_currency):
	cr = CurrencyRates()
	converted_currency = cr.convert(before_currency, after_currency, Decimal(str(amount)))
	return converted_currency
if __name__ == "__main__":
	before_currency = input("your current currency:").upper()
	after_currency = input("in which you want to conver your currency:").upper()
	amount = float(input("your amount:"))
	converted_amount = convertcurrency(amount, before_currency, after_currency)
	print(f"{amount} {before_currency} is equal to {converted_amount} {after_currency}")