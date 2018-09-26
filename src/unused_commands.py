from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys




areas_pool = random.sample(areas, len(areas))
ua_pool = random.sample(ua, len(ua))
ap_prop_list = []
sold_prop_list = []

for num in areas_pool:
    sold_url = 'https://www.zillow.com/homes/recently_sold/'+num +'/house,condo,apartment_duplex,townhouse_type/1-_baths/20000-_price/82-_mp/12m_days/1_pnd/globalrelevanceex_sort/'
    ap_url = 'https://www.zillow.com/homes/for_sale/'+num +'/house,condo,apartment_duplex,townhouse_type/1-_baths/20000-_price/82-_mp/globalrelevanceex_sort/0_mmm/'
    proxy = random.sample(proxies, 1)[0]
    print(proxy)
    header = random.sample(ua, 1)[0]
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}
    req_ap = session.get(ap_url, headers=header)
    soup_ap = BeautifulSoup(req_ap.text, 'html.parser')
    ap_count = soup_ap.findAll('meta', {'name': 'description'})
    print(ap_count)
    ap_prop_list.append(ap_count)
    req_sold = session.get(sold_url, headers=header)
    soup_sold = BeautifulSoup(req_sold.text, 'html.parser')
    sold_count = soup_sold.findAll('title', text=re.compile(r'd+'))
    print(sold_count)
    sold_prop_list.append(sold_count)
    areas_pool.remove(num)
    print(len(areas_pool))
    print(len(ap_prop_list))
    print(len(sold_prop_list))

def strip_count_sold(lst):
    lst = [str(num) for num in lst]
    lst = [num.replace('[<title>Recently ', '') for num in lst]
    lst = ap_prop_list = [num.replace(
        ' Transactions | Zillow</title>]', '') for num in lst]
    lst = list(set(lst))
    return lst

ap_prop_list = strip_count_ap(ap_prop_list)
sold_prop_list = strip_count_sold(sold_prop_list)

# ap_prop_list = [str(num) for num in ap_prop_list]
# ap_prop_list = [num.replace('[<meta content="Zillow has ', '')
#                 for num in ap_prop_list]
# ap_prop_list = [num.replace(
#     '. View listing photos, review sales history, and use our detailed real estate filters to find the perfect place." name="description"/>]', '')
#                 for num in ap_prop_list]
# ap_prop_list = list(set(ap_prop_list))


re_ap_num = r"\d+\s"
re_ap_zip = r"\s\d+"

num_active_homes = []
zip_active_homes = []

for num in ap_prop_list:
    num_active_homes.append(re.findall(re_ap_num, num))
    zip_active_homes.append(re.findall(re_ap_zip, num))

num_active_homes = [[int(y) for y in x] for x in num_active_homes]
zip_active_homes = [[int(y) for y in x] for x in zip_active_homes]

num_ap_homes = []
zip_ap_homes = []

i = 0
while i < len(ap_prop_list):
    num_ap_homes.extend(num_active_homes[i])
    zip_ap_homes.extend(zip_active_homes[i])
    i += 1

df_ap = pd.DataFrame({"ap": num_ap_homes}, index=zip_ap_homes)

num_sold_homes = []
zip_sold_homes = []

re_sold_zip = r"\d+\s"
re_sold_num = r"\-\s\d+"

for num in sold_prop_list:
    num_sold_homes.append(re.findall(re_sold_num, num))
    zip_sold_homes.append(re.findall(re_sold_zip, num))

num_sold_homes = [[y.replace('- ', '') for y in x] for x in num_sold_homes]
num_sold_homes = [[int(y) for y in x] for x in num_sold_homes]
zip_sold_homes = [[int(y) for y in x] for x in zip_sold_homes]

num_sl_homes = []
zip_sl_homes = []

i = 0
while i < len(num_sold_homes):
    num_sl_homes.extend(num_sold_homes[i])
    zip_sl_homes.extend(zip_sold_homes[i])
    i += 1

df_sold = pd.DataFrame({"sold": num_sl_homes}, index=zip_sl_homes)

total_count = pd.concat([df_ap, df_sold], axis=1)
total_count.to_csv('prop_count.csv')

ap_pages = [ceil(num/25) for num in total_count['ap']]
sold_pages = [ceil(num/25) for num in total_count['sold']]

total_count['ap_pages'] = ap_pages
total_count['sold_pages'] = sold_pages

all_info = pd.concat([zip_codes, total_count], axis=1)

all_info['tot'] = all_info['ap']+all_info['sold']

tot_pages = [ceil(num/25) for num in all_info['tot']]
all_info['tot_pages'] = tot_pages

all_info.sort_values(by=['tot'])

#     latitude_soup = soup.findAll('meta', {'itemprop': 'latitude'})
#     latitude = [str(lttds['content']) for lttds in latitude_soup]

#     longitude_soup = soup.findAll('meta', {'itemprop': 'longitude'})
#     longitude = [str(lngts['content']) for lngts in longitude_soup]

# proxy = random.sample(proxies, 1)[0]
# print(proxy)
# data = each_page('https://www.zillow.com/homes/for_sale/Milpitas-CA-95035/fsba,fore,new,cmsn_lt/house,condo,apartment_duplex,townhouse_type/1-_baths/20000-_price/82-_mp/12m_days/1_pnd/pricea_sort/1_rs/', ua_pool, proxy)
# print(data)


# proxy = random.sample(proxies, 1)[0]
# print(proxy)
# for num in areas_pool:
#     num_pages_count = areas_un_five_df.loc[areas_un_five_df['name'] == num].all_pages.values[0]
#     print(num_pages_count)
#     print(num)
#     for i in range(1,num_pages_count+1):
#         print(i)
#         url = 'https://www.zillow.com/homes/for_sale/'+num+'/fsba,fore,new,cmsn_lt/house,condo,apartment_duplex,townhouse_type/1-_baths/20000-_price/82-_mp/12m_days/1_pnd/pricea_sort/'+str(i)+'_p/1_rs/'
#         data = each_page(url, ua_pool, proxy)
#         df = pd.DataFrame(data)
#         main_df = pd.concat([main_df,df])
#     areas_pool.remove(num)


def get_info(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(randint(5,10))
    num_listings = driver.find_element_by_id('map-result-count-message')
    count_listings = num_listings.text
    time.sleep(randint(5,10))
    driver.quit()
    return count_listings
#     num_listings = driver.find_element_by_id('map-result-count-message')
#     driver.
#     return num_listings
firefox_profile = FirefoxProfile('/home/guess/.mozilla/firefox/gbdaydal.default')
driver = webdriver.Firefox()
driver.get('https://www.zillow.com/homedetails/42983-Charleston-Way-Fremont-CA-94538/25041042_zpid/?fullpage=true')
driver.implicitly_wait(1)
fields = driver.find_elements_by_class_name('fact-label')

driver = webdriver.Firefox()
for num in areas:
    sold_url = 'https://www.zillow.com/homes/recently_sold/'+num + \
        '/house,condo,apartment_duplex,townhouse_type/1-_baths/20000-_price/82-_mp/6m_days/1_pnd/globalrelevanceex_sort/'
    ap_url = 'https://www.zillow.com/homes/for_sale/'+num + \
        '/house,condo,apartment_duplex,townhouse_type/1-_baths/20000-_price/82-_mp/globalrelevanceex_sort/0_mmm/'
    driver.get(sold_url)
    time.sleep(randint(8, 10))
    num_s_listings = driver.find_element_by_id('map-result-count-message')
    total_s_listings = int(re.findall(r'\d+', num_s_listings.text)[0])
    num_pages = ceil(total_listings/25)
    for num in range(2, num_pages+1):
        p_url = 'sold_url'+num+'_p/'
    sold.append(total_s_listings)
    driver.get(ap_url)
    time.sleep(randint(4, 8))
    num_ap_listings = driver.find_element_by_id('map-result-count-message')
    total_ap_listings = int(re.findall(r'\d+', num_ap_listings.text)[0])
    num_pages = ceil(total_listings/25)
    for num in range(2, num_pages+1):
        p_url = 'sold_url'+num+'_p/'
    time.sleep(randint(5, 12))
    ap.append(total_ap_listings)
    driver.quit()

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import _thread
import time


def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    return bs.find('div', {'id': 'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$'))
# Define a function for the thread


def scrape_article(thread_name, path):
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    time.sleep(5)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    print('Scraping {} in thread {}'.format(title, thread_name))
    links = get_links(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        scrape_article(thread_name, newArticle)


# Create two threads as follows
try:
    _thread.start_new_thread(
        scrape_article, ('Thread 1', '/wiki/Kevin_Bacon',))
    _thread.start_new_thread(
        scrape_article, ('Thread 2', '/wiki/Monty_Python',))
except:
    print('Error: unable to start threads')
while 1:
    pass