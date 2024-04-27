import random
import string

import hashlib  # hash
import time  # time


class IdMaker:

    @staticmethod
    def get_hash():
        # 根据时间，给出一个不重复的id
        return ''

    @staticmethod
    def get_unique_id():
        # 生产产品的唯一记录码
        # 根据记录生成的时间和文件名，生成；
        # hashlib.sha256(my_string.encode()).hexdigest()
        # md5_hash = hashlib.md5(my_string.encode()).hexdigest()

        t = int(time.time())
        s = str(t)
        md5_hash = hashlib.md5(s.encode()).hexdigest()
        return md5_hash.upper()
