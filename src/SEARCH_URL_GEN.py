# Author: Mohit Gangwani
# Github: Data-is-Life
# Date: 10/02/2018

def search_url_part_two_gen(type_home):
    if (type_home == 'Condo' or type_home == 'Townhouse'):
        url = ',property-type=condo+townhouse'
    elif type_home == 'Single Family House':
        url = ',property-type=House'
    return url

def search_url_part_three_gen(price):    
    if price <= 49999:
        url = ',max-price=75k'
    elif price <= 74999:
        url = ',max-price=100k'
    elif price <= 99999:
        url = ',min-price=50k,max-price=125k'
    elif price <= 124999:
        url = ',min-price=75k,max-price=150k'
    elif price <= 149999:
        url = ',min-price=100k,max-price=175k'
    elif price <= 174999:
        url = ',min-price=125k,max-price=200k'
    elif price <= 199999:
        url = ',min-price=150k,max-price=225k'
    elif price <= 224999:
        url = ',min-price=175k,max-price=250k'
    elif price <= 249999:
        url = ',min-price=200k,max-price=275k'
    elif price <= 274999:
        url = ',min-price=225k,max-price=300k'
    elif price <= 299999:
        url = ',min-price=250k,max-price=325k'
    elif price <= 324999:
        url = ',min-price=275k,max-price=350k'
    elif price <= 349999:
        url = ',min-price=300k,max-price=375k'
    elif price <= 374999:
        url = ',min-price=325k,max-price=400k'
    elif price <= 399999:
        url = ',min-price=350k,max-price=425k'
    elif price <= 424999:
        url = ',min-price=375k,max-price=450k'
    elif price <= 449999:
        url = ',min-price=400k,max-price=475k'
    elif price <= 474999:
        url = ',min-price=425k,max-price=500k'
    elif price <= 499999:
        url = ',min-price=450k,max-price=550k'
    elif price <= 549999:
        url = ',min-price=500k,max-price=600k'
    elif price <= 599999:
        url = ',min-price=500k,max-price=650k'
    elif price <= 649999:
        url = ',min-price=550k,max-price=700k'
    elif price <= 699999:
        url = ',min-price=600k,max-price=750k'
    elif price <= 749999:
        url = ',min-price=650k,max-price=800k'
    elif price <= 799999:
        url = ',min-price=700k,max-price=850k'
    elif price <= 849999:
        url = ',min-price=750k,max-price=900k'
    elif price <= 899999:
        url = ',min-price=800k,max-price=950k'
    elif price <= 949999:
        url = ',min-price=850k,max-price=1M'
    elif price <= 999999:
        url = ',min-price=900k,max-price=1.25M'
    elif price <= 1249999:
        url = ',min-price=950k,max-price=1.5M'
    elif price <= 1499999:
        url = ',min-price=1M,max-price=1.75M'
    elif price <= 1749999:
        url = ',min-price=1.25M,max-price=2M'
    elif price <= 1999999:
        url = ',min-price=1.5M,max-price=2.25M'
    elif price <= 2249999:
        url = ',min-price=1.75M,max-price=2.5M'
    elif price <= 2499999:
        url = ',min-price=2M,max-price=2.75M'
    elif price <= 2749999:
        url = ',min-price=2.25M,max-price=3M'
    elif price <= 2999999:
        url = ',min-price=2.5M,max-price=3.25M'
    elif price <= 3249999:
        url = ',min-price=2.75M,max-price=3.5M'
    elif price <= 3499999:
        url = ',min-price=3M,max-price=4M'
    elif price <= 3749999:
        url = ',min-price=3.25M,max-price=4.25M'
    elif price <= 3999999:
        url = ',min-price=3.5M,max-price=4.5M'
    elif price <= 4249999:
        url = ',min-price=3.75M,max-price=5M'
    elif price <= 4499999:
        url = ',min-price=3.75M,max-price=6M'
    elif price <= 4749999:
        url = ',min-price=4M,max-price=6M'
    elif price <= 4999999:
        url = ',min-price=4.25M,max-price=6M'
    elif price <= 5999999:
        url = ',min-price=4.5M,max-price=7M'
    elif price <= 6999999:
        url = ',min-price=5M,max-price=9M'
    elif price <= 7999999:
        url = ',min-price=5M'
    elif price <= 8999999:
        url = ',min-price=6M'
    else:
        url = ',min-price=7M'

    return url


def search_url_part_four_gen(num_bds):
    if num_bds <= 0:
        url = ',min-beds=0,max-beds=1'
    elif num_bds <= 1:
        url = ',min-beds=1,max-beds=2'
    elif num_bds <= 2:
        url = ',min-beds=2,max-beds=3'
    elif num_bds <= 3:
        url = ',min-beds=3,max-beds=4'
    elif num_bds <= 4:
        url = ',min-beds=3,max-beds=5'
    elif num_bds <= 5:
        url = ',min-beds=4'
    elif num_bds <= 7:
        url = ',min-beds=5'
    else:
        url = ',min-beds=6'
    return url

def search_url_part_five_gen(num_bths):
    if num_bths <= 1:
        url = 'min-baths=1,'
    elif num_bths <= 2:
        url = 'min-baths=2,'
    elif num_bths <= 3:
        url = 'min-baths=2,'
    elif num_bths <= 4:
        url = 'min-baths=3,'
    elif num_bths <= 5:
        url = 'min-baths=4,'
    elif num_bths <= 6:
        url = 'min-baths=5,'
    else:
        url = 'min-baths=6,'

    return url


def search_url_part_six_gen(sqft):
    if sqft <= 350:
        url = ',max-sqft=500'
    elif sqft <= 549:
        url = ',max-sqft=750'
    elif sqft <= 649:
        url = ',min-sqft=500,max-sqft=750'
    elif sqft <= 849:
        url = ',min-sqft=500,max-sqft=1k'
    elif sqft <= 949:
        url = ',min-sqft=750,max-sqft=1k'
    elif sqft <= 1099:
        url = ',min-sqft=750,max-sqft=1.25k'
    elif sqft <= 1299:
        url = ',min-sqft=1k,max-sqft=1.5k'
    elif sqft <= 1599:
        url = ',min-sqft=1.25k,max-sqft=1.75k'
    elif sqft <= 1799:
        url = ',min-sqft=1.5k,max-sqft=2k'
    elif sqft <= 1999:
        url = ',min-sqft=1.5k,max-sqft=2.25k'
    elif sqft <= 2199:
        url = ',min-sqft=1.75k,max-sqft=2.5k'
    elif sqft <= 2499:
        url = ',min-sqft=2k,max-sqft=2.75k'
    elif sqft <= 2749:
        url = ',min-sqft=2.25k,max-sqft=3k'
    elif sqft <= 2999:
        url = ',min-sqft=2.5k,max-sqft=3.5k'
    elif sqft <= 3499:
        url = ',min-sqft=3k,max-sqft=4k'
    elif sqft <= 3999:
        url = ',min-sqft=3k,max-sqft=4.5k'
    elif sqft <= 4499:
        url = ',min-sqft=3.5k,max-sqft=5k'
    elif sqft <= 4999:
        url = ',min-sqft=4k,max-sqft=7.5k'
    elif sqft <= 5499:
        url = ',min-sqft=4.5k,max-sqft=7.5k'
    elif sqft <= 5999:
        url = ',min-sqft=5k,max-sqft=7.5k'
    elif sqft <= 7999:
        url = ',min-sqft=5k'
    else:
        url = ',min-sqft=7.5k'

    return url

def search_url_part_seven_gen(yr_blt):
    if yr_blt <= 1900:
        url = ',max-year-built=1930'
    elif yr_blt <= 1960:
        url = ',min-year-built=1930,max-year-built=1960'
    elif yr_blt <= 1980:
        url = ',min-year-built=1961,max-year-built=1980'
    elif yr_blt <= 1990:
        url = ',min-year-built=1981,max-year-built=1990'
    elif yr_blt <= 2000:
        url = ',min-year-built=1991,max-year-built=2000'
    elif yr_blt <= 2010:
        url = ',min-year-built=2001,max-year-built=2010'
    elif yr_blt <= 2018:
        url = ',min-year-built=2011,max-year-built=2016'
    else:
        url = ',min-year-built=2017'

    return url


def search_url_part_eight_gen(lot_sqft):
    if lot_sqft <= 2000:
        url = ',max-lot-size=6.5k-sqft'
    elif lot_sqft <= 4500:
        url = ',min-lot-size=2k-sqft,max-lot-size=6.5k-sqft'
    elif lot_sqft <= 6500:
        url = ',min-lot-size=4.5k-sqft,max-lot-size=8k-sqft'
    elif lot_sqft <= 8000:
        url = ',min-lot-size=4.5k-sqft,max-lot-size=0.25-acre'
    elif lot_sqft <= 0.25:
        url = ',min-lot-size=6.5k-sqft,max-lot-size=0.5-acre'
    elif lot_sqft <= 0.5:
        url = ',min-lot-size=8k-sqft,max-lot-size=1-acre'
    elif lot_sqft <= 1:
        url = ',min-lot-size=0.25-acre,max-lot-size=3-acre'
    elif lot_sqft <= 2:
        url = ',min-lot-size=0.5-acre,max-lot-size=5-acre'
    elif lot_sqft <= 3:
        url = ',min-lot-size=1-acre,max-lot-size=10-acre'
    elif lot_sqft <= 5:
        url = ',min-lot-size=2-acre,max-lot-size=10-acre'
    elif lot_sqft <= 10:
        url = ',min-lot-size=3-acre,max-lot-size=40-acre'
    elif lot_sqft <= 40:
        url = ',min-lot-size=5-acre,max-lot-size=100-acre'
    elif lot_sqft <= 100:
        url = ',min-lot-size=10-acre'
    else:
        url = ',min-lot-size=40-acre'

    return url


def search_url_part_nine_gen(hoa):
    if hoa <= 0:
        url = ',hoa=0'
    elif hoa <= 25:
        url = ',hoa=75'
    elif hoa <= 50:
        url = ',hoa=100'
    elif hoa <= 75:
        url = ',hoa=125'
    elif hoa <= 100:
        url = ',hoa=150'
    elif hoa <= 150:
        url = ',hoa=200'
    elif hoa <= 200:
        url = ',hoa=250'
    elif hoa <= 250:
        url = ',hoa=300'
    elif hoa <= 300:
        url = ',hoa=400'
    elif hoa <= 400:
        url = ',hoa=500'
    elif hoa <= 500:
        url = ',hoa=600'
    elif hoa <= 600:
        url = ',hoa=700'
    elif hoa <= 700:
        url = ',hoa=800'
    elif hoa <= 800:
        url = ',hoa=900'
    elif hoa <= 900:
        url = ',hoa=1000'
    else:
        url = ''

    return url