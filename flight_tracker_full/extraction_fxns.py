from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
from datetime import date, timedelta
from time import sleep
import numpy as np
import pandas as pd

def extract_roundtrip_info(start_day, end_day, url_dict, num_days):
	chromedriver_path = "/Users/AliBaba/downloads/chromedriver"

	browser = webdriver.Chrome(chromedriver_path)

	start_date = datetime.datetime.strptime(start_day, '%Y-%m-%d')
	end_date = datetime.datetime.strptime(end_day, '%Y-%m-%d')

	front_url = url_dict['front_url']
	middle_url = url_dict['middle_url']
	back_url = url_dict['back_url']

	fare_list = []

	for i in range(num_days):
	    start = str(start_date).split()[0]
	    end = str(end_date).split()[0]
	    
	    variable_url = front_url + start + middle_url + end + back_url

	    cards = get_cards_via_soup(variable_url, browser)
	    day_dict = {}
	    for card in cards:
	        city, fare = convert_key_val(card)
	        day_dict[city] = int(fare)
	    
	    series = pd.Series(day_dict)
	    df = pd.DataFrame(series, columns=[start])
	    fare_list.append(df)
	    
	    start_date = start_date + timedelta(days=1)
	    end_date = end_date + timedelta(days=1)

	return fare_list

def extract_oneway_info(start_day, url_dict, num_days):
	chromedriver_path = "/Users/AliBaba/downloads/chromedriver"

	browser = webdriver.Chrome(chromedriver_path)

	start_date = datetime.datetime.strptime(start_day, '%Y-%m-%d')

	front_url = url_dict['front_url']
	middle_url = url_dict['middle_url']
	back_url = url_dict['back_url']

	fare_list = []

	for i in range(num_days):
	    start = str(start_date).split()[0]
	    
	    variable_url = front_url + middle_url + start + back_url

	    cards = get_cards_via_soup(variable_url, browser)
	    day_dict = {}
	    for card in cards:
	        city, fare = convert_key_val(card)
	        day_dict[city] = int(fare)
	    
	    series = pd.Series(day_dict)
	    df = pd.DataFrame(series, columns=[start])
	    fare_list.append(df)
	    
	    start_date = start_date + timedelta(days=1)

	return fare_list

def get_cards_via_soup(variable_url, browser):
	sleep(np.random.randint(3,7))

	browser.get(variable_url)

	soup = BeautifulSoup(browser.page_source, 'html.parser')

	return soup.select('div[class*=info-container]')


def convert_key_val(card):
    pre_city = card.select('h3')[0].text
    city = str(pre_city)
    pre_fare = card.select('span[class*=price]')[0].text
    fare = str(pre_fare)
    #Need to do this in order to ensure clean dataframe when concat the series
    if fare == '':
        fare = '0'
    else:   #lets just get the comma and dollar sign out of the way
        fare = (fare.replace(',','').split('$')[1])
    return city, fare