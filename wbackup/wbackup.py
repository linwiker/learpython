#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现实时远程备份

import os
import sys
import paramiko
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class Wbackup(FileSystemEventHandler):

    def __init__(self, filename, sftp):
        self.filename = filename
        self.observer = Observer()
        self.sftp = sftp


    def start(self):
        self.observer.schedule(self, path=self.filename, recursive=False)
        self.observer.start()
        self.observer.join()


    def stop(self):
        self.observer.stop()

    def on_created(self, event):
        print(event.src_path)
        try:
            self.sftp.put(event.src_path)
        except:
            raise Exception('{0}同步失败'.format(event.src_path))

    def on_modified(self, event):
        try:
            self.sftp.put(event.src_path)
        except:
            raise Exception('{0}同步失败'.format(event.src_path))

    def on_deleted(self, event):
        try:
            self.sftp.delete(event.src_path)
        except:
            raise Exception("{0}远端删除失败".format(event.src_path))
    def on_moved(self, event):
        try:
            self.sftp.move(event.src_path, event.dest_path)
        except:
            raise Exception("{0}远端移动到{1}失败".format(event.src_path, event.dest_path))

class Rsync:

    def __init__(self, ip, username, password, dest_path):
        self.t = paramiko.Transport((ip,22))
        self.ssh = paramiko.SSHClient()
        self.t.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip,22, username, password)
        self.dest_path = dest_path

    def put(self, src_path):
        if not os.path.exists(self.dest_path):
            _,_,stderr = self.ssh.exec_command("mkdir {0}".format(self.dest_path))
            if stderr:
                print("{0} 创建失败")
                print(stderr.read())
        try:
            self.sftp.put(src_path, os.path.join(self.dest_path,src_path))
        except:
            raise Exception("{0}同步失败".format(src_path))

    def delete(self, src_path):
        stdin,stdout,stderr = self.ssh.exec_command("rm -rf {0}".format(src_path))
        if stderr:
            print("{0} 远端同步失败".format(src_path))

    def move(self, src_path, dest_path):
        _,_,stderr = self.ssh.exec_command("mv {0} {1}".format(src_path, dest_path))
        if stderr:
            print("{0}远端移动到{1}失败".format(src_path, dest_path))

    def stop(self):
        self.t.close()
        self.ssh.close()

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    rsync = Rsync('127.0.0.1', 'wiker', 'zhouwenjia@30','/tmp/')
    w = Wbackup(path,rsync)
    try:
        w.start()
    except KeyboardInterrupt:
        w.stop()
        rsync.stop()




