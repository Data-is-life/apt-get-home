# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 09/30/2018

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
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from itertools import cycle


def session_creator(proxy, ua, url):

    header = random.sample(ua, 1)[0]

    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    req = session.get(url, headers=header)

    soup = BeautifulSoup(req.text, 'lxml')

    return soup


def proxie_check(proxies):

    default_list = []
    url = 'https://httpbin.org/ip'

    for i in range(0, len(proxies) - 1):

        print(i + 1)
        proxy = proxies[i]

        time.sleep(random.uniform(0.5, 1.5))
        start_time = time.time()

        try:

            time.sleep(random.uniform(1, 2))
            response = requests.get(
                url, proxies={"http": proxy, "https": proxy})

            print(response.json())
            print(time.time() - start_time)

        except:

            print("Skipping. Connnection error")
            print(time.time() - start_time)

            default_list.append(i + 1)

        print(default_list)

    return proxies


def zip_prop_count(zip_list, proxies, prp_list, ua, ezl):

    proxy = random.sample(proxies, 1)[0]

    print(proxies.index(proxy))
    print(proxy)

    for num in zip_list:

        url = 'https://www.redfin.com/zipcode/' + \
            str(num) + '/filter/property-type=house+condo+townhouse,' + \
            'include=sold-1yr,min-price=100k,min-baths=1,include=sold-1yr'

        try:

            start_time = time.time()
            soup = session_creator(proxy, ua, url)

            print(num)
            print(len(zip_list))

            all_count = soup.findAll('div', {'class': 'homes summary'})

            if len(str(all_count)) >= 20:
                print(all_count)
                print(time.time() - start_time)
                ezl.append(num)
                prp_list.append(all_count)
                zip_list.remove(num)
                print(len(zip_list) + len(prp_list))

            else:
                print("Captcha!!!!!")
        except:
            print("Skipping. Connnection error")
            proxies.remove(proxy)
            print(len(proxies))
            return prp_list, zip_list, proxies, ezl

    return prp_list, zip_list, proxies, ezl


def each_page(proxy, ua, url):

    soup = session_creator(proxy, ua, url)

    # start_time = time.time()
    time.sleep(random.uniform(0, 1) * 3)
    # print(time.time() - start_time)

    full_soup = soup.findAll('a', {'class': 'bottom link-override'})

    full_address = [fas['title'] for fas in full_soup]

    home_link = ['https://www.redfin.com' +
                 str(hls.get('href')) for hls in full_soup]

    df = {'full_address': full_address, 'home_link': home_link}

    return df


def links_for_props(proxies, url_list, main_df, ua):

    proxy = random.sample(proxies, 1)[0]
    print(f'proxy number: {proxy}')

    i = randint(0, (len(url_list) // 2))
    print(f'starting from url number: {i}')

    while i < len(url_list):
        url = url_list[i]

        try:
            b = random.uniform(0.75, 2.25)
            time.sleep(b)
            # start_time = time.time()
            # print(f'total left: {len(url_list)}')

            data = each_page(proxy, ua, url)
            df = pd.DataFrame(data)
            eds = {'full_address': [], 'home_link': []}
            if data['full_address'] != eds['full_address']:
                main_df = pd.concat([main_df, df])
                url_list.pop(i)
                # a = (time.time() - start_time) * len(url_list)
                # print('SUCCESS!!')
                # print(f'Currently on url number: {i}')
                # print(f'time taken: {a/len(url_list)}')
                if i > 0:
                    i -= randint(0, 1)
                else:
                    i += 0
            else:
                # print('No results')
                # print(f'Currently on url number: {i}')
                i += randint(1, 5)
        except:
            # print("Skipping. Connnection error")
            proxies.remove(proxy)
            # print(f'proxies left: {len(proxies)}')
            # print(f'total left: {len(url_list)}')

            return url_list, main_df, proxies

    return url_list, main_df, proxies
