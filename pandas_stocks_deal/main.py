# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/22_21:05 '

import numpy as np
import pandas as pd

names = ['date',  # 日期
         'time',  # 时间
         'opening_price',  # 开盘价
         'ceiling_price',  # 价格上限
         'floor_price',  # 价格下线
         'closing_price',  # 收盘价
         'volume',  # 成交量
         'amount']  # 成交额

raw = pd.read_csv('data/SH600690.csv', names=names, index_col='date', parse_dates=True)  # 读取csv文件 创建DataFrame


# print raw.head(5)  # 打印前五行
# print raw.tail(5)  # 打印后五行

# 过滤涨跌幅超过10%的股票
def _valid_price(g):
    # print g.max(), g.min()
    return (((g.max() - g.min()) / g.min()) < 0.223).all()


# 按照日期分组
days = raw.groupby(level='date').agg(
    {'opening_price': lambda g: _valid_price(g) and g[0] or 0,
     'ceiling_price': lambda g: _valid_price(g) and np.max(g) or 0,
     'floor_price': lambda g: _valid_price(g) and np.min(g) or 0,
     'closing_price': lambda g: _valid_price(g) and g[-1] or 0,
     'volume': 'sum',
     'amount': 'sum'})
# print days.head()
qdhr = pd.read_csv('data/_SH600690.csv', names=names, index_col='date', parse_dates=True)



if __name__ == '__main__':
    pass
