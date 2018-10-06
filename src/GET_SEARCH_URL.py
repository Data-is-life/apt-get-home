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


def rename_columns_big(strs_to_replace):
    modified_list = []
    for num in strs_to_replace:
        modified_list.append(num.lower().replace('bedrooms', 'beds').replace(
            '# of ', 'num_').replace('sq. ft.', 'sq_ft').replace(':  ', '').replace(
            ': ', '').replace('.', '').replace('  ', '').replace(' ', '_').replace(
            '_(', '_').replace(')', '').replace(')', '').replace(',', '').replace(
            'minimum', 'min').replace('maximum', 'max').replace('$', 'price'))
    return modified_list


def info_from_property(soup):

    top_info_dict = top_info_parser(soup, 1)
    public_info_dict = public_info_parser(soup, 1)
    school_dict = school_parser(soup, 1)
    all_home_feats = feats_parser(soup, 1)

    df = pd.DataFrame()
    df = pd.concat([top_info_dict, school_dict, public_info_dict,
                    all_home_feats], axis=1)

    df.columns = rename_columns_big(df.columns)

    return df


def gen_zip_url(customer_df):
    zip_code = int(customer_df['zip_code'][1])
    city = customer_df['city'][1].replace(',', '')
    type_home = customer_df['style'][1]

    if 'last_sold_price' in customer_df.columns:
        price = float(customer_df['last_sold_price'][
            1].replace('$', '').replace(',', ''))
    else:
        price = float(customer_df['price'][1].replace(
            '$', '').replace(',', '').replace('+', ''))

    num_bds = int(customer_df['num_bdrs'][1])

    num_bths = float(customer_df['num_bts'][1])

    sqft = int(customer_df['sq_ft'][1].replace(',', '').replace(' ', ''))

    if 'yr_bt' in customer_df.columns:
        yr_blt = int(customer_df['yr_bt'][1].replace('—', '5000'))
    elif 'year_built' in customer_df.columns:
        yr_blt = int(customer_df['year_built'][1].replace('—', '5000'))

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

    if 'hoa' in customer_df.columns:
        hoa = customer_df['hoa'].values
        hoa_fee = float(customer_df['hoa_fee'].values)
        url_part_nine = ',' + search_url_part_nine_gen(hoa_fee)
    else:
        url_part_nine = ''

    url_part_one = 'https://www.redfin.com/zipcode/' + \
        (zip_code) + '/filter/sort=lo-days'

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

    search_url = url_part_one + url_part_two + url_part_three + \
        url_part_four + url_part_five + url_part_six + \
        url_part_seven + url_part_eight + url_part_nine

    return search_url


def gen_city_url(customer_df):
    city = customer_df['city'][1].replace(',', '').replace(' ', '-')
    if city[-1] == '-':
        city = city[:-1]
    type_home = customer_df['style'][1]

    if 'last_sold_price' in customer_df.columns:
        price = float(customer_df['last_sold_price'][
            1].replace('$', '').replace(',', ''))
    else:
        price = float(customer_df['price'][1].replace(
            '$', '').replace(',', '').replace('+', ''))

    num_bds = int(customer_df['num_bdrs'][1])

    num_bths = float(customer_df['num_bts'][1])

    sqft = int(customer_df['sq_ft'][1].replace(',', '').replace(' ', ''))

    if 'yr_bt' in customer_df.columns:
        yr_blt = int(customer_df['yr_bt'][1].replace('—', '5000'))
    elif 'year_built' in customer_df.columns:
        yr_blt = int(customer_df['year_built'][1].replace('—', '5000'))

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

    if 'hoa' in customer_df.columns:
        hoa = customer_df['hoa'].values
        hoa_fee = float(customer_df['hoa_fee'].values)
        url_part_nine = ',' + search_url_part_nine_gen(hoa_fee)
    else:
        url_part_nine = ''

    url_part_one = 'https://www.redfin.com/city/' + city + '/filter/sort=lo-days'

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

    search_url = url_part_one + url_part_two + url_part_three + url_part_four + \
        url_part_five + url_part_six + url_part_seven + url_part_eight + url_part_nine

    return search_url
