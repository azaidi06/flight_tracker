import sys
from viz_fxns import four_destination_scatter, dest_single_plot
from parse_extraction import print_countries_extracted

def graph_control(prices_data_frame):
	type_graph = viz_type()
	if type_graph == "Scatter":
		destinations = destinations_extract(prices_data_frame, True)
		four_destination_scatter(prices_data_frame, destinations)
	else:
		destinations = destinations_extract(prices_data_frame, False)
		dest_single_plot(prices_data_frame, destinations)

def viz_type():
	print("How would you like to visualize the data?")
	print("Individual scatter plots or Combined?")
	viz_type = check_correct_graph_input()
	return viz_type

def check_correct_graph_input():
	viz_type = input()
	while(True):
		if viz_type == 'Scatter' or viz_type == 'Combined':
			break
		else:
			print("Please enter either: 'Individual' or 'Combined'")
			viz_type = input()
	return viz_type

def get_correct_destinations(prices_df, count):
	destinations = []
	while (len(destinations) < count):
		print("\nYou've provided {} destinations so far".format(len(destinations)))
		print("Please copy & paste countries (one at a time) or type 'done':")
		dest = input()
		if (dest == 'done'):
			return destinations
		else:
			if (dest in prices_df.index):
				destinations.append(dest)
	return destinations

def destinations_extract(prices_data_frame, scatter):
	print_countries_extracted(prices_data_frame)
	count = 4 if scatter else 6
	print("\nWe need up to {} countries from above:".format(count))
	destinations = get_correct_destinations(prices_data_frame, count)
	return destinations