
# 新建配置，工位

class Configuration():
    ''' 
    配置：
    1. 适用于station；
    典型内容：
    1. 设备；
    2. 人员；
    3. 场地；
    '''

    def __init__(self, configuration_name, configuration_txt):
        self.__configuration_name = configuration_name  # 名字
        self.__configuration_txt = configuration_txt    # 内容
        self.__elementList = []   # 空表

    def fatmat(self):
        '''
        格式化公式
        '''
        pass

    def translation(self):
        ''' 
        翻译
        '''
        if self.__configuration_txt == "":
            return None
