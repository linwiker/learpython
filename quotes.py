#!/usr/bin/env python
# -*- coding: utf-8 -*-
#获取雅虎财经上面各上市公司的股票的历史数据
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo('AXP',start,today)
df = pd.DataFrame(quotes)
print df
