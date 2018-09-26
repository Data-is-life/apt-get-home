from lxml.html import fromstring
import requests
import time
import traceback
import random

proxies = ['12.2.202.242:8080', '24.148.73.79:8080',
           '50.224.173.179:8080', '50.237.58.161:31468',
           '50.242.47.41:31128', '52.144.107.142:35569', 
           '64.49.66.69:34776', '64.125.223.19:55577', 
           '64.125.223.19:55577', '70.183.205.174:33721', 
           '72.35.40.34:8080', '75.172.104.143:48002', 
           '96.95.154.205:39668', '98.150.241.216:8080', 
           '107.165.144.125:45931', '140.227.60.114:3128', 
           '144.202.62.109:8000', '173.164.26.117:3128', 
           '184.177.165.96:44134', '198.52.8.50:55626', 
           '216.241.207.246:57080', '207.144.111.230:8080']

url = 'https://httpbin.org/ip'
default_list = []

for i in range(0,len(proxies)):
    #Get a proxy from the pool
    proxy = proxies[i]
    print(i+1)
    start_time = time.time()
    print(start_time)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
        print(time.time() - start_time)
    except:
        print("Skipping. Connnection error")
        default_list.append(i+1)
        print(time.time() - start_time)