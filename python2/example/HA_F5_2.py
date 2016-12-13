# F5_HA test script

import requests
import time

import requests
import time

while True:
    n = requests.get("http://172.16.14.20")
    if n.status_code == 200:
        begin = time.time()
    else:
        end = time.time()
        usetime = end - begin
        print usetime
        break

