import requests
import json
from datetime import date,timedelta
import time

def getAllIndex():
    z=requests.get("http://172.17.43.122:9200/_cat/indices?format=json")
    li = []
    for i in json.loads(z.content):
        li.append(i.get(u'index'))
    li.remove(".kibana")
    return li

def esbackup(servicename, reposname):
    t = date.today() - timedelta(days=14)
    A = getAllIndex()
    v = []
    dic = {}
    for i in A:
        if i.startswith(servicename):
            v.append(i)
            timestap = str(t).replace("-", ".")
            index = "{0}-{1}".format(servicename, timestap)
            if v:
                if index in v:
                    putbody = {
                        "indices": index,
                        "ignore_unavailable": True,
                        "include_global_state": False
                    }
                    v.remove(index)
                    print putbody
                    snapput = requests.put(
                        "http://172.17.43.122:9200/_snapshot/{0}/{1}?wait_for_completion=true".format(reposname,index),
                        data=json.dumps(putbody))
                    p = json.loads(snapput.content)
                    if snapput.status_code == 200:
                        dic[p.get("snapshot").get("snapshot")] = p.get("snapshot").get("reason")
                    print snapput.content
                    time.sleep(1)
                    t = t - timedelta(days=1)
                    timestap = str(t).replace("-", ".")
                    index = "{0}-{1}".format(servicename, timestap)
    with open("/tmp/snap.txt","a") as f:
        json.dump(dic,f)

if __name__ == '__main__':
    esbackup("firewall","Full_backup")
