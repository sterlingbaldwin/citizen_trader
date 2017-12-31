import argparse
import json

illegal_commodities = ['WiDoW', 'Stims', 'Altruciatoxin']

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', help='Path to your input csv or json', required=True)
	parser.add_argument('-s', '--start', help='Optional start location')
	parser.add_argument('-e', '--end', help='Optional end location')
	parser.add_argument('-c', '--commodity', help='Optional commodity preference')
	parser.add_argument('-l', '--legal', help="Only select legal commodities", action='store_true')
	return parser.parse_args()

def main():
	args = parse_args()
	trade_data = json.load(open(args.input))
	
	start_location = args.start if args.start else None
	end_location = args.end if args.end else None
	commodity = args.commodity if args.commodity else None
	if args.start:
		if start_location not in trade_data:
			print "Cant find {start} in trading data".format(start=args.start)
	if args.end:
		if end_location not in trade_data:
			print "Cant find {end} in trading data".format(end=args.end)


	best_value = 0
	best_buy_loc = None
	best_sell_loc = None
	best_commodity = None
	
	for buy_loc in trade_data.keys():
		if start_location and buy_loc != start_location:
			continue
		for buy_com, buy_price in trade_data[buy_loc]["Buy"].items():
			if buy_price == 0:
				continue
			if args.legal and buy_com in illegal_commodities:
				continue
			if args.commodity and buy_com != args.commodity:
				continue
			for sell_loc in trade_data.keys():
				if end_location and end_location != sell_loc:
					continue
				if sell_loc == buy_loc:
					continue
				for sell_com, sell_price in trade_data[sell_loc]["Sell"].items():
					if sell_price == 0:
						continue
					if sell_com != buy_com:
						continue
					value = float(sell_price) - float(buy_price)
					if value > best_value:
						best_value = value
						best_commodity = buy_com
						best_buy_loc = buy_loc
						best_sell_loc = sell_loc

	if not best_value or not best_commodity or not best_buy_loc or not best_sell_loc:
		print "Could not find a match, try relaxing your search parameteres"
	else:
		print "Best trade, buy {commodity} from {buy_location} and sell to {sell_location} for ${profit}/scu".format(
			commodity=best_commodity, buy_location=best_buy_loc, sell_location=best_sell_loc, profit=best_value)

if __name__ == '__main__':
	main()
