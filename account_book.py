# -*- coding: UTF-8 -*-

import numpy as np
import time

import deal_process




def main():
    # 获取今日日期
    year  = time.strftime('%Y', time.localtime())
    month = int(time.strftime('%m', time.localtime()))
    day   = int(time.strftime('%d',time.localtime()))

    print("您好，今天是{}年{}月{}日，欢迎使用My Account Book.".format(year, month, day))

    while(True):
        print("已有功能：")
        print("1 - 增加一条消费记录")
        print("0 - 退出")

        operation_idx = input("您要进行什么操作？")

        if operation_idx == "1":
            deal_process.add_deal()
        elif operation_idx == "0":
            print("谢谢使用！\n")
            break

    deal_process.get_monthly_deal(year, month)
    deal_process.get_daily_deal(year, month, day)



if __name__ == '__main__':
    main()