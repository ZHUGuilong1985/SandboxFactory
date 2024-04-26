


class Position:
    '''
    一个过滤器、一个容器
    position之间的物资传递，作为重点动作考虑；
    '''

    def __init__(self, filter, volume=0, name=None, pst_tp="other"):
        self.name = name 
        self.real_material = None   # 所装材料
        # self.quantity = 0 
        self.volume = volume        # 容量. 0 代表不限量
        self.filter = filter        # 按照名字过滤
        self.pst_tp = pst_tp        # in,out,hold,other

    def isEmpty(self):
        if self.real_material == None:
            return True
        else:
            return False
