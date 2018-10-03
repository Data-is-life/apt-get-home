#     all_home_feats = soup.findAll('div', {'class':"amenities-container"})
#     for num in all_home_feats:
#         print(num.findAll('li'))
# sdf = pd.DataFrame({'zip': ezl, 'sld': sold_prp_list})
# apdf = strip_count(ap_prp_count_list)
# apdf.to_csv('../Data/apdf.csv')
# sdf.to_csv('../Data/sdf.csv')

# apdf.index = ap_df['zip']
# sdf.index = sdf['zip']

# sdf['sld'] = (sdf['sld']).astype(int)
# apdf['num_ap_homes'] = (ap_df['num_ap_homes']).astype(int)

# sdf['zip'] = (sdf['zip']).astype(int)
# apdf['zip'] = (ap_df['zip']).astype(int)

# sld_pgs = [ceil(num/20) for num in sdf['sld']]
# ap_pgs = [ceil(num/20) for num in apdf['num_ap_homes']]

# sdf['pages'] = sld_pgs
# apdf['pages'] = ap_pgs

# sdf = sdf.sort_values(by='pages')
# apdf = apdf.sort_values(by='pages')

# sdf_under = sdf[sdf['pages'] <= 18]
# sdf_over = sdf[sdf['pages'] > 18]


# ap_url_list = []
# for num in zip_list:
#     num_pages_count = apdf.loc[apdf['zip'] == num].pages.values[0]
#     for i in range(1, num_pages_count+1):
#         url = 'https://www.redfin.com/zipcode/'+str(num) + \
#             '/filter/property-type=house+condo+townhouse,min-baths=1,status=active+pending+contingent/page-' + \
#             str(i)
#         ap_url_list.append(url)


# ap_url_list = [num.replace(r'/page-1^', '') for num in ap_url_list]
# ap_url_list = [num.replace('contingent0', 'contingent/page-10')
#                for num in ap_url_list]
# ap_url_list = [num.replace('contingent1', 'contingent/page-11')
#                for num in ap_url_list]
# ap_url_list = [num.replace('contingent2', 'contingent/page-12')
#                for num in ap_url_list]
# ap_url_list = [num.replace('contingent3', 'contingent/page-13')
#                for num in ap_url_list]

# main_df = pd.DataFrame(columns=['full_address', 'home_link'])

# ap_url_list = sorted(ap_url_list)
# print(ap_url_list)

# sld_under_url_list = []

# for num in sdf_under['zip']:
#     num_pages_count = sdf_under.loc[sdf_under['zip'] == num].pages.values[0]
#     for i in range(1, num_pages_count+1):
#         url = 'https://www.redfin.com/zipcode/'+str(num) + \
#             '/filter/property-type=house+condo+townhouse,min-price=100k,min-baths=1,include=sold-1yr/page-' + \
#             str(i)
#         sld_under_url_list.append(url)


# sld_under_url_list = [num.replace('/page-1', '') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr0', '=sold-1yr/page-10') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr1', '=sold-1yr/page-11') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr2', '=sold-1yr/page-12') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr3', '=sold-1yr/page-13') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr4', '=sold-1yr/page-14') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr5', '=sold-1yr/page-15') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr6', '=sold-1yr/page-16') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr7', '=sold-1yr/page-17') for num in sld_under_url_list]
# sld_under_url_list = [num.replace(
#     '=sold-1yr8', '=sold-1yr/page-18') for num in sld_under_url_list]

# s_main_df = pd.DataFrame(columns=['full_address', 'home_link'])

# sld_under_url_list = sorted(sld_under_url_list)
# print(len(sld_under_url_list))


#     other_home_feats = soup.findAll('span', {'data-rf-test-id':"propertyDetails"})
#     print(f'other_home_feats = {other_home_feats}')
#     other_home_feats_vals = soup.findAll('span', {'class':"content font-weight-roman"})
#     print(f'other_home_feats_vals = {other_home_feats_vals}')
# both are in soup.findAll('div', {'class':"keyDetail font-size-base"})

#     home_full_feat_desc = soup.findAll('span', {'class': 'statsLabel'})
#     for desc in home_full_feat_desc:
#         print(f'hffd = {desc}')
#         homefeat_desc.append(str(desc.contents[0]))

#     home_full_feat_info = soup.findAll('span', {'class': 'statsValue'})
#     for info in home_full_feat_info:
#         print(f'info = {info}')
#         homefeat_info.append(str(info.contents[0]))

#     school_grades = soup.findAll('div', {'class': 'nearby-schools-grades'})
#     for grade in school_grades:
#         print(grade.text)

#     school_assigned = soup.findAll(
#         'span', {'class': 'assigned-label zsg-fineprint'})

#     for assi in school_assigned:
#         print(assi.text)

#     school_dist = soup.findAll('div', {'class': 'nearby-schools-distance'})
#     for dist in school_dist:
#         print(dist.text)

#     school_rating = soup.findAll('div', {'class': 'nearby-schools-rating'})
#     for rating in school_rating:
#         print(rating.span.text)

#     school_name_regex = r'school-name notranslate$'
#     school_name = soup.findAll('a', {'class': 'school-name notranslate'})
#     for mane in school_name:
#         print(mane.next_element)

#     homefeat_desc = []
#     homefeat_info = []

#     new_dict = dict(zip(homefeat_desc, homefeat_info))
#     new_dict['address'] = str(home_address_MLS)

# #     new_dict['home_description'] = str(home_description.attrs['content'])

# lots of info:

#     estimate = soup.find('div', {'data-rf-test-name': 'avmValue"'})
#     print(f'estimate = {estimate}')

#     home_hist_src = soup.findAll('td', {'class': 'zsg-sm-hide'})
#     print(home_hist_src)

# rand_zip_list_ap = random.sample(zip_list, len(zip_list))
# ap_prp_count_list = []

# rand_zip_sld = random.sample(zip_list, len(zip_list))
# sold_prp_list = []
# ezl = []# sld_under_url_list = sld_under_url_list[1:]
# print(len(sld_under_url_list))
# sld_under_url_list, s_main_df = links_for_props(
#     proxies, sld_under_url_list, s_main_df, ua)
# list_ = list(s_main_df.full_address.values)
# set([num[-5:] for num in list_])
# main_df.to_csv('../Data/main_df_ap.csv')
# s_main_df.to_csv('../Data/s_main.csv')
# s_main_df = pd.read_csv('../Data/s_main.csv')
# main_df = pd.read_csv('../Data/main_df_ap.csv')

# ap_prp_count_list, rand_zip_list, proxies = zip_prop_count(rand_zip_list_ap, proxies, ap_prp_count_list, ua)
# sold_prp_list, rand_zip_sld, proxies, ezl = zip_prop_count(rand_zip_sld, proxies, sold_prp_list, ua, ezl)

# sold_prp_list = [str(num) for num in sold_prp_list]
# sold_prp_list = [num.replace(
#     '[<div class="homes summary" data-rf-test-id="homes-description"><span class="showingText">Showing </span>', '') for num in sold_prp_list]
# sold_prp_list = [num.replace(
#     ' Homes<span class="summarySeparator ">•</span></div>]', '') for num in sold_prp_list]
# sold_prp_list = [num.replace('20 of ', '') for num in sold_prp_list]


#     prop_hist = soup.findAll(
#         'div', {'id': 'propertyHistory-expandable-segment'})
#     prop_history = [num.text for num in prop_hist]


# sld_under_url_list = sld_under_url_list[1:]
# print(len(sld_under_url_list))
# sld_under_url_list, s_main_df = links_for_props(
#     proxies, sld_under_url_list, s_main_df, ua)
# list_ = list(s_main_df.full_address.values)
# set([num[-5:] for num in list_])
# main_df.to_csv('../Data/main_df_ap.csv')
# s_main_df.to_csv('../Data/s_main.csv')
# s_main_df = pd.read_csv('../Data/s_main.csv')
# main_df = pd.read_csv('../Data/main_df_ap.csv')
