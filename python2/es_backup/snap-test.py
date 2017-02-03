import requests
import json
from datetime import date,timedelta

def getAllIndex():
    z=requests.get("http://172.17.2.81:9200/_cat/indices?format=json")
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
        n = requests.delete("http://172.17.2.81:9200/{0}".format(k))
        print k
        print n.content

if __name__ == '__main__':
    #backup = ["ips","firewall"]
    app_list=["app-route-intra","app-payment-core","app-gateway-route-intra","app-gateway-route-core","app-gateway-payment-core","app-gateway-channel-core","log"]
    # for i in backup:
    for i in app_list:
         esdelete("{0}".format(i))

