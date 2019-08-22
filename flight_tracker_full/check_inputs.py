import sys
import string
from url_dicts import regions_list
from month_dict import month_days

"""Input indexes
   YYYY  -  MM - DD
   0123  4  56 7 89

   #TOO MUCH WORK TO ENSURE DAY COUNT IN MONTH
"""

def get_integer():
	value = input()
	while(True):
		if(value.isnumeric()):
			return value
		else:
			print("That's not an integer!")
			value = input()

def determine_flight_type():
	print("\nAre you looking for a one-way or roundtrip flight?")
	print("one-way : 'ow' or roundtrip : 'rt'")
	type_trip = input()

	while(type_trip != 'ow' and type_trip != 'rt'):
		print("\nPlease provide input in correct format")
		print("one-way : 'ow' or roundtrip : 'rt'")
		type_trip = input()

	return type_trip

def get_regions():
	print("\nWhere in Europe are you interested?")
	print("You can pick 'Western', 'Southern' or 'Eastern', 'Done'")
	region = input()
	while(True):
		if region in regions_list:
			return region
		else:
			print("The acceptable inputs are: 'Western', 'Southern' or 'Eastern'")
			region = input()

def get_ow_date():
	print("\nPlease provide the departure day")
	start_day = check_date()
	return start_day


def get_rt_dates():
	print("\nPlease provide the departure day")
	start_day = check_date()

	print("\nPlease provide the return day")
	end_day = check_date()

	return start_day, end_day



def date_instructions(initial=True):
	if(initial is False):
		print("\nThe date provided is not correct")

	print("NOTE: Reference a calander to make sure correct")
	print("Format should be YYYY-MM-DD")

def check_date():
	date_instructions()
	input_date = input()
	while(True):
		year = input_date[0:4]
		month = input_date[5:7]
		day = input_date[8:10]
		#first four should be year
		if( check_year(year) ):
			if( check_month(month) ):
				if( (check_day(day, month)) ):
					return input_date
		date_instructions(initial=False)
		input_date = input()

	return input_date


def check_year(year):
	# must be 2019 or 2020 - can't go beyond in site
	first_two = year[0:2]
	last_two = year[2:4]
	if(year.isnumeric() ): #make sure you got integer	
		if(first_two == '20'):
			if(last_two == '19' or last_two == '20'):
				return True
	return False


def check_month(month):
	#Must be between 01 & 12
	#First digit must be 0 or 1 - second can be any number
	if( (month.isnumeric()) ):
		first_digit = month[0]
		second_digit = month[1]
		if( first_digit == '0' or first_digit == '1'):
			if( second_digit.isnumeric() ): 
				return True
	return False


def check_day(day, month):
	#Ensure day is between 1 - 31
	if( (day.isnumeric() ) ):
		day = int(day)
		if( (day > 0 & day < 32)):
			if(day <= int(month_days[month])):
				return True
	return False
