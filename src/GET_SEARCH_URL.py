import re, urllib, random, requests
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

def rename_columns(strs_to_replace):
    modified_list = []
    for num in strs_to_replace:
        modified_list.append(num.replace('Redfin Estimate', 'redfin_est').replace('Beds', 'num_bdrms').replace(
            'Baths', 'num_bths').lower().replace('built: ', 'yr_blt').replace(':  ', '').replace(': ', '').replace(
            '.', '').replace('  ', '').replace('sq ft', 'sq_ft').replace(' ', '_').replace('#_of', 'num').replace(
            'year_built', 'yr_blt').replace('_(', '_').replace(')', '').replace(')', '').replace(',', '').replace(
            'minimum', 'min').replace('maximum', 'max'))
    return modified_list


def info_from_property(soup):

    top_info_dict = top_info_parser(soup, 1)
    public_info_dict = public_info_parser(soup, 1)
    school_dict = school_parser(soup, 1)
    all_home_feats = feats_parser(soup, 1)

    df = pd.DataFrame()
    df = pd.concat([top_info_dict, school_dict, public_info_dict,
                    all_home_feats], axis=1)

    df.columns = rename_columns(df.columns)

    num_bdrms = {'num_bdrms': ['num_bdrs', 'num_bdrs2']}
    num_bths = {'num_bths': ['num_bts2', 'num_bts']}
    sq_ft = {'sq_ft': ['sq_ft2', 'sq_ft']}
    yblt = {'yr_blt': ['yr_bt2', 'yr_bt']}

    df = df.rename(columns=lambda x: num_bdrms[x].pop(0) if x in num_bdrms.keys() else x)
    df = df.rename(columns=lambda x: num_bths[x].pop(0) if x in num_bths.keys() else x)
    df = df.rename(columns=lambda x: sq_ft[x].pop(0) if x in sq_ft.keys() else x)
    df = df.rename(columns=lambda x: yblt[x].pop(0) if x in yblt.keys() else x)

    return df


def gen_url(customer_df):
    zip_code = int(customer_df['zip'].values)
    city = str(customer_df['city'].values)
    type_home = (customer_df['home_type'].values)
    price = float(customer_df['price'].values)
    num_bds = int(customer_df['num_bds'].values)
    num_bths = float(customer_df['num_bths'].values)
    sqft = int(customer_df['sq_ft'].values)
    yr_blt = int(customer_df['yr_blt'].values)
    lot_sqft = int(customer_df['lot_sf'].values)
    hoa = customer_df['HOA'].values
    hoa_fee = float(customer_df['HOA_fee'].values)

    url_part_one = 'https://www.redfin.com/zipcode/' + \
        str(zip_code) + '/filter/sort=lo-days/'

    url_part_two = search_url_part_two_gen(type_home)

    url_part_three = search_url_part_three_gen(price)

    url_part_four = search_url_part_four_gen(num_bds)

    url_part_five = search_url_part_five_gen(num_bths)

    url_part_six = search_url_part_six_gen(sqft)

    url_part_seven = search_url_part_seven_gen(yr_blt)

    url_part_eight = search_url_part_eight_gen(lot_sqft)

    url_part_nine = search_url_part_nine_gen(hoa)

    search_url = url_part_one + url_part_two + url_part_three + \
        url_part_four + url_part_five + url_part_six + \
        url_part_seven + url_part_eight + url_part_nine

    return search_url
