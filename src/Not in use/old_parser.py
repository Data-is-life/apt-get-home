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

        money_ = num.findAll('div', {'class': 'statsValue'})
        home_vals = [num.text for num in money_]

        price_cat_1 = num.findAll('div', {'class': 'avmLabel'})
        price_cats = [num.text for num in price_cat_1]

        price_cat_2 = num.find('div', {'class': 'statsLabel'})
        price_cats = [price_cats.extend(num.text) for num in price_cat_2]

        price_dict = dict(zip(price_cats, price_vals))

        home_lat = 

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
