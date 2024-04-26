# instance class

from solution import Element


class Instance(Element): 
    # 基于definition的实力化
    # 每一个instance都必须有definition_id

    def __init__(self, definition_id):
        super.__init__()

        self.definition_id = definition_id # 定义

        self.instance_id = None
        self.quantity = 0

    def unlink(self):
        # 解除连接关系
        # 具体操作就是复制一份definition, 并实例化

        pass
