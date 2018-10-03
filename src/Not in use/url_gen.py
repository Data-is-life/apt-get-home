# def search_url_part_four_gen(price):

#     pmik = int(price//100000)
#     pmvk = int(price % 100000)/1000

#     pmim = int(price//1000000)
#     pmvm = int(price % 1000000)/10000

#     if price <= 500000:
# #         if pmvk <= 24.99:
# #             min_price = str(pmik)+'50k'
#         if pmvk <= 49.99:
#             max_price = str(pmik)+'75k'
#         elif pmvk <= 74.99:
#             max_price = str(pmik+1)+'00k'
#         else:
#             max_price = str(pmik+1)+'25k'
#         url = ',max-price='+max_price

#     elif price <= 900000:

#         if pmvk <= 29.99:
#             max_price = str(pmik)+'50k'
#         elif pmvk <= 59.99:
#             max_price = str(pmik+1)+'00k'
#         else:
#             max_price = str(pmik+1)+'50k'
#         url = ',max-price='+max_price

#     elif price <= 1000000:

#         if pmvk <= 29.99:
#             max_price = '1M'
#         else:
#             max_price = '1.25M'
#         url = ',max-price='+max_price

#     elif price <= 2000000:
#         if pmv <= 24.99:
#             max_price = str(pmim)+'.5M'
#         elif pmv <= 49.99:
#             max_price = str(pmim)+'.75M'
#         elif pmv <= 74.99:
#             max_price = str(pmim+1)+'M'
#         else:
#             max_price = str(pmim+1)+'.25M'
#         url = ',max-price='+max_price

#     elif price <= 3250000:
#         if pmvm <= 24.99:
#             max_price = str(pmim)+'.75M'
#         elif pmvm <= 49.99:
#             max_price = str(pmim+1)+'M'
#         elif pmvm <= 74.99:
#             max_price = str(pmim+1)+'.25M'
#         else:
#             max_price = str(pmim+1)+'.5M'
#         url = ',max-price='+max_price

#     elif price <= 3500000:
#         url = ',min-price=2.75M,max-price=4.25M'
#     elif price <= 4000000:
#         url = ',min-price=3.25M,max-price=5M'
#     elif price <= 4500000:
#         url = ',min-price=3.5M,max-price=6M'
#     elif price <= 5000000:
#         url = ',min-price=4.25M,max-price=7M'
#     elif price <= 6000000:
#         url = ',min-price=4.5M,max-price=8M'
# #     elif price <= 7000000:
# #         url = ',min-price=5M'
# #     elif price <= 9000000:
# #         url = ',min-price=5M'
# #     else:
# #         url = ',min-price=6M'
#     return url
