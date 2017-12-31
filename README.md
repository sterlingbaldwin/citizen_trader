# citizen_trader
A trade optimizer for StarCitizen.

Writen by GeneralPandamonium, using trade data from Commander Haas.
https://docs.google.com/spreadsheets/d/1t7W9GV8XETgkX6em6uAOEx7QMQFZwQpHqRRPqqGXDrE/edit#gid=0

Given an imput file with trade data, find the most lucrative single hope trade route.

```
usage: trader.py [-h] -i INPUT [-s START] [-e END] [-c COMMODITY] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to your input csv or json
  -s START, --start START
                        Optional start location
  -e END, --end END     Optional end location
  -c COMMODITY, --commodity COMMODITY
                        Optional commodity preference
  -l, --legal           Only select legal commodities
```

Example usage:

```
python trader.py -i SC_Trading_Main.json 
Best trade, buy WiDoW from Secret Location and sell to Grim Hex for $76.88/scu
```

Obviously buying narcotics will net you the highest profit/scu, but we're not all smugglers right? Use the -l or --legal flag to turn off illegal items.

```
python trader.py -i SC_Trading_Main.json -l
Best trade, buy Laranite from Kudre Ore and sell to Port Olisar for $38.9/scu
```

Maybe Im planning on heading to Grim Hex, and want to know the best good to bring to market there, use the -e, or --end flag to pick an ending location. Similarly use the -s, or --start flag to pick a starting location.

```
python trader.py -i SC_Trading_Main.json -l -e "Grim Hex"
Best trade, buy Distilled Spirits from Terra Mills Hydro-Farm and sell to Grim Hex for $5.24/scu
```



Trade data must be a valid JSON object, in the format:

```
{
	LocationA: {
		"Buy": {
			"Commodity_1": "1",
			"Commodity_2": "2"
		},
		"Sell": {
			"Commodity_1": "1",
			"Commodity_2": "2"
		}
	},
	LocationB: {
		"Buy": {
			"Commodity_1": "0",
			"Commodity_2": "0"
		},
		"Sell": {
			"Commodity_1": "1",
			"Commodity_2": "2"
		}
	}
}
```

Any 0s in the buy or sell list denote that the location doesnt buy/sell that good.
