#/usr/bin/env python
# -*- coding: utf-8 -*-

import templates

web_clusters = templates.LinuxGenericTemplate()
web_clusters.hosts = ['10.99.56.124',
                      '10.99.56.121',
                      '10.99.16.254']

mysql_groups = templates.Linux2()
mysql_groups.hosts = ['10.99.56.124',
                      '10.99.56.121']

monitored_groups = [web_clusters, mysql_groups]  #监控主机组列表

if __name__ == '__main__':
     host_config_dic = {}
     for group in monitored_groups:
         for host in group.hosts: #列出需要监控的主机
             if host not in host_config_dic: #如果主机不在host_config_dic字典内，则在host_config_dic字典在以host为key再生成一个空的字典
                 host_config_dic[host] = {}
             for s in group.services: #对服务进行循环，然后把以服务名为key的字典加到host为key的字典内。
                 host_config_dic[host][s.name] = [s.plugin_name, s.interval]
     for k, v in host_config_dic.items(): #循环出所有主机的监控项目
         print(k,v)
