#/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

def monitor():
    shell_command = "grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree' /proc/meminfo"
    status,result = subprocess.getstatusoutput(shell_command)

    if status == 0:
        value_dic = {}
        for i in result.split('kB\n'):
            temp = i.split()
            key = temp[0].strip(':')
            value = temp[1]
            value_dic[key] = value
    MemUsage=int((int(value_dic['MemTotal'])-int(value_dic['MemFree'])-int(value_dic['Cached'])-int(value_dic['Buffers']))*100/int(value_dic['MemTotal']))
    SwapUsage=int(value_dic['SwapTotal']) - int(value_dic['SwapFree'])
    value_dic['MemUsage'] = MemUsage
    value_dic['SwapUsage'] = SwapUsage
    return value_dic