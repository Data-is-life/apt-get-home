# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/01/2018

import re
import pandas as pd


def rename_columns(strs_to_replace):
    '''Keeping Dataframe heading formating consistant by converting all values
    to standardized format that is easy to trace back. If left unformatted,
    there could be duplicate columns with the same values and it would make it
    far more challenging to search for homes.'''

    modified_list = []

    for num in strs_to_replace:
        modified_list.append(num.replace('Redfin Estimate', 'redfin_est'
                                         ).replace(
            'Beds', 'num_bdrs').replace('beds', 'num_bts').replace(
            'Baths', 'num_bts').replace('$', 'price').replace(
            'Built: ', 'yr_blt').lower().replace('__', '_').replace(
            ' ', '_').replace(':_', '').replace(':', '').replace(
            '.', '').replace('sqft', 'sq_ft').replace('_(', '_').replace(
            '(', '_').replace(')', '').replace(',', '').replace(
            'minimum', 'min').replace('maximum', 'max').replace(
            'bedrooms', 'beds').replace('bathrooms', 'baths').replace(
            '#_of_', 'num_').replace('sq. ft.', 'sqft'))

    return modified_list


def top_info_parser(soup):
    '''Starting with getting the information at the very top of the page.
    This takes information from the top of the page that highlights the main
    attributes of the home, including latitude and longitude.'''

    all_top = soup.findAll('div', {'class': 'HomeInfo inline-block'})

    top_info_dict = {}
    values_ = []
    cats_ = []
    sqft = []
    lat_lon = []

    for num in all_top:

        # Getting the address
        address_ = num.findAll('span', {'class': 'street-address'})
        top_info_dict['address'] = [num.text for num in address_][0]

        # Getting the city
        city_ = num.findAll('span', {'class': 'locality'})
        top_info_dict['city'] = [num.text for num in city_][0]

        # Getting the state (maybe not needed?)
        state_ = num.findAll('span', {'class': 'region'})
        top_info_dict['state'] = [num.text for num in state_][0]

        # Getting the zip-code
        zip_code_ = num.findAll('span', {'class': 'postal-code'})
        top_info_dict['zip_code'] = [num.text for num in zip_code_][0]

        '''Getting the Redfin Estimate. This is important, since if the home
        was sold a few months ago, the search should focus on the homes current
        value and not for what it sold for. This make the results far more
        efficiant.'''
        red_est = num.findAll('div', {'class': 'info-block avm'})
        for i in red_est:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        # If the Redfin estimate is not available, this is the fall back option.
        price_ = num.findAll('div', {'class': 'info-block price'})
        for i in price_:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        # Getting number of bedrooms
        bdrs_ = num.findAll('div', {'data-rf-test-id': 'abp-beds'})
        for i in bdrs_:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        # Getting number of bathrooms
        bths_ = num.findAll('div', {'data-rf-test-id': 'abp-baths'})
        for i in bths_:
            values_.append(i.div.text)
            cats_.append(i.span.text)

        # Getting size of the home
        sqft_ = num.findAll('div', {'data-rf-test-id': 'abp-sqFt'})
        for i in sqft_:
            top_info_dict['sqft'] = i.span.text[:6]

        # Getting the year the home was built in
        yrblt_ = num.findAll('div', {'class': 'HomeBottomStats'})
        for i in yrblt_:
            lbls_ = i.findAll('span', {'class': 'label'})
            vals_ = i.findAll('span', {'class': 'value'})
            for j in lbls_:
                cats_.append(j.text)
            for k in vals_:
                values_.append(k.text)

        # Getting latitude and longitude of the home
        lat_lon_ = num.findAll('span', {'itemprop': 'geo'})
        for i in lat_lon_:
            ll_ = i.findAll('meta')
            for num in ll_:
                lat_lon.append(num['content'])

    if len(lat_lon) >= 2:
        top_info_dict['latitude'] = lat_lon[0]
        top_info_dict['longitude'] = lat_lon[1]

    # Checking to make sure the values are present for the fields
    # If they are not avaialble, get rid of them.
    values_ = [num for num in values_ if num != '—']
    cats_ = [num for num in cats_ if num != '—']

    # Putting everything in a dictionary, since it removes redundant columns
    info_dict = dict(zip(cats_, values_))

    # Merging the two dictionaries
    all_info_dict = {**top_info_dict, **info_dict}

    # Getting the home description
    home_description = soup.find('p', {'class': 'font-b1'})
    if home_description is not None:
        all_info_dict['description'] = home_description.span.text
    else:
        all_info_dict['description'] = 'N/A'

    return all_info_dict


def public_info_parser(soup):
    '''Getting information from tax sources to ensure all the home information
    matches from Zillow, Agent, and Tax records.'''

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

    return public_info_dict


def school_parser(soup):
    ''' Getting schools and the grades they attend with their score from
    GreatSchools this will be added as a feature for homes bigger than
    three bedrooms and all single family homes.'''

    school_dict = {}
    school_info = soup.findAll('div', {'class': "name-and-info"})
    school_names = []
    school_grades = []
    school_ratings = []
    for num in school_info:
        s_name = num.findAll('div', {'data-rf-test-name': 'school-name'})
        s_grade = num.findAll('div', {'class': re.compile('^sub-info')})
        s_rating = num.findAll('div', {'class': 'gs-rating-row'})
        for i in s_name:
            school_names.append(i.text)
        for j in s_grade:
            school_grades.append(j.text.replace(
                ' • Serves this home', '').replace(' • ', ' - '))
        for k in s_rating:
            school_ratings.append(
                k.text[-5:].replace(' ', '').replace('/10', ''))

    w = 0
    while w < len(school_names):
        if ('Public' in school_grades[w] and ((
                ('k' in school_grades[w] or 'Pre' in school_grades)
                or '5' in school_grades[w]) or 'Elementary' in school_names[w])):
            school_dict['elem_school_name'] = school_names[w]
            school_dict['elem_school_grades'] = school_grades[
                w].split(' - ', 1)[1]
            school_dict['elem_school_rating'] = school_ratings[w]
            w += 1
        else:
            w += 1

    w = 0
    while w < len(school_names):
        if ('Public' in school_grades[w] and ((
                ('7' in school_grades[w] or '8' in school_grades)
                or 'Middle' in school_names[w]) or 'Junior' in school_names[w])):
            school_dict['middle_school_name'] = school_names[w].title()
            school_dict['middle_school_grades'] = school_grades[
                w].split(' - ', 1)[1].title()
            school_dict['middle_school_rating'] = school_ratings[w].title()
            w += 1
        else:
            w += 1

    w = 0
    while w < len(school_names):
        if ('Public' in school_grades[w] and (
                ('12' in school_grades or 'High' in school_names[w]))):
            school_dict['high_school_name'] = school_names[w].title()
            school_dict['high_school_grades'] = school_grades[
                w].split(' - ', 1)[1].title()
            school_dict['high_school_rating'] = school_ratings[w].title()
            w += 1
        else:
            w += 1

    if 'elem_school_name' not in school_dict.keys():
        school_dict['elem_school_name'] = 'N/A'
        school_dict['elem_school_grades'] = 'N/A'
        school_dict['elem_school_rating'] = 'N/A'

    if 'middle_school_name' not in school_dict.keys():
        school_dict['middle_school_name'] = 'N/A'
        school_dict['middle_school_grades'] = 'N/A'
        school_dict['middle_school_rating'] = 'N/A'

    if 'high_school_name' not in school_dict.keys():
        school_dict['high_school_name'] = 'N/A'
        school_dict['high_school_grades'] = 'N/A'
        school_dict['high_school_rating'] = 'N/A'

    return school_dict


def feats_parser(soup):
    '''All the listed features by the agent/broker inputting the listing
    on the MLS.'''

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

    feats_dict = dict(zip(feat_cats, feat_vals))

    extra_feats = []

    for k, v in feats_dict.items():
        if 'span>' in k:
            extra_feats.append(k)

    for num in extra_feats:
        if num in feats_dict.keys():
            feats_dict.pop(num)

    # This is to replace all the HTML tags
    extra_feats = [num.replace('<span>', '').replace('</span>', '').replace(
        '<a href=', '').replace('"', '').replace(' rel=nofollow', '').replace(
        ' target=_blank>', '').replace('Virtual Tour (External Link)', '').replace(
        '</a', '').replace('>', '').replace('&amp;', '&').replace('(s)', '') for num
        in extra_feats]

    x_feat_string = ', '.join([num for num in extra_feats])
    x_feat_string = x_feat_string.split(sep=', ')
    x_feat_list = list(set(x_feat_string))

    feats_dict['extra_feats'] = ', '.join([num for num in x_feat_list])

    return feats_dict


def additional_info(soup):
    '''Need to get additional information, so we don't miss anything that
    could prove to be critical later.'''

    cats_ = soup.findAll('span', {'class': re.compile('^header ')})
    cats_ = [num.text for num in cats_]
    vals_ = soup.findAll('span', {'class': re.compile('^content ')})
    vals_ = [num.text for num in vals_]

    cats_ = [str(num).replace('Property Type', 'prop_type').replace(
        'HOA Dues', 'hoa_fees').replace('Type', 'prop_type') for num in cats_]
    vals_ = [str(num).replace('$', '').replace('/month', '').replace(
        'Hi-Rise', 'Condo').replace('Residential', 'Single Family Residence')
        for num in vals_]

    return dict(zip(cats_, vals_))


def info_from_property(soup):
    ''' Putting all the information together in a Dataframe and removing any
    duplicate columns.'''

    top_info_dict = top_info_parser(soup)
    public_info_dict = public_info_parser(soup)
    school_dict = school_parser(soup)
    all_home_feats = feats_parser(soup)
    mid_info_feats = additional_info(soup)

    df1 = pd.DataFrame(top_info_dict, index=[1])
    df2 = pd.DataFrame(public_info_dict, index=[1])
    df3 = pd.DataFrame(school_dict, index=[1])
    df4 = pd.DataFrame(all_home_feats, index=[1])
    df5 = pd.DataFrame(mid_info_feats, index=[1])

    df = pd.DataFrame()
    df = pd.concat([df1, df2, df3, df4, df5], axis=1)

    df.columns = rename_columns(df.columns)

    all_dict = df.to_dict()
    new_df = pd.DataFrame(all_dict)

    return new_df
