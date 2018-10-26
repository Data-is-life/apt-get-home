# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 09/30/2018

import time
import urllib
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


def session_creator(ua, url, proxy):
    '''This function is used to create a session to get data from a website.
    Proxies are used so the user's IP address is masked.'''

    header = random.sample(ua, 1)[0]
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    req = session.get(url, headers=header)

    soup = BeautifulSoup(req.text, 'lxml')

    return soup


def proxie_check(proxies):
    '''This function connects to a website that checks and if the proxies in the
    list are working.'''

def proxie_check(proxies):
    sprfst = []
    fst = []
    keep = []
    meh = []
    slw = []
    snl = []
    usls = []
    url = 'https://httpbin.org/ip'
    for i in range(1, (len(proxies))+1):
        proxy = proxies[i-1]
        start_time = time.time()
        try:
            response = requests.get(
                url, proxies={"http": proxy, "https": proxy})
            
            total_time = time.time()-start_time

            if total_time <= 1.00:
                sprfst.append(i)
                print(
                    f'#{i} SUPERFAST: {total_time}')
            elif total_time <= 3.00:
                fst.append(i)
                print(f'#{i} Fast: {total_time}')
            elif total_time <= 10.00:
                keep.append(i)
                print(f'#{i} Keep: {total_time}')
            elif total_time <= 15.00:
                meh.append(i)
                print(f'#{i} Decide: {total_time}')
            elif total_time <= 20.00:
                slw.append(i)
                print(f'#{i} Slow: {total_time}')
            else:
                snl.append(i)
                print(f'#{i} Snail: {total_time}')
        except:
            total_time = time.time()-start_time
            usls.append(i)
            print(f'#{i} Delete: {total_time}')
    
    all_proxs = {}
    all_proxs['superfast'] = sprfst
    all_proxs['fast'] = fst
    all_proxs['keep'] = keep
    all_proxs['decide'] = meh
    all_proxs['slow'] = slw
    all_proxs['snail'] = snl
    all_proxs['delete'] = usls
    
    return all_proxs


def zip_prop_count(zip_list, proxies, prp_list, ua, ezl):
    '''This will be used later to collect the number of properties per zip code.
    This will be necessary since the majority of the sites limit the number of 
    properties between 350 and 500 per search. If we find the number of properties 
    is more than the website will allow per search, we have to add an additional 
    filter (max sqft, price, etc.) to narrow the results per search. This runs well. 
    Not being used currently. This will be used to run feature importance when it 
    comes to pricing homes.'''

    proxy = random.sample(proxies, 1)[0]

    print(proxies.index(proxy))
    print(proxy)

    for num in zip_list:

        url = 'https://www.redfin.com/zipcode/' + \
            str(num) + '/filter/property-type=house+condo+townhouse,' + \
            'include=sold-1yr,min-price=20k,min-baths=1,include=sold-1yr'

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
    '''Once we start running the search, the search page displays only home's 
    basic features. This function collects homes information (home addresses 
    and home URLs) from the search result page.'''

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
    '''After collecting all the search page's URLs, this function runs each 
    URL and parses all homes address and URL from every single search page's.'''

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
