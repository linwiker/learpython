import requests
import json

z=requests.get("http://172.17.43.122:9200/_cat/indices?format=json")
li = []
for i in json.loads(z.content):
    li.append(i.get(u'index'))
for i in li:
    if i > "admin-nginx-2016.10.30":
        li.remove(i)
    else:
        print 1
print li