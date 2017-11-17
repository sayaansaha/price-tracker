from ..libs import priceapi

prices = PriceFetcher()

def main():
	data = prices.get_price_cancun('2018-01-10', '2018-01-17')
	print data

main()