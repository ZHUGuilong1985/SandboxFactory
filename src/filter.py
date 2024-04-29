# 添加一条信息，from

class Filter:
    '''
    过滤器
    '''

    def __init__(self, material_name:   str, parent=None):
        # 按名字过滤，当前是单一过滤器
        self.material_name = material_name
        self.parent = parent            # 安装位置

    def check(self, obj_name):
        if obj_name == self.material_name:
            return True
        else:
            return False

    def __eq__(self, __value) -> bool:
        '''
        只要过滤装置名称相同，就返回True
        '''
        if self.material_name == __value.material_name:
            return True
        else:
            return False
