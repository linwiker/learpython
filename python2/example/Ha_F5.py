# F5_HA test script
# -*- coding: utf-8 -*-

import requests
import time

def curl():
    try:
        n = requests.get("http://127.0.0.1")
        if n.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

flag = 0
while True:
    ret = curl()
    if ret == True and flag == 1:
        end = time.time()
        print begin,end
        print str(end-begin)
        break
    if flag ==0 and ret == False:
        begin = time.time()
        flag = 1
exit(0)

