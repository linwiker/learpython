#/usr/bin/env python
# -*- coding: utf-8 -*-
from conf import hosts
import json

def  push_all_configs_into_redis(main_ins,host_groups):
     host_config_dic = {}
     for group in host_groups:
         for host in group.hosts: #列出需要监控的主机
             if host not in host_config_dic: #如果主机不在host_config_dic字典内，则在host_config_dic字典在以host为key再生成一个空的字典
                 host_config_dic[host] = {}
             for s in group.services: #对服务进行循环，然后把以服务名为key的字典加到host为key的字典内。
                 host_config_dic[host][s.name] = [s.plugin_name, s.interval]
     for k, v in host_config_dic.items(): #配置信息存储到redis里面
         host_config_key =("HostConfig::%s" %k)
         main_ins.r.set(host_config_key,json.dumps(v))

def fetch_all_configs(host_groups):
     host_config_dic = {}
     for group in host_groups:
         for host in group.hosts:
             if host not in host_config_dic:
                 host_config_dic[host] = {}
             for s in group.services:
                 host_config_dic[host][s.name] = s
     for k, v in host_config_dic.items():
         print(k,v)
     return host_config_dic


def data_process(main_ins):
    all_host_configs = fetch_all_configs(hosts.monitored_groups)
    while True:
        for ip,service_dic in all_host_configs.items():
            for service_name,s_instance in service_dic.items():
                service_redis_key = "ServerData::%s::%s" %(ip, service_name)
                s_data = main_ins.r.get(service_redis_key)
                if s_data:
                    s_data = json.loads(s_data)
                    time_stamp = s_data['time_stamp']
                    if time.time() - time_stamp < s_instance.interval:
                        for item_key, val_dic in s_instance.triggers.items():

                else:
                    print(" host [%s] service [%s] No data from redis" %(ip, service_name))
