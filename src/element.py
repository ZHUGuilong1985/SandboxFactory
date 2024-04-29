import sys
import time
import copy
from abc import ABCMeta, abstractmethod
from enum import Enum

from id_maker import IdMaker


class Element():

    def __init__(self, root_container, id=None):
        # root_container

        if id:
            self.id = id
        else:
            self.id = IdMaker.get_unique_id()

        self.desription = ''                  # 描述
        self.root_container = root_container  #  dm or layout

    def refresh():
        # 由于曾在嵌套，需要优化更新顺序！内部的需要提前优化；

        # 预处理
        for i in Element.element_list:
            i.refresh_pre()

        # 处理
        for i in Element.element_list:
            i.refresh_process()

        # 后处理
        for i in Element.element_list:
            i.refresh_post()
