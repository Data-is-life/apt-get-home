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
from initial_scrapper_functions import *
from parser_functions import *
from list_df_functions import *
from search_url_gen import *
from get_search_url import *
from get_results import *
ua = user_agent_list
proxies = proxies_list_

''' This puts all the files together and gets the results'''

customer_url = input("Paste the Redfin URL of the Home: ")
url = customer_url

print(f'The Redfin link you entered for the home: {url}')

proxy = random.sample(proxies, 1)[0]
header = random.sample(ua, 1)[0]
soup = session_creator(ua, url, proxy)

customer_df = info_from_property(soup)

print(customer_df.T)

c_url = gen_zip_url(customer_df)

header = random.sample(ua, 1)[0]
soup_ = session_creator(ua, c_url, proxy)

print(get_results(soup_, customer_df))
