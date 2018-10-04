# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/01/2018

import re, ast, sys, random, string
import pandas as pd
from bs4 import BeautifulSoup
from random import randint


def address_parser(soup, i):

    home_dict = dict()

    home_address_MLS = soup.title.string

    add_list = home_address_MLS.split(sep=' |')
    zip_code = re.search('\d+$', add_list[0])
    home_add = re.search('(.+?),', home_address_MLS)
    home_city = re.search(',(.+?),', home_address_MLS)
    home_state = re.search('\s\b\w\w\b\s', add_list[0])
#     .replace(home_add.group(1), '').replace(
#         home_city.group(1), '').replace(zip_code.group(), '').replace(
#         ',', '').replace(' ', '')

    home_dict['address'] = home_add.group(1)
    home_dict['city'] = home_city.group(1)
    home_dict['zip_code'] = zip_code.group()
    home_dict['state'] = home_state

    home_description = soup.find('p', {'class': 'font-b1'})
    if home_description != None:
        home_dict['description'] = home_description.span.text
    else:
    	home_dict['description'] = 'N/A'

    if len(add_list) >= 2:
        mls_num = re.search('\d+$', add_list[1])

        if mls_num != None:
            home_dict['mls_num'] = mls_num.group()
    else:
        home_dict['mls_num'] = 'N/A'

    return pd.DataFrame(home_dict, index=[i])



def top_info_parser(soup):

    all_top = soup.findAll('div', {'class': 'HomeInfo inline-block'})



    for num in all_top:

        address_ = num.findAll('span', {'class': 'street-address'})
        home_dict['address'] = [num.text for num in address_][0]

        city_ = num.findAll('span', {'class': 'locality'})
        home_dict['city'] =  [num.text for num in city_][0]

        state_ = num.findAll('span', {'class': 'region'})
        home_dict['state'] = [num.text for num in state_][0]

        zip_code_ = num.findAll('span', {'class': 'postal-code'})
        home_dict['zip_code'] = [num.text for num in zip_code_][0]

        
        price_cats = []

        money_ = num.findAll('div', {'class': 'statsValue'})
        price_vals = [num.text for num in money_]


        price_cat_1 = num.findAll('div', {'class': 'avmLabel'})
        price_cats = [num.text for num in price_cat_1]

        price_cat_2 = num.find('div', {'class': 'statsLabel'})
        price_cats = [num.text for num in price_cat_1]

            home_dict['address'] = num.text
        home_dict['city'] = home_city.group(1)
        home_dict['zip_code'] = zip_code.group()
        home_dict['state'] = home_state
        cats = num.findAll('span', {'class': 'table-label'})
        for i in cats:
            label_list.append(i.text)

    for num in all_info:
        vals = num.findAll('div', {'class': 'table-value'})
        for i in vals:
            values_list.append(i.text)

    public_info_dict = dict(zip(label_list, values_list))

    return pd.DataFrame(public_info_dict, index=[i])

    # price_regex = r'\$\S+\s+'
    # bed_regex = r'\d+\S?\d?\d?Bed'
    # bath_regex = r'\d+\S?\d?\d?Bath'
    # size_regex = r'\d+\S?\d?\d?\s?Sq'
    # yr_blt_regex = r'Built: \d+'
    # status_regex = r'Status: \w+'

    # top_info_dict = dict()
    # price_list = []

    
    print (all_top)

    for num in all_top:
        a = num.text

        num_beds = re.findall(bed_regex, a)
        num_baths = re.findall(bath_regex, a)
        home_sqft = re.findall(size_regex, a)
        yr_blt = re.findall(yr_blt_regex, a)
        status = re.findall(status_regex, a)

        if num_beds != None:
            top_info_dict['num_beds'] = float(num_beds[0].replace(
                'Bed', '').replace(' ', ''))

        if num_baths != None:
            top_info_dict['num_baths'] = float(num_baths[0].replace(
                'Bath', '').replace(' ', ''))

        if home_sqft != None:
            top_info_dict['home_sqft'] = float(home_sqft[0].replace(
                'Sq', '').replace(' ', '').replace(':', ''))

        if yr_blt != None:
            top_info_dict['yr_blt'] = int(yr_blt[0].replace(
                'Built', '').replace(' ', '').replace(':', ''))

        if status != None:
            top_info_dict['status'] = status[0].replace(
                'Status', '').replace(' ', '').replace(':', '')

        price_list.extend(re.findall(price_regex, a))

        if len(price_list) >= 2:
            top_info_dict['redfin_est'] = float([
                num for num in price_list if 'Redfin' in num][0].replace(
                'Redfin ', '').replace('$', '').replace(',', ''))
            top_info_dict['sold_price'] = float([
                num for num in price_list if 'Last' in num][0].replace(
                'Last ', '').replace('$', '').replace(',', ''))

        elif len(price_list) >= 1:
            top_info_dict['sold_price'] = float([
                num for num in price_list if 'Last' in num][0].replace(
                'Last ', '').replace('$', '').replace(',', ''))
        else:
            top_info_dict['redfin_est'] = 'N/A'
            top_info_dict['sold_price'] = 'N/A'

    return pd.DataFrame(top_info_dict, index=[i])


def public_info_parser(soup, i):
    all_info = soup.findAll('div', {'data-rf-test-id': 'publicRecords'})

    label_list = []
    values_list = []

    for num in all_info:
        cats = num.findAll('span', {'class': 'table-label'})
        for i in cats:
            label_list.append(i.text)

    for num in all_info:
        vals = num.findAll('div', {'class': 'table-value'})
        for i in vals:
            values_list.append(i.text)

    public_info_dict = dict(zip(label_list, values_list))

    return pd.DataFrame(public_info_dict, index=[i])



def school_parser(soup, i):
    school_dict = dict()
    school_info = soup.findAll('div', {'class': "name-and-info"})
    schools = [num.text for num in school_info]

    if ('Public') in schools[0]:
        es = schools[0]
        elementary_school = es.split(sep=' •')
        school_dict['elem_school_name'] = elementary_school[0][:-6]
        school_dict['elem_school_grades'] = elementary_school[1]
        school_dict['elem_school_rating'] = re.findall(
            '(\d+)', elementary_school[2])[0]

    elif ((len(schools) >= 2 and 'public' in schools[1])):
        es = schools[1]
        elementary_school = es.split(sep=' •')
        school_dict['elem_school_name'] = elementary_school[0][:-6]
        school_dict['elem_school_grades'] = elementary_school[1]
        school_dict['elem_school_rating'] = re.findall(
            '(\d+)', elementary_school[2])[0]
    else:
        school_dict['elem_school_name'] = 'N/A'
        school_dict['elem_school_grades'] = 'N/A'
        school_dict['elem_school_rating'] = 'N/A'

    if ((len(schools) >= 2 and 'public' in schools[1]) and (
        'Middle' or 'Junior') in schools[1]):
        middle_school = ms.split(sep=' •')
        school_dict['middle_school_name'] = middle_school[0][:-6]
        school_dict['middle_school_grades'] = middle_school[1]
        school_dict['middle_school_rating'] = re.findall(
            '(\d+)', middle_school[2])[0]
    elif ((len(schools) >= 3 and 'public' in schools[2]) and (
        'Middle' or 'Junior') in schools[2]):
        middle_school = ms.split(sep=' •')
        school_dict['middle_school_name'] = middle_school[0][:-6]
        school_dict['middle_school_grades'] = middle_school[1]
        school_dict['middle_school_rating'] = re.findall(
                        '(\d+)', middle_school[2])[0]
    else:
        school_dict['middle_school_name'] = 'N/A'
        school_dict['middle_school_grades'] = 'N/A'
        school_dict['middle_school_rating'] = 'N/A'

    if ((len(schools) >= 3 and ('9 to 12') in schools[2]) and 'public' in schools[2]):
        high_school = hs.split(sep=' •')
        school_dict['high_school_name'] = high_school[0][:-6]
        school_dict['high_school_grades'] = high_school[1]
        school_dict['high_school_rating'] = high_school[2]
    elif ((len(schools) >= 4 and ('9 to 12') in schools[3]) and 'public' in schools[3]):
        hs = schools[3]
        high_school = hs.split(sep=' •')
        school_dict['high_school_name'] = high_school[0][:-6]
        school_dict['high_school_grades'] = high_school[1]
        school_dict['high_school_rating'] = high_school[2]
    else:
        school_dict['high_school_name'] = 'N/A'
        school_dict['high_school_grades'] = 'N/A'
        school_dict['high_school_rating'] = 'N/A'

    return pd.DataFrame(school_dict, index=[i])



def feats_parser(soup, i):

    all_home_feats = soup.findAll('span', {'class': "entryItemContent"})

    feat_cats = []
    feat_vals = []

    for num in all_home_feats:
        feat_cats.append(num.contents[0])
    for num in all_home_feats:
        feat_vals.append(num.span)

    cats_set = set(feat_cats)
    vals_set = set(feat_vals)
    redundant = cats_set & vals_set

    for num in redundant:
        feat_cats.remove(num)
        feat_vals.remove(num)

    feat_cats = [str(num) for num in feat_cats]
    feat_vals = [str(num.text) for num in feat_vals]

    df = pd.DataFrame(dict(zip(feat_cats, feat_vals)), index=[i])

    return df


























# def gen_sold_prop_info(url, hdr, proxy):


#     price_regex = r'\$\S+\s+'
#     bed_regex = r'\d+\S?\d?\d?Bed'
#     bath_regex = r'\d+\S?\d?\d?Bath'
#     size_regex = r'\d+\S?\d?\d?\s?Sq'
#     yr_blt_regex = r'Built: \d+'
#     status_regex = r'Status: \w+'
#     home_dict = dict()

#     home_address_MLS = soup.title.string
#     add_list = text.split(sep=' |')
#     zip_code = re.search('\d+$', add_list[0])
#     mls_num = re.search('\d+$', add_list[1])
#     home_add = re.search('(.+?),', home_address_MLS)
#     home_city = re.search(',(.+?),', home_address_MLS)
#     home_state = add_list[0].replace(home_add.group(1), '').replace(
#         home_city.group(1), '').replace(zip_code.group(), '').replace(
#         ',', '').replace(' ', '')

#     home_dict['address'] = home_add.group(1)
#     home_dict['city'] = home_city.group(1)
#     home_dict['zip_code'] = zip_code.group()
#     home_dict['state'] = home_state
#     home_dict['mls_num'] = mls_num.group()

#     all_top = soup.findAll('div', {'class': 'HomeInfo inline-block'})
#     price_list = []
#     for num in all_top:
#         a = num.text
#         price_list.extend(re.findall(price_regex, a))
#         home_dict['num_beds'] = (re.findall(bed_regex, a))
#         home_dict['num_baths'] = (re.findall(bath_regex, a))
#         home_dict['home_sqft'] = (re.findall(size_regex, a))
#         home_dict['yr_blt'] = (re.findall(yr_blt_regex, a))
#         home_dict['status'] = (re.findall(status_regex, a))

#     home_dict['redfin_est'] = [num for num in price_list if 'Redfin' in num]
#     home_dict['sold_price'] = [num for num in price_list if 'Last' in num]

#     home_description = soup.find('p', {'class': 'font-b1'})
#     home_dict['description'] = home_description.span.text

#     all_home_feats = soup.findAll('span', {'class': "entryItemContent"})
#     feats = [num.text for num in all_home_feats]

#     # prop_hist = soup.findAll(
#     #     'div', {'id': 'propertyHistory-expandable-segment'})
#     # prop_history = [num.text for num in prop_hist]

#     school_info = soup.findAll('div', {'class': "name-and-info"})
#     schools = [num.text for num in school_info]

#     return home_dict, feats, prop_history, schools
