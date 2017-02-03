import requests
import json
from datetime import date,timedelta
import time

def getAllIndex():
    z=requests.get("http://192.168.212.77:9200/_cat/indices?format=json")
    li = []
    for i in json.loads(z.content):
        li.append(i.get(u'index'))
    li.remove(".kibana")
    return li

def esdelete(servicename):
    t = date.today() - timedelta(days=30)
    A = getAllIndex()
    v = []
    timestap = str(t).replace("-", ".")
    index = "{0}-{1}".format(servicename, timestap)
    for i in A:
        if i.startswith(servicename):
            v.append(i)
    for j in range(30):
        if index in v:
            v.remove(index)
        t = t + timedelta(days=1)
        timestap = str(t).replace("-", ".")
        index = "{0}-{1}".format(servicename, timestap)
    for k in v:
        putbody = {
            "indices": k,
            "ignore_unavailable": True,
            "include_global_state": False
        }
        n = requests.delete("http://192.168.212.77:9200/{0}".format(k))
        print n.content

if __name__ == '__main__':
    #backup = ["ips","firewall"]
    #app_list=["admin-nginx","api-nginx-access","nginx-access","log","f5","netapp","router","switch","ws-logging-arch"]
    # for i in backup:
    # for i in app_list:
    #     esbackup("{0}".format(i),"app")
    esdelete("log")
