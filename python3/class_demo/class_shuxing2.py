# /usr/bin/env python
# -*- coding: utf-8 -*-
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码(第一页、第二页.....)
        self.current_page = current_page
        # 每页默认显示十条数据
        self.per_iterms = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_iterms
        return val

    @property
    def end(self):
        val = self.current_page * self.per_iterms
        return val


p = Pager(1)
print(p.start)
print(p.end)
