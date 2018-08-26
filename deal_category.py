# -*- coding: UTF-8 -*-

import json

class deal_category:
    """
    消费分类的管理
    """
    def __init__(self):
        """
        初始化所有消费类别
        """
        file = open('./Config/category.json', 'r')
        self.category_list = json.load(file)


    def delete_category(self, category_name):
        """
        删除一个消费类别
        :param category_name: 需要删除的消费类别
        :return:
        """
        self.category_list.remove(category_name)

    def add_category(self, category_name):
        """
        增加一个消费类别
        :param category_name: 需要增加的消费类别
        :return:
        """
        self.category_list.append(category_name)