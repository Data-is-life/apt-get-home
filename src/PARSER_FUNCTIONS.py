# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/01/2018

import re, ast, sys, random, string
import pandas as pd
from bs4 import BeautifulSoup
from random import randint

def top_info_parser(soup, _count):

    all_top = soup.findAll('div', {'class': 'HomeInfo inline-block'})
    
    top_info_dict = {}
    values_ = []
    cats_ = []
    sqft = []
    lat_lon = []
    
    for num in all_top:

        address_ = num.findAll('span', {'class': 'street-address'})
        top_info_dict['address'] = [num.text for num in address_][0]

        city_ = num.findAll('span', {'class': 'locality'})
        top_info_dict['city'] = [num.text for num in city_][0]

        state_ = num.findAll('span', {'class': 'region'})
        top_info_dict['state'] = [num.text for num in state_][0]

        zip_code_ = num.findAll('span', {'class': 'postal-code'})
        top_info_dict['zip_code'] = [num.text for num in zip_code_][0]
        
        red_est = num.findAll('div', {'class': 'info-block avm'})
        for i in red_est:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        price_ = num.findAll('div', {'class': 'info-block price'})
        for i in price_:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        bdrs_ = num.findAll('div', {'data-rf-test-id': 'abp-beds'})
        for i in bdrs_:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        bths_ = num.findAll('div', {'data-rf-test-id': 'abp-baths'})
        for i in bths_:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        sqft_ = num.findAll('div', {'data-rf-test-id': 'abp-sqFt'})
        for i in sqft_:
            top_info_dict['sqft'] = i.span.text[:6]

        yrblt_ = num.findAll('div', {'class': 'HomeBottomStats'})
        for i in yrblt_:
            lbls_ = i.findAll('span', {'class': 'label'})
            vals_ = i.findAll('span', {'class': 'value'})
            for j in lbls_:
                cats_.append(j.text)
            for k in vals_:
                values_.append(k.text)

        lat_lon_ = num.findAll('span', {'itemprop': 'geo'})
        for i in lat_lon_:
            ll_ = i.findAll('meta')
            for num in ll_:
                lat_lon.append(num['content'])

    if len(lat_lon)>=2:
        top_info_dict['latitude'] = lat_lon[0]
        top_info_dict['longitude'] = lat_lon[1]

    values_ = [num for num in values_ if num!='—']
    cats_ = [num for num in cats_ if num!='—']
    info_dict = dict(zip(cats_, values_))
    
    all_info_dict = {**top_info_dict, **info_dict}
    
    return pd.DataFrame(all_info_dict, index=[_count])


def public_info_parser(soup, _count):
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

    return pd.DataFrame(public_info_dict, index=[_count])



def school_parser(soup, _count):
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

    return pd.DataFrame(school_dict, index=[_count])



def feats_parser(soup, _count):

    all_home_feats = soup.findAll('span', {'class': "entryItemContent"})

    feat_cats = []
    feat_vals = []

    for num in all_home_feats:
        feat_cats.append(num.contents[0])
    for num in all_home_feats:
        feat_vals.append(num.span.text)

    cats_set = set(feat_cats)
    vals_set = set(feat_vals)
    redundant = cats_set & vals_set

    for num in redundant:
        feat_cats.remove(num)
        feat_vals.remove(num)

    feat_cats = [str(num) for num in feat_cats]
    feat_vals = [str(num) for num in feat_vals]

    df = pd.DataFrame(dict(zip(feat_cats, feat_vals)), index=[_count])

    return df