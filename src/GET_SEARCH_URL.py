# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/03/2018


import re
import urllib
import random
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from header_list import user_agent_list
from proxies_list import proxies_list_
from INITIAL_SCRAPPER_FUNCTIONS import *
from PARSER_FUNCTIONS import *
from LIST_DF_FUNCTIONS import *
from SEARCH_URL_GEN import *
ua = user_agent_list
proxies = proxies_list_


def gen_last_part_url(customer_df):
    num_range_to_check = list(range(100))
    num_range_to_check = [str(num) for num in num_range_to_check]

    yr_range_to_check = list(range(1800, 2050))
    yr_range_to_check = [str(num) for num in yr_range_to_check]

    '''Converting zip code to an int, to make sure it is valid'''

    zip_code = int(customer_df['zip_code'][1])

    '''Cleaning city name if we need to do a search with it'''

    city = customer_df['city'][1].replace(',', '')

    '''Making sure the type of home is used for better results'''

    type_home = customer_df['prop_type'][1]

    '''Using the Redfin Estimate first to determine the price range of the search,
    follwed by last sold price, if they property is sold, or listing price if the
    property is active or pending. '''

    if 'red_est' in customer_df.columns:
         price = float(customer_df['red_est'][
             1].replace('$', '').replace(',', ''))
    elif 'last_sold_price' in customer_df.columns:
        price = float(customer_df['last_sold_price'][
            1].replace('$', '').replace(',', ''))
    elif 'price' in customer_df.columns:
        price = float(customer_df['price'][1].replace(
            '$', '').replace(',', '').replace('+', ''))
    else:
        price = 0

    '''Making sure we have the right bathroom count'''

    if customer_df['num_bdrs'][1] in num_range_to_check:
        num_bds = float(customer_df['num_bdrs'][1])
    elif customer_df['num_beds'][1] in num_range_to_check:
        num_bds = float(customer_df['num_beds'][1])
    else:
        num_bds = -1

    '''Making sure we have the right bathroom count'''

    if customer_df['num_bts'][1] != '-':
        num_bths = float(customer_df['num_bts'][1])
    elif customer_df['num_num_bts'][1] in num_range_to_check:
        num_bths = float(customer_df['num_num_bts'][1])
    else:
        num_bths = -1

    sqft = float(customer_df['sq_ft'][1].replace(',', '').replace(' ', ''))

    '''Getting year built from the home'''

    if ('year_built' in customer_df.columns and customer_df['year_built'][1] in yr_range_to_check):
        yr_blt = float(customer_df['year_built'][1])
    elif ('built' in customer_df.columns and customer_df['built'][1] in yr_range_to_check):
        yr_blt = float(customer_df['built'][1])
    else:
        yr_blt = 9999

    '''Lot size getting converted to sqft and float'''

    lot_sqft = customer_df['lot_size'][1].replace(
        ',', '').replace(' ', '').replace('—', '0')

    if ('Sq' in lot_sqft or 'Ft' in lot_sqft):
        lot_sqft = int(''.join(num for num in re.findall(r'\d', lot_sqft)))
    elif ('ac' in lot_sqft or 're' in lot_sqft):
        lot_sqft = int(
            float(''.join(num for num in re.findall(r'\d?\.?\d?\d?', lot_sqft))) * 43560)
    elif (float(lot_sqft) > 0 and float(lot_sqft) < 10):
        lot_sqft = int(
            float(''.join(num for num in re.findall(r'\d?\.?\d?\d?', lot_sqft))) * 43560)
    elif '—' in lot_sqft:
        lot_sqft = 0
    else:
        lot_sqft = int(''.join(num for num in re.findall(r'\d', lot_sqft)))

    '''Checking to see if there is any HOA fees'''

    if 'hoa_fees' in customer_df.columns:
        hoa_fee = float(customer_df['hoa_fees'].values)

        url_part_nine = ',' + search_url_part_nine_gen(hoa_fee)
    else:
        url_part_nine = ''

    '''Putting them all together'''

    url_part_two = ',' + search_url_part_two_gen(type_home)
    if len(url_part_two) <= 2:
        url_part_two = ''

    url_part_three = ',' + search_url_part_three_gen(price)
    if len(url_part_three) <= 2:
        url_part_three = ''

    url_part_four = ',' + search_url_part_four_gen(num_bds)
    if len(url_part_four) <= 2:
        url_part_four = ''

    url_part_five = ',' + search_url_part_five_gen(num_bths)
    if len(url_part_five) <= 2:
        url_part_five = ''

    url_part_six = ',' + search_url_part_six_gen(sqft)
    if len(url_part_six) <= 2:
        url_part_six = ''

    url_part_seven = ',' + search_url_part_seven_gen(yr_blt)
    if len(url_part_seven) <= 2:
        url_part_seven = ''

    url_part_eight = ',' + search_url_part_eight_gen(lot_sqft)
    if (len(url_part_eight) <= 1 or (type_home == re.compile('^Cond') or type_home == re.compile('^Town'))):
        url_part_eight = ''

    last_part_url = url_part_two + url_part_three + \
        url_part_four + url_part_five + url_part_six + \
        url_part_seven + url_part_eight + url_part_nine

    return last_part_url


def gen_zip_url(customer_df):
    zip_code = int(customer_df['zip_code'][1])
    url_part_one = 'https://www.redfin.com/zipcode/' + str(zip_code) + '/filter/sort=lo-days'
    last_part_url = gen_last_part_url(customer_df)
    url = url_part_one + last_part_url
    return url


def gen_city_url(customer_df):
    city = customer_df['city'][1].replace(',', '').replace(' ', '-')
    if city[-1] == '-':
        city = city[:-1]
    type_home = customer_df['prop_type'][1]
    url_part_one = 'https://www.redfin.com/city/' + city + '/filter/sort=lo-days'
    last_part_url = gen_last_part_url(customer_df)
    url = url_part_one + last_part_url
    return url
