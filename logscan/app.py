#/usr/bin/env python
# -*- coding: utf-8 -*-
from logscan.match import Matcher
from logscan.watch import Watcher
from logscan.schedule import Schedule

if __name__ == '__main__':
    import sys
    s = Schedule()
    try:
        s.add_watcher(Watcher(sys.argv[1], Matcher('#123#')))
        s.add_watcher(Watcher(sys.argv[2], Matcher('#123#')))
        s.join() #这个地方的join是等待线程退出
    except KeyboardInterrupt:
        s.remove_watcher(sys.argv[1])
        s.remove_watcher(sys.argv[2])
    #我们可以在下面再加一个join的，意思是等待上面两个remove_watcher的退出，然后再退出主线程。
    s.join()
