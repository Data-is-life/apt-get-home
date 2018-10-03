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

def search_url_part_six_gen(sqft):
    if sqft <= 350:
        url = ',max-sqft=500'
    elif sqft <= 550:
        url = ',max-sqft=750'
    elif sqft <= 650:
        url = ',min-sqft=500,max-sqft=750'
    elif sqft <= 850:
        url = ',min-sqft=500,max-sqft=1k'
    elif sqft <= 950:
        url = ',min-sqft=750,max-sqft=1k'
    elif sqft <= 1100:
        url = ',min-sqft=750,max-sqft=1.25k'
    elif sqft <= 1300:
        url = ',min-sqft=1k,max-sqft=1.5k'
    elif sqft <= 1600:
        url = ',min-sqft=1.25k,max-sqft=1.75k'
    elif sqft <= 1800:
        url = ',min-sqft=1.5k,max-sqft=2k'
    elif sqft <= 2000:
        url = ',min-sqft=1.5k,max-sqft=2.25k'
    elif sqft <= 2200:
        url = ',min-sqft=1.75k,max-sqft=2.5k'
    elif sqft <= 2500:
        url = ',min-sqft=2k,max-sqft=2.75k'
    elif sqft <= 2750:
        url = ',min-sqft=2.25k,max-sqft=3k'
    elif sqft <= 3000:
        url = ',min-sqft=2.5k,max-sqft=3.5k'
    elif sqft <= 3500:
        url = ',min-sqft=3k,max-sqft=4k'
    elif sqft <= 4000:
        url = ',min-sqft=3k,max-sqft=4.5k'
    elif sqft <= 4500:
        url = ',min-sqft=3.5k,max-sqft=5k'
    elif sqft <= 5000:
        url = ',min-sqft=4k,max-sqft=7.5k'
    elif sqft <= 6000:
        url = ',min-sqft=4.5k,max-sqft=7.5k'
    elif sqft <= 6500:
        url = ',min-sqft=5k,max-sqft=7.5k'
    elif sqft <= 7500:
        url = ',min-sqft=5k'
    else:
        url = ',min-sqft=7.5k'

    return url



