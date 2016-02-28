#!/usr/bin/env python
# -*- coding: utf-8 -*-
#获取雅虎财经上面各上市公司的股票的历史数据,以AXP作为示例
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
from datetime import datetime
import pandas as pd
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo('AXP',start,today)
fields = ['date','open','close','high','low','colume']
#转换成正常时间序列
timelist= []
for i in range(len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    timelist.append(y)
quotesdf = pd.DataFrame(quotes,index=timelist,columns = fields)
quotesdf = quotesdf.drop(['date'],axis = 1)
#print quotesdf
print quotesdf.head(5)
print quotesdf.tail(5)
