#/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def monitor():
    shell_command = 'sar 1 3 | grep ^Average'
    status,result = subprocess.getstatusoutput(shell_command)

    if not status:
        value_dic = {}
        temp = result.split()
        value_dic['iowait'] = temp[-3]
        value_dic['idle'] = temp[-1]
    return value_dic


