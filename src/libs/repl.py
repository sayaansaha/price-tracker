from priceapi import PriceFetcher

def main():
	fetcher = PriceFetcher()
	data = fetcher.get_price_cancun('2017-11-11', '2017-11-18')
	print(data)

main()