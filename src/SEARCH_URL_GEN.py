# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/02/2018

import re


def search_url_part_two_gen(type_home):

    #(type_home == re.compile('^Condo') or type_home == re.compile('^Town')):
    if (re.match('Condo', type_home) != None or re.match('Town', type_home) != None):
        url = 'property-type=condo+townhouse'
    # type_home == re.compile('^Single'):
    elif re.match('Single', type_home) != None:
        url = 'property-type=house'
    else:
        url = ''

    return url


def search_url_part_three_gen(price):

    if price <= 49999:
        url = 'max-price=75k'
    elif price <= 74999:
        url = 'max-price=125k'
    elif price <= 99999:
        url = 'min-price=50k,max-price=125k'
    elif price <= 124999:
        url = 'min-price=75k,max-price=150k'
    elif price <= 149999:
        url = 'min-price=100k,max-price=200k'
    elif price <= 174999:
        url = 'min-price=125k,max-price=225k'
    elif price <= 199999:
        url = 'min-price=150k,max-price=250k'
    elif price <= 224999:
        url = 'min-price=150k,max-price=275k'
    elif price <= 249999:
        url = 'min-price=200k,max-price=325k'
    elif price <= 274999:
        url = 'min-price=225k,max-price=350k'
    elif price <= 299999:
        url = 'min-price=225k,max-price=375k'
    elif price <= 324999:
        url = 'min-price=250k,max-price=400k'
    elif price <= 349999:
        url = 'min-price=275k,max-price=400k'
    elif price <= 374999:
        url = 'min-price=300k,max-price=450k'
    elif price <= 399999:
        url = 'min-price=325k,max-price=475k'
    elif price <= 424999:
        url = 'min-price=350k,max-price=500k'
    elif price <= 449999:
        url = 'min-price=375k,max-price=500k'
    elif price <= 474999:
        url = 'min-price=400k,max-price=550k'
    elif price <= 499999:
        url = 'min-price=425k,max-price=575k'
    elif price <= 549999:
        url = 'min-price=500k,max-price=625k'
    elif price <= 599999:
        url = 'min-price=475k,max-price=675k'
    elif price <= 649999:
        url = 'min-price=550k,max-price=725k'
    elif price <= 699999:
        url = 'min-price=600k,max-price=775k'
    elif price <= 749999:
        url = 'min-price=650k,max-price=850k'
    elif price <= 799999:
        url = 'min-price=700k,max-price=900k'
    elif price <= 849999:
        url = 'min-price=725k,max-price=950k'
    elif price <= 899999:
        url = 'min-price=750k,max-price=1M'
    elif price <= 999999:
        url = 'min-price=850k,max-price=1.25M'
    elif price <= 1249999:
        url = 'min-price=900k,max-price=1.5M'
    elif price <= 1499999:
        url = 'min-price=950k,max-price=2M'
    elif price <= 1749999:
        url = 'min-price=1.25M,max-price=2.25M'
    elif price <= 1999999:
        url = 'min-price=1.5M,max-price=2.5M'
    elif price <= 2249999:
        url = 'min-price=1.5M,max-price=2.75M'
    elif price <= 2499999:
        url = 'min-price=1.75M,max-price=3.25M'
    elif price <= 2749999:
        url = 'min-price=2M,max-price=3.25M'
    elif price <= 2999999:
        url = 'min-price=2.25M,max-price=3.5M'
    elif price <= 3249999:
        url = 'min-price=2.75M,max-price=3.75M'
    elif price <= 3499999:
        url = 'min-price=3M,max-price=4.25M'
    elif price <= 3749999:
        url = 'min-price=3.25M,max-price=4.5M'
    elif price <= 3999999:
        url = 'min-price=3.25M,max-price=5M'
    elif price <= 4249999:
        url = 'min-price=3.25M,max-price=6M'
    elif price <= 4999999:
        url = 'min-price=3.5M,max-price=6M'
    elif price <= 5249999:
        url = 'min-price=4.25M,max-price=7M'
    elif price <= 6999999:
        url = 'min-price=4.5M,max-price=10M'
    elif price <= 7999999:
        url = 'min-price=5M'
    elif price <= 12000000:
        url = 'min-price=6M'
    elif price > 12000000:
        url = 'min-price=7M'
    else:
        url = ''

    return url


def search_url_part_four_gen(num_bds):

    if num_bds <= 0:
        url = 'max-beds=1'
    elif num_bds <= 1:
        url = 'max-beds=2'
    elif num_bds <= 2:
        url = 'min-beds=1,max-beds=3'
    elif num_bds <= 3:
        url = 'min-beds=2,max-beds=4'
    elif num_bds <= 4:
        url = 'min-beds=3,max-beds=6'
    elif num_bds <= 5:
        url = 'min-beds=4'
    elif num_bds <= 10:
        url = 'min-beds=5'
    elif num_bds > 10:
        url = 'min-beds=6'
    else:
        url = ''

    return url


def search_url_part_five_gen(num_bths):

    if num_bths <= 1.0:
        url = ''
    elif num_bths <= 2.0:
        url = 'min-baths=1'
    elif num_bths <= 3.0:
        url = 'min-baths=2'
    elif num_bths <= 4.5:
        url = 'min-baths=3'
    elif num_bths <= 6.0:
        url = 'min-baths=4'
    elif num_bths <= 9.9:
        url = 'min-baths=5'
    elif num_bths > 10:
        url = 'min-baths=6'
    else:
        url = ''

    return url


def search_url_part_six_gen(sqft):

    if sqft <= 300:
        url = 'max-sqft=500-sqft'
    elif sqft <= 499:
        url = 'max-sqft=750-sqft'
    elif sqft <= 649:
        url = 'min-sqft=500-sqft,max-sqft=1k-sqft'
    elif sqft <= 849:
        url = 'min-sqft=500-sqft,max-sqft=1.25k-sqft'
    elif sqft <= 949:
        url = 'min-sqft=750-sqft,max-sqft=1.5k-sqft'
    elif sqft <= 1099:
        url = 'min-sqft=750-sqft,max-sqft=1.5k-sqft'
    elif sqft <= 1299:
        url = 'min-sqft=1k-sqft,max-sqft=1.75k-sqft'
    elif sqft <= 1599:
        url = 'min-sqft=1.25k-sqft,max-sqft=2k-sqft'
    elif sqft <= 1799:
        url = 'min-sqft=1.5k-sqft,max-sqft=2.25k-sqft'
    elif sqft <= 1999:
        url = 'min-sqft=1.5k-sqft,max-sqft=2.5k-sqft'
    elif sqft <= 2199:
        url = 'min-sqft=1.75k-sqft,max-sqft=2.75k-sqft'
    elif sqft <= 2499:
        url = 'min-sqft=2k-sqft,max-sqft=3k-sqft'
    elif sqft <= 2749:
        url = 'min-sqft=2.25k-sqft,max-sqft=3.5k-sqft'
    elif sqft <= 2999:
        url = 'min-sqft=2.25k-sqft,max-sqft=4k-sqft'
    elif sqft <= 3499:
        url = 'min-sqft=3k-sqft,max-sqft=4.5k-sqft'
    elif sqft <= 3999:
        url = 'min-sqft=3k-sqft,max-sqft=5k-sqft'
    elif sqft <= 4499:
        url = 'min-sqft=3.5k-sqft,max-sqft=7.5k-sqft'
    elif sqft <= 4999:
        url = 'min-sqft=4k-sqft,max-sqft=7.5k-sqft'
    elif sqft <= 5499:
        url = 'min-sqft=4.5k-sqft,max-sqft=7.5k-sqft'
    elif sqft <= 5999:
        url = 'min-sqft=4.5k-sqft'
    elif sqft <= 7999:
        url = 'min-sqft=5k-sqft'
    elif sqft >= 10000:
        url = 'min-sqft=7.5k-sqft'
    else:
        url = ''

    return url


def search_url_part_seven_gen(yr_blt):

    if yr_blt <= 1900:
        url = 'max-year-built=1940k'
    elif yr_blt <= 1960:
        url = 'min-year-built=1900,max-year-built=1970'
    elif yr_blt <= 1980:
        url = 'min-year-built=1950,max-year-built=2000'
    elif yr_blt <= 1995:
        url = 'min-year-built=1970,max-year-built=2005'
    elif yr_blt <= 2000:
        url = 'min-year-built=1980,max-year-built=2010'
    elif yr_blt <= 2005:
        url = 'min-year-built=1990,max-year-built=2015'
    elif yr_blt <= 2018:
        url = 'min-year-built=2005'
    else:
        url = ''

    return url


def search_url_part_eight_gen(lot_sqft):

    if lot_sqft <= 2000:
        url = 'max-lot-size=8k-sqft'
    elif lot_sqft <= 5200:
        url = 'min-lot-size=2k-sqft,max-lot-size=0.25-acre'
    elif lot_sqft <= 7500:
        url = 'min-lot-size=4.5k-sqft,max-lot-size=0.25-acre'
    elif lot_sqft <= 10000:
        url = 'min-lot-size=4.5k-sqft,max-lot-size=0.5-acre'
    elif lot_sqft <= 13000:
        url = 'min-lot-size=6.5k-sqft,max-lot-size=0.5-acre'
    elif lot_sqft <= 20000:
        url = 'min-lot-size=8k-sqft,max-lot-size=1-acre'
    elif lot_sqft <= 38000:
        url = 'min-lot-size=0.25-acre,max-lot-size=3-acre'
    elif lot_sqft <= 60000:
        url = 'min-lot-size=0.5-acre,max-lot-size=5-acre'
    elif lot_sqft <= 100000:
        url = 'min-lot-size=1-acre,max-lot-size=10-acre'
    elif lot_sqft <= 200000:
        url = 'min-lot-size=2-acre,max-lot-size=10-acre'
    elif lot_sqft <= 400000:
        url = 'min-lot-size=5-acre,max-lot-size=40-acre'
    elif lot_sqft <= 2400000:
        url = 'min-lot-size=5-acre,max-lot-size=100-acre'
    elif lot_sqft <= 4000000:
        url = 'min-lot-size=10-acre'
    elif lot_sqft > 4000000:
        url = 'min-lot-size=40-acre'
    else:
        url = ''

    return url


def search_url_part_nine_gen(hoa):

    if hoa_fee <= 0:
        url = ''
    elif hoa_fee <= 25:
        url = ',hoa=75'
    elif hoa_fee <= 50:
        url = ',hoa=100'
    elif hoa_fee <= 75:
        url = ',hoa=125'
    elif hoa_fee <= 100:
        url = ',hoa=150'
    elif hoa_fee <= 150:
        url = ',hoa=200'
    elif hoa_fee <= 200:
        url = ',hoa=250'
    elif hoa_fee <= 250:
        url = ',hoa=300'
    elif hoa_fee <= 300:
        url = ',hoa=400'
    elif hoa_fee <= 400:
        url = ',hoa=500'
    elif hoa_fee <= 500:
        url = ',hoa=600'
    elif hoa_fee <= 600:
        url = ',hoa=700'
    elif hoa_fee <= 700:
        url = ',hoa=800'
    elif hoa_fee <= 800:
        url = ',hoa=900'
    elif hoa_fee <= 900:
        url = ',hoa=1000'
    else:
        url = ''

    return url
