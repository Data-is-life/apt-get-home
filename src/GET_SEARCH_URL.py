import re, urllib, random, requests
import pandas as pd
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

def info_from_property(soup):

    top_info_dict = top_info_parser(soup, 1)
    public_info_dict = public_info_parser(soup, 1)
    school_dict = school_parser(soup, 1)
    all_home_feats = feats_parser(soup, 1)

    df = pd.DataFrame()
    df = pd.concat([top_info_dict, school_dict, public_info_dict,
                    all_home_feats], axis=1)

    df.columns = rename_columns(df.columns)

    return df


def gen_url(customer_df):
    zip_code = int(customer_df['zip'].values)
    city = str(customer_df['city'].values)
    type_home = (customer_df['home_type'].values)
    price = float(customer_df['price'].values)
    num_bds = int(customer_df['num_bds'].values)
    num_bths = float(customer_df['num_bths'].values)
    sqft = int(customer_df['sqft'].values)
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
