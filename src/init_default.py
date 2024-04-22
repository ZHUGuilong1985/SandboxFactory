# 读取数据

import json
import os

# 配置文件
SETUP_PATH = r'./src/resource.json'

default_info = {
    "database":     "default_database",
    "version":      0.1,
    "resources":    []
}


class SetupSystem():

    @staticmethod
    def load_setup():
        json_data = open_setup_file(SETUP_PATH)
        return json_data  # 返回配置信息

    @staticmethod
    def save_setup(info):
        save_setup_file(SETUP_PATH, info)


def open_setup_file(file_path):
    # 读取文件

    if not os.path.exists(file_path):  # 不存在，新建一个默认的配置文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(default_info, f)  # 转存
        return default_info
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data


def save_setup_file(file_path, info):

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(info, json_file)


# country_dict = json.loads(json_string) # 将 JSON 字符串转换为 Python 字典
# json_string  = json.dumps(data)        # 将 Python 字典转换为 JSON 字符串


if __name__ == '__main__':

    d = SetupSystem.load_setup()
    # d['created_time'] = '2024-04-52'
    # SetupSystem.save_setup(d)
    print(d)
