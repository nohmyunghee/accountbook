# -*- coding: UTF-8 -*-

import numpy as np
import time

import deal_process




def main():
    # 获取今日日期
    year  = time.strftime('%Y', time.localtime())
    month = time.strftime('%m', time.localtime())
    day   = time.strftime('%d',time.localtime())

    print("您好，今天是{}年{}月{}日，欢迎使用My Account Book.".format(year, month, day))

    while(True):
        print("您需要做什么？")
        print("1 - 增加一条消费记录")

    deal_process.add_deal()




if __name__ == '__main__':
    main()