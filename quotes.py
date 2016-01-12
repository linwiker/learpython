#!/usr/bin/env python
# -*- coding: utf-8 -*-
#获取雅虎财经上面各上市公司的股票的历史数据,以AXP作为示例
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo('AXP',start,today)
fields = ['date','open','close','high','low','colume']
quotesdf = pd.DataFrame(quotes,index = range(1,len(quotes)+1),columns = fields)
print quotesdf
