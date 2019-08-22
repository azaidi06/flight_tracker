import numpy as np
import pandas as pd

def get_print_lowest(prices_list, lowest_count):
	length = len(prices_list)
	low_count = int(lowest_count)
	for x in range(length):
		one_day = prices_list[x]
		#slice out all indexes with zero values
		cleared_day = one_day[one_day > 0]
		
		day = one_day.columns[0]
		cheapest_prices = cleared_day.nsmallest(low_count, day)
		print_lowest(cheapest_prices, low_count, day)
	


def print_lowest(cheapest_prices, low_count, day):
	print("The cheapest flights on {}:".format(day))
	for x in range(low_count):
		price = cheapest_prices.values[x][0]
		destination = cheapest_prices.index[x]
		print("\t({}) {} : {}".format(x + 1,
							destination, price))
	print("\n")