from math import ceil
import time, re, ast, sys, urllib, random, string, requests
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
from GET_RESULTS import *
ua = user_agent_list

''' This puts all the files together and gets the results'''

customer_url = input("Paste the Redfin URL of the Home: ")
url = customer_url

print(f'The Redfin link you entered for the home: {url}')

header = random.sample(ua, 1)[0]
soup = session_creator(ua, url)

customer_df = info_from_property(soup)

print (customer_df.T)

c_url = gen_zip_url(customer_df)

header = random.sample(ua, 1)[0]
soup_ = session_creator(ua, c_url)

print (get_results(soup_, customer_df))
