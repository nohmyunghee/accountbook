# -*- coding: UTF-8 -*-

import numpy as np
import time
import json
import os

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

    print("\n目前可选的消费类别有：")
    for i in range(len(category.category_list)):
        print("{} - {}".format(i, category.category_list[i]))
    category_index = int(input("请选择消费类别："))

    amount = float(input("\n请输入消费金额："))

    note = input("\n请输入消费详情：")

    deal = {'date':date,
            'category':category.category_list[category_index],
            'amount':amount,
            'note':note}

    record_file_name = str(date['year']) + '_' + str(date['month'])
    if os.path.isfile('./Records/' + record_file_name + '.json'):
        month_deal_list = json.load(open('./Records/' + record_file_name + '.json', 'r'))
        month_deal_list.append(deal)
        json.dump(month_deal_list, open('./Records/' + record_file_name + '.json', 'w'))
    else:
        json.dump([deal], open('./Records/' + record_file_name + '.json', 'w'))

    print("\n已保存。")

def get_monthly_deal(year, month):
    record_file_name = str(year) + '_' + str(month)
    month_deal_list = json.load(open('./Records/' + record_file_name + '.json', 'r'))
    deal_count = len(month_deal_list)
    print("{}年{}月共有{}笔交易.".format(year, month, deal_count))
    for deal in month_deal_list:
        for day in range(1, 32):
            if int(deal['date']['year']) == year and int(deal['date']['month']) == month and int(deal['date']['day']) == day:
                print("日期：{}-{}-{}\n类别：{}\n消费金额：{}\n详情：{}\n".format(deal['date']['year'], deal['date']['month'], deal['date']['day'], deal['category'], deal['amount'], deal['note']))

def get_daily_deal(year, month, day):
    record_file_name = str(year) + '_' + str(month)
    month_deal_list = json.load(open('./Records/' + record_file_name + '.json', 'r'))

    for deal in month_deal_list:
        if deal['date']['year'] == year and deal['date']['month'] == month and deal['date']['day'] == day:
            print("日期：{}-{}-{}\n类别：{}\n消费金额：{}\n详情：{}\n".format(deal['date']['year'], deal['date']['month'],
                                                                deal['date']['day'], deal['category'], deal['amount'],
                                                                deal['note']))
