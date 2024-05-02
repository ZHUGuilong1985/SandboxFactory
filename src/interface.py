
from id_maker import create_id


class Interface():

    def __init__(self, obj):

        self.sbid = create_id()   # 接口编号，实际上就是数组的编号；通过parent和id可以连接到接口
        self.parent = obj  # 插槽
        self.position = None    # 容器, 装载设备、人员、材料、半成品等等；
        self.filter = None

        self.match_interface = None  # 为空，代表为未连接
        self.connection = None      # 为空，代表为未连接

    def reset_filter(self):
        pass

    def set_filter(self):
        pass


class Plug(Interface):
    '''
    插头, plug
    '''

    def __init__(self, parent, sbid, name=None):
        super().__init__(parent)

        self.match_interface = None  # 为空，代表为未连接
        self.connection = None       # 为空，代表为未连接


class Socket(Interface):
    '''
    插座, socket
    '''

    def __init__(self, parent, sbid, name=None):
        super().__init__(parent)

        self.match_interface = None     # 为空，代表为未连接
        self.connection = None          # 为空，代表为未连接
