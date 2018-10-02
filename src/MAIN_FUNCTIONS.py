## Author: Mohit Gangwani
## Github: Data-is-Life
## Date: 10/01/2018

import time, re, ast, sys, urllib, time, random
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import requests, string
from header_list import user_agent_list
from SCRAPPER_FUNCTIONS import session_creator

ua = user_agent_list

def gen_sold_prop_info(url, hdr, proxy):

    soup = session_creator(proxy, ua, url)

    price_regex = r'\$\S+\s+'
    bed_regex = r'\d+\S?\d?\d?Bed'
    bath_regex = r'\d+\S?\d?\d?Bath'
    size_regex = r'\d+\S?\d?\d?\s?Sq'
    yr_blt_regex = r'Built: \d+'
    status_regex = r'Status: \w+'
    home_dict = dict()

    home_address_MLS = soup.title.string
    add_list = text.split(sep=' |')
    zip_code = re.search('\d+$', add_list[0])
    mls_num = re.search('\d+$', add_list[1])
    home_add = re.search('(.+?),', home_address_MLS)
    home_city = re.search(',(.+?),', home_address_MLS)
    home_state = add_list[0].replace(home_add.group(1), '').replace(
        home_city.group(1), '').replace(zip_code.group(), '').replace(
        ',', '').replace(' ', '')

    home_dict['address'] = home_add.group(1)
    home_dict['city'] = home_city.group(1)
    home_dict['zip_code'] = zip_code.group()
    home_dict['state'] = home_state
    home_dict['mls_num'] = mls_num.group()

    all_top = soup.findAll('div', {'class': 'HomeInfo inline-block'})
    price_list = []
    for num in all_top:
        a = num.text
        price_list.extend(re.findall(price_regex, a))
        home_dict['num_beds'] = (re.findall(bed_regex, a))
        home_dict['num_baths'] = (re.findall(bath_regex, a))
        home_dict['home_sqft'] = (re.findall(size_regex, a))
        home_dict['yr_blt'] = (re.findall(yr_blt_regex, a))
        home_dict['status'] = (re.findall(status_regex, a))

    home_dict['redfin_est'] = [num for num in price_list if 'Redfin' in num]
    home_dict['sold_price'] = [num for num in price_list if 'Last' in num]

    home_description = soup.find('p', {'class': 'font-b1'})
    home_dict['description'] = home_description.span.text

    all_home_feats = soup.findAll('span', {'class': "entryItemContent"})
    feats = [num.text for num in all_home_feats]

    # prop_hist = soup.findAll(
    #     'div', {'id': 'propertyHistory-expandable-segment'})
    # prop_history = [num.text for num in prop_hist]

    school_info = soup.findAll('div', {'class': "name-and-info"})
    schools = [num.text for num in school_info]

    return home_dict, feats, prop_history, schools