
#/usr/bin/env python
# -*- coding: utf-8 -*-

import twisted_demo
class MyHandler(twisted_demo.BaseHandle):
    def execute(self):
        print('event-drive execute Myhandler')

twisted_demo.event_list.append(MyHandler)
twisted_demo.run()