#/usr/bin/env python
# -*- coding: utf-8 -*-

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
         host_config_key =("HostConfig::%s",k)
         main_ins.r.set(host_config_key,json.dumps(v))