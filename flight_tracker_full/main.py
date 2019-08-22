import numpy as np
import pandas as pd
from extraction_fxns import extract_roundtrip_info
from extraction_fxns import extract_oneway_info
from parse_extraction import combine_days
#from url_dicts import western_europe_url, southern_europe_url
from url_dicts import rt_regions_dict, ow_regions_dict
from graph_control import graph_control
from print_lowest_prices import get_print_lowest
from check_inputs import get_integer, get_regions
from check_inputs import get_rt_dates, get_ow_date
from check_inputs import determine_flight_type



if __name__ == '__main__':
	#start_day = '2020-03-29'
	#end_day = '2020-04-12'

	#Find out one way or roundtrip
	type_trip = determine_flight_type()


	region = get_regions()

	print("\nWhat window of departure will you consider?")
	num_days = int(get_integer())

	#get dates of trip from user
	prices_list = pd.DataFrame()
	if(type_trip == 'rt'):
		start_day, end_day = get_rt_dates()
		prices_list = (extract_roundtrip_info(start_day, end_day,
	                                rt_regions_dict[region], 
	                                num_days=num_days))
	else:
		start_day = get_ow_date()
		prices_list = extract_oneway_info(start_day,
                                ow_regions_dict[region], 
                                num_days=num_days)
	
	print("\nHow many of lowest prices per day do you want to see?")
	lowest_count = int(get_integer())

	get_print_lowest(prices_list, lowest_count)

	prices_df = combine_days(prices_list)

	#graph_control(prices_df)