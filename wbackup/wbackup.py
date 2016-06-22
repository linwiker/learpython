#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现实时远程备份

import os
import sys
import json
import paramiko
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class Wbackup(FileSystemEventHandler):

    def __init__(self, filename, sftp):
        self.filename = filename
        self.observer = Observer()
        self.sftp = sftp


    def start(self, arg):
        self.observer.schedule(self, path=self.filename, recursive=False)
        self.observer.start()
        self.observer.join()
        print(arg)


    def stop(self):
        self.observer.stop()

    def on_created(self, event):
        path = os.path.abspath(event.src_path)
        try:
            if not os.path.basename(path).startswith('.'):
                self.sftp.put(path)
        except:
            raise Exception('<{0}>同步失败created'.format(path))

    def on_modified(self, event):
        path = os.path.abspath(event.src_path)
        try:
            if not os.path.basename(path).startswith('.'):
                self.sftp.put(path)
        except:
            raise Exception('<{0}>同步失败modified'.format(path))

    def on_deleted(self, event):
        path = os.path.abspath(event.src_path)
        try:
            self.sftp.delete(path)
        except:
            raise Exception("<{0}>远端备份删除失败deleted".format(path))
    def on_moved(self, event):
        src_path = os.path.abspath(event.src_path)
        dest_path = os.path.abspath(event.dest_path)
        try:
            self.sftp.move(src_path, dest_path)
        except:
            raise Exception("远端备份<{0}>移动到<{1}>失败moved".format(src_ppath, dest_path))

class Rsync:

    def __init__(self, ip, username, password, dest_path):
        self.t = paramiko.Transport((ip,22))
        self.ssh = paramiko.SSHClient()
        self.t.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip,22, username, password)
        self.dest_path = dest_path
    
    #本地发现有修改或者创建的话，直接sftp传到远端，传之前做判断是否由此目录，如果没有的话创建目录
    def put(self, src_path):
        path = os.path.join(self.dest_path, os.path.dirname(src_path).split('/',1)[1])
        stdin,stdout,stderr = self.ssh.exec_command("ls {0}".format(path))
        if stderr.read():
            _,_,stderr = self.ssh.exec_command("mkdir -p {0}".format(path))
            if stderr.read():
                print("备份端<{0}>创建失败".format(os.path.dirname(path)))
        try:
            if not os.path.isdir(src_path):
                print(src_path)
                self.sftp.put(src_path, os.path.join(self.dest_path, src_path.split('/',1)[1]))
        except:
            raise Exception("<{0}>同步失败".format(src_path))

    def delete(self, src_path):
        stdin,stdout,stderr = self.ssh.exec_command("rm -rf {0}".format(os.path.join(self.dest_path, src_path.split('/',1)[1])))
        if not stderr:
            print("<{0}>远端删除失败".format(src_path))

    def move(self, src_path, dest_path):
        _,_,stderr = self.ssh.exec_command("mv {0} {1}".format(os.path.join(self.dest_path, src_path.split('/',1)[1]), os.path.join(self.dest_path,dest_path.split('/',1)[1])))
        if not stderr:
            print("move<{0}>到<{1}>失败".format(src_path, dest_path))

    def stop(self):
        self.t.close()
        self.ssh.close()

if __name__ == '__main__':
    f = open('wbackup.json', 'r')
    conf = json.load(f)
    rsync = Rsync(conf['ip'], conf['username'], conf['password'], conf['dest_path'])
    w = Wbackup(conf['path'], rsync)
    try:
        w.start()
    except KeyboardInterrupt:
        w.stop()
        rsync.stop()
