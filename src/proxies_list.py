import random

proxies_list_ = ['12.183.155.91:39828', '12.2.202.242:8080', '12.239.213.145:32313',
                 '24.177.187.101:47599', '24.248.37.66:31100', '37.224.84.90:8080',
                 '50.224.173.179:8080', '50.224.173.189:8080', '50.224.173.190:8080',
                 '50.79.20.203:57378', '64.19.116.82:60814', '66.60.134.102:60170',
                 '67.165.205.83:40086', '68.188.21.10:44314', '69.38.69.254:52168',
                 '72.35.40.34:8080', '96.250.47.126:54157', '96.43.255.82:52283',
                 '96.87.222.225:43075', '98.101.147.86:50259', '98.26.32.15:36891',
                 '140.227.60.114:3128', '160.2.250.19:46694', '173.88.208.145:41111',
                 '216.21.161.185:48560', '216.228.69.202:42651', '24.112.63.248:35663',
                 '50.224.87.210:50850', '50.78.238.83:54172', '64.58.192.36:41258',
                 '216.85.7.155:59880', '97.90.251.228:8080', '160.2.232.154:50346',
                 '108.29.37.161:59481', '74.0.244.146:52807', '104.160.108.10:42239',
                 '65.154.9.12:37593', '71.43.23.74:47012', '67.79.64.90:39423',
                 '23.25.254.91:37617', '173.17.122.32:58548', '173.15.195.9:61561',
                 '97.80.39.42:59543', '68.101.62.26:8888', '38.134.10.106:53281',
                 '216.27.126.86:53146', '192.0.10.186:51886', '65.49.167.6:8888']
                 
proxie_random_pool = random.sample(proxies_list_, len(proxies_list_))
