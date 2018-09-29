import time
import sys
import urllib
import time
import random
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.error import URLError
import requests
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

