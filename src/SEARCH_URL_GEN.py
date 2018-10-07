# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/02/2018

import re

'''Generating part one of the search URL that matches the property type to the
user interested in'''

def search_url_part_two_gen(type_home):

    #(type_home == re.compile('^Condo') or type_home == re.compile('^Town')):
    if ('Condo' in type_home or 'Town' in type_home):
        url = 'property-type=condo+townhouse'
    # type_home == re.compile('^Single'):
    elif 'Single' in type_home:
        url = 'property-type=house'
    else:
        url = ''

    return url

'''generating part three of the search URL that matches the users price range'''

def search_url_part_three_gen(price):

    if price > 12000000:
        url = 'min-price=6M'
    elif price >=80000000:
        url = 'min-price=5M'
    elif price >= 7000000:
        url = 'min-price=4.5M,max-price=10M'
    elif price >= 5250000:
        url = 'min-price=4.25M,max-price=8M'
    elif price >= 5000000:
        url = 'min-price=3.5M,max-price=7M'
    elif price >= 4250000:
        url = 'min-price=3.25M,max-price=6M'
    elif price >= 4000000:
        url = 'min-price=3.25M,max-price=5M'
    elif price >= 3750000:
        url = 'min-price=3.25M,max-price=4.5M'
    elif price >= 3500000:
        url = 'min-price=3M,max-price=4.25M'
    elif price >= 3250000:
        url = 'min-price=2.75M,max-price=3.75M'
    elif price >= 3000000:
        url = 'min-price=2.25M,max-price=3.5M'
    elif price >= 2750000:
        url = 'min-price=2M,max-price=3.25M'
    elif price >= 2500000:
        url = 'min-price=1.75M,max-price=3.25M'
    elif price >= 2250000:
        url = 'min-price=1.5M,max-price=2.75M'
    elif price >= 2000000:
        url = 'min-price=1.5M,max-price=2.5M'
    elif price >= 1750000:
    elif price >= 1500000:
        url = 'min-price=950k,max-price=2M'
    elif price >= 1250000:
        url = 'min-price=900k,max-price=1.5M'
    elif price >= 1000000:
        url = 'min-price=850k,max-price=1.25M'
    elif price >= 900000:
        url = 'min-price=750k,max-price=1M'
    elif price >= 850000:
        url = 'min-price=725k,max-price=950k'
    elif price >= 800000:
        url = 'min-price=1.25M,max-price=2.25M'
        url = 'min-price=700k,max-price=900k'
    elif price >= 725000:
        url = 'min-price=650k,max-price=800k'
    elif price >= 700000:
        url = 'min-price=600k,max-price=775k'
        url = 'min-price=575k,max-price=725k'
    elif price >= 650000:
        url = 'min-price=550k,max-price=700k'
    elif price >= 625000:
        url = 'min-price=500k,max-price=675k'
    elif price >= 600000:
        url = 'min-price=475k,max-price=650k'
    elif price >= 550000:
        url = 'min-price=500k,max-price=600k'
    elif price >= 500000:
        url = 'min-price=425k,max-price=550k'
    elif price >= 475000:
        url = 'min-price=400k,max-price=550k'
    elif price >= 450000:
        url = 'min-price=375k,max-price=500k'
    elif price >= 425000:
        url = 'min-price=350k,max-price=500k'
    elif price >= 400000:
        url = 'min-price=325k,max-price=475k'
    elif price >= 375000:
        url = 'min-price=300k,max-price=450k'
    elif price >= 350000:
        url = 'min-price=275k,max-price=400k'
    elif price >= 325000:
        url = 'min-price=250k,max-price=400k'
    elif price >= 300000:
        url = 'min-price=225k,max-price=375k'
    elif price >= 275000:
        url = 'min-price=225k,max-price=350k'
    elif price >= 250000:
        url = 'min-price=200k,max-price=325k'
    elif price >= 225000:
        url = 'min-price=150k,max-price=275k'
    elif price >= 200000:
        url = 'min-price=150k,max-price=250k'
    elif price >= 175000:
        url = 'min-price=125k,max-price=225k'
    elif price >= 150000:
        url = 'min-price=100k,max-price=200k'
    elif price >= 125000:
        url = 'min-price=75k,max-price=150k'
    elif price >= 100000:
        url = 'min-price=50k,max-price=125k'
    elif price >= 75000:
        url = 'max-price=125k'
    elif price >=35000:
        url = 'max-price=75k'
    elif (price > 1 and price < 35000):
        url = 'max-price=50k'
    elif price >= 675000:
    else:
        url = ''

    return url

'''generating part four of the search URL that matches the users preference
for number of bedrooms'''

def search_url_part_four_gen(num_bds):
    if num_bds > 10:
        url = 'min-beds=6'
    elif num_bds >= 8:
        url = 'min-beds=5'
    elif num_bds >= 5:
        url = 'min-beds=4'
    elif num_bds >=4:
        url = 'min-beds=3,max-beds=6'
    elif num_bds >= 3:
        url = 'min-beds=2,max-beds=4'
    elif num_bds >= 2:
        url = 'min-beds=1,max-beds=3'
    elif num_bds >=1:
        url = 'max-beds=2'
    if num_bds == 0:
        url = 'max-beds=1'
    else:
        url = ''

    return url

'''Generating part five of the search URL that matches the users preference
for number of bathrooms'''

def search_url_part_five_gen(num_bths):

    if num_bths >= 10:
        url = 'min-baths=6'
    elif num_bths >= 7:
        url = 'min-baths=5'
    elif num_bths >= 4.5:
        url = 'min-baths=3'
    elif num_bths >= 3:
        url = 'min-baths=2'
    elif num_bths >= 2:
        url = 'min-baths=1.25'
    elif num_bths > 1.01:
        url = 'min-baths=1'
    else:
        url = ''

    return url

'''Generating part six of the search URL that matches the users preference
for size of the home'''

def search_url_part_six_gen(sqft):

    if sqft >= 10050:
        url = 'min-sqft=7.5k-sqft'
    elif sqft >= 6000:
        url = 'min-sqft=5k-sqft'
    elif sqft >= 5500:
        url = 'min-sqft=5k-sqft,max-sqft=7.5k-sqft'
    elif sqft >= 4700:
        url = 'min-sqft=4k-sqft,max-sqft=7.5k-sqft'
    elif sqft >= 4300:
        url = 'min-sqft=3.5k-sqft,max-sqft=7.5k-sqft'
    elif sqft >= 3950:
        url = 'min-sqft=3.5k-sqft,max-sqft=5k-sqft'
    elif sqft >= 3750:
        url = 'min-sqft=3k-sqft,max-sqft=5k-sqft'
    elif sqft >= 3150:
        url = 'min-sqft=2.75k-sqft,max-sqft=4k-sqft'
    elif sqft >= 2950:
        url = 'min-sqft=2.5k-sqft,max-sqft=3.5k-sqft'
    elif sqft >= 2750:
        url = 'min-sqft=2.25k-sqft,max-sqft=3.5k-sqft'
    elif sqft >= 2550:
        url = 'min-sqft=2.25k-sqft,max-sqft=3k-sqft'
    elif sqft >= 2350:
        url = 'min-sqft=2k-sqft,max-sqft=3k-sqft'
    elif sqft >= 2200:
        url = 'min-sqft=1.75k-sqft,max-sqft=2.75k-sqft'
    elif sqft >= 2050:
        url = 'min-sqft=1.75k-sqft,max-sqft=2.5k-sqft'
    elif sqft >= 1900:
        url = 'min-sqft=1.5k-sqft,max-sqft=2.25k-sqft'
    elif sqft >= 1750:
        url = 'min-sqft=1.5k-sqft,max-sqft=2k-sqft'
    elif sqft >= 1650:
        url = 'min-sqft=1.25k-sqft,max-sqft=2k-sqft'
    elif sqft >= 1500:
        url = 'min-sqft=1.25k-sqft,max-sqft=1.75k-sqft'
    elif sqft >= 1400:
        url = 'min-sqft=1k-sqft,max-sqft=1.75k-sqft'
    elif sqft >= 1200:
        url = 'min-sqft=1k-sqft,max-sqft=1.5k-sqft'
    elif sqft >= 1025:
        url = 'min-sqft=1k-sqft,max-sqft=1.25k-sqft'
    elif sqft >= 900:
        url = 'min-sqft=750-sqft,max-sqft=1.25k-sqft'
    elif sqft >= 825:
        url = 'min-sqft=500-sqft,max-sqft=1k-sqft'
    elif sqft >= 350:
        url = 'max-sqft=750-sqft'
    elif sqft > 1:
        url = 'max-sqft=500-sqft'
    else:
        url = ''

    return url

'''Generating part seven of the search URL that matches the users preference
for the year the home was built in'''

def search_url_part_seven_gen(yr_blt):

    if yr_blt >= 2018:
        url = 'min-year-built=2005'
    elif yr_blt >= 2015:
        url = 'min-year-built=2000'
    elif yr_blt >= 2005:
        url = 'min-year-built=1990,max-year-built=2015'
    elif yr_blt >= 1995:
        url = 'min-year-built=1980,max-year-built=2010'
    elif yr_blt >= 1985:
        url = 'min-year-built=1960,max-year-built=2000'
    elif yr_blt >= 1975:
        url = 'min-year-built=1950,max-year-built=1980'
    elif yr_blt >= 1965:
        url = 'min-year-built=1940,max-year-built=1980'
    elif yr_blt >= 1955:
        url = 'min-year-built=1930,max-year-built=1970'
    elif yr_blt >= 1935:
        url = 'max-year-built=1960'
    elif yr_blt >= 1900:
        url = 'max-year-built=1950'
    elif (yr_blt <= 1900 and yr_blt > 1500):
        url = 'max-year-built=1940'
    else:
        url = ''

    return url

'''Generating part eight of the search URL that matches the users preference
for the lot size'''

def search_url_part_eight_gen(lot_sqft):

    if lot_sqft >= 3000000:
        url = 'min-lot-size=40-acre'
    elif lot_sqft >= 1000000:
        url = 'min-lot-size=10-acre'
    elif lot_sqft >= 400000:
        url = 'min-lot-size=5-acre,max-lot-size=40-acre'
    elif lot_sqft >= 200000:
        url = 'min-lot-size=2-acre,max-lot-size=10-acre'
    elif lot_sqft >= 100000:
        url = 'min-lot-size=1-acre,max-lot-size=10-acre'
    elif lot_sqft >= 60000:
        url = 'min-lot-size=0.5-acre,max-lot-size=5-acre'
    elif lot_sqft >= 38000:
        url = 'min-lot-size=0.25-acre,max-lot-size=3-acre'
    elif lot_sqft >= 20000:
        url = 'min-lot-size=8k-sqft,max-lot-size=1-acre'
    elif lot_sqft >= 13000:
        url = 'min-lot-size=6.5k-sqft,max-lot-size=0.5-acre'
    elif lot_sqft >= 10000:
        url = 'min-lot-size=4.5k-sqft,max-lot-size=0.5-acre'
    elif lot_sqft >= 7500:
        url = 'min-lot-size=4.5k-sqft,max-lot-size=0.25-acre'
    elif lot_sqft >= 4500:
        url = 'min-lot-size=2k-sqft,max-lot-size=0.25-acre'
    elif lot_sqft >= 2000:
        url = 'max-lot-size=8k-sqft'
    else:
        url = ''

    return url

'''Generating part nine of the search URL that matches the home user provided.
This could be crucial, since the closer the search to the HOA dues, if any,
from the home of their liking, the better the results'''

def search_url_part_nine_gen(hoa):

    if hoa_fee >= 900:
        url = ',hoa=1000'
    elif hoa_fee >= 800:
        url = ',hoa=900'
    elif hoa_fee >= 700:
        url = ',hoa=800'
    elif hoa_fee >= 600:
        url = ',hoa=700'
    elif hoa_fee >= 500:
        url = ',hoa=600'
    elif hoa_fee >= 400:
        url = ',hoa=500'
    elif hoa_fee >= 300:
        url = ',hoa=400'
    elif hoa_fee >= 250:
        url = ',hoa=300'
    elif hoa_fee >= 200:
        url = ',hoa=250'
    elif hoa_fee >= 150:
        url = ',hoa=200'
    elif hoa_fee >= 100:
        url = ',hoa=150'
    elif hoa_fee >= 75:
        url = ',hoa=125'
    elif hoa_fee >= 50:
        url = ',hoa=100'
    else:
        url = ''

    return url
