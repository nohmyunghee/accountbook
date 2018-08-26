# -*- coding: UTF-8 -*-

import numpy as np
import time
import json

from deal_category import deal_category

def add_deal():
    date = {'year':0, 'month':0, 'day':0}
    category = deal_category()
    amount = 0
    note = ""

    print("请输入消费信息：")

    input_date = input("日期(yyyy-mm-dd)：")
    date['year']  = input_date.split('-')[0]
    date['month'] = input_date.split('-')[1]
    date['day']   = input_date.split('-')[2]

    print("目前可选的消费类别有：")
    for i in range(len(category.category_list)):
        print("{} - {}".format(i, category.category_list[i]))
    category_index = int(input("请选择消费类别："))

    amount = float(input("请输入消费金额："))

    note = input("请输入消费详情：")

    deal = [{'date':date,
             'category':category.category_list[category_index],
             'amount':amount,
             'note':note}]

    file = open('./Records/daily_records.json', 'w+')
    file.write(json.dumps(deal))