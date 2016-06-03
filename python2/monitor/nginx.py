#!/usr/bin/env python
# -*- coding: utf-8 -*-
# _author:wiker

import json
import urllib2
import os
import sys

# 把字符转换为数字，便于监控的时候使用
dic_status = {'False': 1, 'True': 0}
content = urllib2.urlopen("http://10.150.128.11/stats_json").read()
dic_demo = json.loads(content)
dic = {}
# 取出需要的值写到dic字典内
dic['requests'] = dic_demo['connections']['requests']
for i in dic_demo["upstreamZones"].keys():
    if i == "store.asus.com.cn" or i == "img.asus.com.cn":
        for j in dic_demo["upstreamZones"][i]:
            dic[j['server']] = {'stats': dic_status[str(j['down'])], '5xx': j['responses']['5xx'],
                                'responeMsec': j['responeMsec']}


def nginx(item,parms=None):

    #首先判断是否存在上一次的监控记录，如果没有的话，直接把本次收集的写入文件内，如果有的话，取出上一次存储在文本内的数据进行对比
    if os.path.isfile("/tmp/nginx.json"):
        with open('/tmp/nginx.json','rb') as f:
            pre_dic = json.load(f)
            if item == 'requests':
                value = dic[item] - pre_dic[item]
                print(value)
            #除了5xx需要计算外，其他两项可以直接取原值
            else:
                if parms == '5xx':
                    value = dic[item][parms] - pre_dic[item][parms]
                    print(value)
                else:
                    value = dic[item][parms]
                    print(value)
        #把本次数据写到文本，覆盖掉上一次
        with open('/tmp/nginx.json', 'wb') as f:
            json.dump(dic, f)

    else:
        with open('/tmp/nginx.json','wb') as f:
            json.dump(dic, f)

if __name__ == '__main__':
    #使用方法
    item = sys.argv[1]
    if item in dic.keys():
        if item == "requests":
            nginx(item)
        else:
            parms = sys.argv[2]
            if parms in dic[item].keys():
                nginx(item, parms)
            else:
                print("Use:\n\tparms: [{0}]".format(dic[item].keys()))
    else:
        print("Use:\n\titem: [{0}]".format(dic.keys()))

