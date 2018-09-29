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
        print(default_list)
    return default_list

def session_creator(proxy, ua, url):
    header = random.sample(ua, 1)[0]
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    req = session.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup

def zip_prop_count(zip_list, proxies, prp_list, ua, ezl):
    proxy = random.sample(proxies, 1)[0]
    print(proxies.index(proxy))
    print(proxy)
    for num in zip_list:
        url = 'https://www.redfin.com/zipcode/' + \
            str(num)+'/filter/property-type=house+condo+townhouse,include=sold-1yr,min-price=100k,min-baths=1,include=sold-1yr'
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
                print(len(zip_list)+len(prp_list))
            else:
                print("Captcha!!!!!")
        except:
            print("Skipping. Connnection error")
            proxies.remove(proxy)
            print(len(proxies))
            return prp_list, zip_list, proxies, ezl
    return prp_list, zip_list, proxies, ezl

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

def each_page(proxy, ua, url):
    soup = session_creator(proxy, ua, url)
    start_time = time.time()
    time.sleep(random.uniform(0, 1)*4)
    print(time.time()-start_time)
    full_soup = soup.findAll('a', {'class': 'bottom link-override'})
    full_address = [fas['title'] for fas in full_soup]
    home_link = ['https://www.redfin.com' +
                 str(hls.get('href')) for hls in full_soup]
    df = {'full_address': full_address, 'home_link': home_link}
    return df

def links_for_props(proxies, url_list, main_df, ua):
    proxy = random.sample(proxies, 1)[0]
    print(proxies.index(proxy))
    print(proxy)
    i = 0
    while i < len(url_list):
        url = url_list[i]        
        try:
            start_time = time.time()
            print(len(url_list))
            print(url)
            
            data = each_page(proxy, ua, url)
            df = pd.DataFrame(data)
            eds = {'full_address': [], 'home_link': []}
            if data['full_address'] != eds['full_address']:
                main_df = pd.concat([main_df, df])
                url_list.pop(i)
                print(time.time() - start_time)
            else:
                print('Captcha')
                return url_list, main_df
        except:
            print("Skipping. Connnection error")
            proxies.remove(proxy)
            print(len(proxies))

            return url_list, main_df

    return url_list, main_df

