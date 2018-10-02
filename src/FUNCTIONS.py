## Author: Mohit Gangwani
## Github: Data-is-Life
## Date: 09/27/2018

from math import ceil
import time
import re
import ast
import sys
import urllib
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.error import URLError
import requests
from itertools import cycle
import string

def proxie_check(proxies):
    default_list = []
    url = 'https://httpbin.org/ip'
    for i in range(0, len(proxies)):
        time.sleep(random.uniform(0.5,1.5))
        proxy = proxies[i]
        print(i+1)
        start_time = time.time()
        try:
            response = requests.get(
                url, proxies={"http": proxy, "https": proxy})
            print(response.json())
            print(time.time() - start_time)
        except:
            print("Skipping. Connnection error")
            default_list.append(i+1)
            print(time.time() - start_time)
            proxies.remove(proxy)
        print(default_list)
    return proxies


def strip_count(lst):
    rx_num_homes = r'\d+\shomes'
    rx_zip = r'\d+\sat'
    rx_median = r'\$\d+\.?\w+'
    median_list = []
    zip_list = []
    num_homes_list = []
    for num in lst:
        num = str(num)
        median_ = re.findall(rx_median, num, re.MULTILINE)
        zip_ = re.findall(rx_zip, num, re.MULTILINE)
        num_homes_ = re.findall(rx_num_homes, num, re.MULTILINE)
        median_list.extend([i for i in median_])
        zip_list.extend([i for i in zip_])
        num_homes_list.extend([i for i in num_homes_])

    median_list = [num.replace('$', '').replace(
        'K', ',000').replace('.', ',') for num in median_list]
    i = 0
    while i < len(median_list):
        if len(median_list[i]) == 2:
            median_list[i] = median_list[i].replace('M', ',000,000')
            i += 1
        elif len(median_list[i]) == 4:
            median_list[i] = median_list[i].replace('M', '00,000')
            i += 1
        elif len(median_list[i]) == 5:
            median_list[i] = median_list[i].replace('M', '0,000')
            i += 1
        else:
            i += 1
    zip_list = [re.findall(r'\d+', num, re.MULTILINE)[0] for num in zip_list]
    num_homes_list = [re.findall(r'\d+', num, re.MULTILINE)[0]
                      for num in num_homes_list]

    df = pd.DataFrame(
        data={'zip': zip_list, 'median_price': median_list, 'num_ap_homes': num_homes_list})
    return df

def gen_url_list(zip_list):
    active_url_list = []
    sold_url_list = []
    for num in zip_list:
        
        if num >= 10000:
            url_asaul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=lo-price,property-type=house'
            active_url_list.append(url_asaul)

            url_asdul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=hi-price,property-type=house'
            active_url_list.append(url_asdul)

            url_ssaul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=lo-price,property-type=house,include=sold-3mo'
            sold_url_list.append(url_ssaul)

            url_ssdul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=hi-price,property-type=house,include=sold-3mo'
            sold_url_list.append(url_ssdul)

            url_actaul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=lo-price,property-type=condo+townhouse'
            active_url_list.append(url_actaul)

            url_actdul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=hi-price,property-type=condo+townhouse'
            active_url_list.append(url_actdul)

            url_sctaul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=lo-price,property-type=condo+townhouse,include=sold-3mo'
            sold_url_list.append(url_sctaul)

            url_sctdul = 'https://www.redfin.com/zipcode/' + str(num) + \
                '/filter/sort=hi-price,property-type=condo+townhouse,include=sold-3mo'
            sold_url_list.append(url_sctdul)
        
        else:
            url_asaul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=lo-price,property-type=house'
            active_url_list.append(url_asaul)

            url_asdul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=hi-price,property-type=house'
            active_url_list.append(url_asdul)

            url_ssaul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=lo-price,property-type=house,include=sold-3mo'
            sold_url_list.append(url_ssaul)

            url_ssdul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=hi-price,property-type=house,include=sold-3mo'
            sold_url_list.append(url_ssdul)

            url_actaul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=lo-price,property-type=condo+townhouse'
            active_url_list.append(url_actaul)

            url_actdul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=hi-price,property-type=condo+townhouse'
            active_url_list.append(url_actdul)

            url_sctaul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=lo-price,property-type=condo+townhouse,include=sold-3mo'
            sold_url_list.append(url_sctaul)

            url_sctdul = 'https://www.redfin.com/zipcode/0' + str(num) + \
                '/filter/sort=hi-price,property-type=condo+townhouse,include=sold-3mo'
            sold_url_list.append(url_sctdul)
    
    return active_url_list, sold_url_list