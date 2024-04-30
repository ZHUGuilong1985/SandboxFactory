
import copy


class Connection:
    '''
    定义连接
    '''

    def __init__(self, plug, socket):  # 创建连接
        self.plug = plug
        self.socket = socket

        # 两边记录匹配
        self.plug.connection = self  # return the connection.
        self.plug.match_interface = self.socket

        self.socket.connection = self   # return the connection.
        self.socket.match_interface = self.plug

        print("{}和{}建立连接".format(self.plug.parent.name, self.socket.parent.name))

    def disconnect(self):
        del self

    def __delete__(self):  # 删除时，解除两边
        self.plug.connection = None
        self.plug.match_interface = None
        self.socket.connection = None
        self.socket.match_interface = None

        print("{}和{}断开连接".format(self.plug.parent.name, self.socket.parent.name))

    def transport(self, num):
        '''
        transport objects from plug to socket. 
        本质上是position之间的物资传递？
        '''

        # 没有位置，退出
        if self.plug.position == None or self.socket.position == None:
            return

        # case: plug 没有物料
        if self.plug.position.real_material == None:
            return

        # case: plug 有物料
        # 计算 socket 实际能接收的物料量

        if self.socket.position.real_material == None:  # 没有材料，则有效空间就是容量
            free_space = self.socket.position.volume

        else:   # 有材料，则是差值
            free_space = self.socket.position.volume - \
                self.socket.position.real_material.amount

        # 计算能够传递的材料数量
        if free_space >= num:
            real_num = num
        else:
            real_num = free_space

        # case: plug 够
        if self.plug.position.real_material.amount >= real_num:  # 够
            if self.socket.position.real_material == None:  # 插座没有物料
                m = self.plug.position.real_material     # 材料
                m2 = copy.copy(m)               # 复制一份；
                m.amount -= real_num    # 减去
                m2.amount = real_num    # 数量赋值
                self.socket.position.real_material = m2
                return

            else:  # 插座有物料
                self.plug.position.real_material -= real_num
                self.socket.position.real_material -= real_num
                return

        else:       # 不够
            if self.socket.position.real_material == None:  # 插座没有物料
                self.socket.position.real_material = self.plug.position.real_material
                self.plug.position.real_material = None  # 直接转移
                return

            else:   # 插座有物料
                self.socket.position.real_material += self.plug.position.real_material
                del self.plug.position.real_material    # 删除插头的；
                return
