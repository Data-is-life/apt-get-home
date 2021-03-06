import random
from header_list import user_agent_list
from proxies_list import proxies_list_
from initial_scrapper_function import *
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
