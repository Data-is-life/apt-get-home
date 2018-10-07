# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/04/2018


from math import ceil
import time
import re
import ast
import sys
import urllib
import random
import string
import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from itertools import cycle
from header_list import user_agent_list
from proxies_list import proxies_list_
from INITIAL_SCRAPPER_FUNCTIONS import *
from PARSER_FUNCTIONS import *
from LIST_DF_FUNCTIONS import *
from SEARCH_URL_GEN import *
from GET_SEARCH_URL import *

ua = user_agent_list
proxies = proxies_list_

header = random.sample(ua, 1)[0]
proxy = random.sample(proxies, 1)[0]

''' This is used to collect number of homes that matched users interest'''

def prop_count_(soup):

    all_count = soup.findAll('div', {'class': 'homes summary'})
    if len(str(all_count)) >= 20:
        prp_list = [re.findall('\d+', num.text) for num in all_count]
        return prp_list[0][0]
    else:
        print('Error on Page. Please try running it again.')

''' This is used to get results from the search pages'''

def props_from_search_page(soup):

    full_soup = soup.findAll('a', {'class': 'bottom link-override'})

    full_address = [fas['title'] for fas in full_soup]

    home_link = ['https://www.redfin.com' +
                 str(hls.get('href')) for hls in full_soup]

    df = {'full_address': full_address, 'home_link': home_link}

    return df


'''This is used to run the search and display results'''

def get_results(soup, customer_df):

    print(f'Found {prop_count_(soup)} properties')

    results_from_search_page = props_from_search_page(soup)

    search_result_url_list = results_from_search_page['home_link']

    if len(search_result_url_list) >= 2:
        print(f'Here are top two homes out of {prop_count_(soup)}:')
        print(f'Home # 1: {search_result_url_list[0]}')
        print(f'Home # 2: {search_result_url_list[1]}')
    elif len(search_result_url_list) == 1:
        if
        print('Here is the only home I could find like the one you entered:')
        print(f'Home # 1: {search_result_url_list[0]}')
    elif 'captcha' in soup.text:
        print("Getting captcha from Redfin")
    else:
        print ("Didn't find anything similar in the same zip code")
        customer_response = input("Would you like to search the entire city? (y or n): ")
        if customer_response.lower() == 'y':
            city_url = gen_city_url(customer_df)
            soup_ = session_creator(proxy, ua, city_url)
            print(f'Found {prop_count_(soup_)} properties')

            results_from_search_page = props_from_search_page(soup_)

            search_result_url_list = results_from_search_page['home_link']
            if len(search_result_url_list) >= 2:
                print(f'Here are top two homes out of {prop_count_(soup)}:')
                print(f'Home # 1: {search_result_url_list[0]}')
                print(f'Home # 2: {search_result_url_list[1]}')
            elif len(search_result_url_list) == 1:
                print('Here is the only home I could find like the one you entered:')
                print(f'Home: {search_result_url_list[0]}')
            elif 'captcha' in soup_.text:
                    print("Getting captcha from Redfin")
                else:
                    print ("Didn't find anything similar in the same city either. I'm working on improving your next experience")
