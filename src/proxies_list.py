import random

proxies_list_ = ['12.2.202.242:8080', '140.227.60.114:3128', '37.224.84.90:8080', 
                '64.19.116.82:60814', '50.224.173.189:8080', '72.35.40.34:8080', 
                '50.224.173.190:8080', '50.224.173.179:8080', '174.61.82.138:57511', 
                '184.105.42.66:32103', '104.193.236.63:36937', '207.98.171.42:8888', 
                '160.2.250.19:46694', '24.148.73.79:8080', '199.21.106.154:43396', 
                '50.246.214.132:34827', '100.40.4.230:59809', '104.165.219.163:46101', 
                '173.88.208.145:41111']
                
proxie_random_pool = random.sample(proxies_list_, len(proxies_list_))