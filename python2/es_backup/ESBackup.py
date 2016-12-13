#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from datetime import date,timedelta
import time


class Esbackup():
    def __init__(self, esip):
        self.esip = esip
        self.yesterday = date.today() - timedelta(days=6)
        self.timeline = str(self.yesterday).replace("-", ".")

    def getallindex(self):
        rq = requests.get("http://{0}:9200/_cat/indices?format=json".format(self.url))
        allindex = []
        for i in json.loads(rq.content):
            allindex.append(i.get(u'index'))
        allindex.remove(".kibana")
        return allindex


    def backup(self, servicename,reponame):
        index = "{0}-{1}".format(servicename, self.timeline)
        body = {
            "indices": index,
            "ignore_unavailable": True,
            "include_global_state": False
        }
        begin = time.time()
        snapput = requests.put("http://{0}:9200/_snapshot/{1}/{2}?wait_for_completion=true".format(self.esip, reponame, index), data=json.dumps(body))
        end = time.time()
        usetime = end - begin
        usetime = round(usetime, 2)
        content = json.loads(snapput.content)
        print content
        status = content.get("snapshot").get("state")
        if status == "SUCCESS":
            state = "成功"
        else:
            state = "失败"
        postbody = {"name": index, "type": "ELK", "action": "备份", "usetime": usetime, "status": state, "comments": "备份{0}到{1}".format(index, reponame)}
        # z = requests.post("http://192.168.23.182:8000/backupplatform/backupjob/api/",data=json.dumps(postbody,ensure_ascii=False))
        requests.post("http://ops.ppdaicorp.com/backupplatform/backupjob/api/",data=json.dumps(postbody, ensure_ascii=False))

    #删除14天之前的日志
    def delete(self, servicename):
        delday = date.today() - timedelta(days=14)
        timeline = str(delday).replace("-", ".")
        index = "{0}-{1}".format(servicename, timeline)
        begin = time.time()
        snapdel = requests.delete("http://{0}:9200/{1}?wait_for_completion=true".format(self.esip, index))
        end = time.time()
        usetime = end - begin
        usetime = round(usetime, 2)
        content = json.loads(snapdel.content)
        status = content["acknowledged"]
        print content
        if status == True:
            state = "成功"
            print state
        else:
            state = "失败"
        print index
        postbody = {"name": index, "type": "ELK", "action": "删除", "usetime": usetime, "status": state,"comments": "删除{0}索引".format(index)}
        requests.post("http://ops.ppdaicorp.com/backupplatform/backupjob/api/", data=json.dumps(postbody, ensure_ascii=False))

if __name__ == '__main__':
    esbak = Esbackup("172.17.43.122")
    # app_list = ["admin-access", "api-nginx-access", "nginx-access", "log", "f5", "netapp", "router", "switch"]
    # for i in app_list:
    #     esbak.backup(i,"app")
    backup = ["ips", "firewall"]
    for j in backup:
        esbak.backup(j,"Full_backup")
        # esbak.delete(j)











