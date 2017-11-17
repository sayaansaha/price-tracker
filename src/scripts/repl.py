from ..libs import priceapi

prices = PriceFetcher()

def main():
	data = prices.get_price_cancun()
	print data

main()