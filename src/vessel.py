


from constant import TIME_UNIT
from position import Position


class Vessel:
    '''
    point的反应容器，相当于公式；可以接收公式；
    几种反应容器：
    1. 加工厂；
    2. 连接器、传送带
    3. 仓库；
    4. 发生器；
    5. 处理厂；
    '''

    def __init__(self, name=None, formula=None):

        self.name = name

        self.positions:Position = []          # 容器
        self.timer = 0               # 计时器, min
        self.is_processing = False   # 是否在反应中，反应中，输入、输出均锁定；

        self.formula = formula          # 公式

        self.set_positions(formula)     # 设置容器

    def check_condition(self):
        # in端：
        # hold端
        # out端，为空。如果不为空，会造成堵塞；
        # 按照公式检查：

        for i in self.formula.material_positions:

            if i.type_material == "in":
                for j in self.positions:
                    if j.filter.material_name == i.material_name:
                        if j.real_material.amount < i.num:  # 不足
                            return False

            elif i.type_material == "out":
                for j in self.positions:
                    if j.filter.material_name == i.material_name:
                        if j.real_material.amount > 0:  # 滞留
                            return False

            elif i.type_material == "hold":
                for j in self.positions:
                    if j.filter.material_name == i.material_name:
                        if j.real_material.amount < i.num:  # 不足
                            return False

            else:   # other
                continue

        return True

    def reaction(self):
        '''
        检查容器位子，
        符合条件，
            就开始计时，
            时间到后，
            就删除原来的物料，
            再添加新的物料
        '''
        if not self.is_processing:           # 没有在反应中
            if self.check_condition():      # 符合反应条件，启动反应
                self.timer = 0              # 重置计时器
                self.timer += TIME_UNIT     # 加上一个时间周期
                self.is_processing = True    # 锁定进程
                return
            else:   # 不符合反应条件
                return

        else:  # 在反应中
            self.timer += TIME_UNIT  # 加上一个时间周期

            if self.timer >= self.formula.time:  # 到达、超过反应时间
                for i in self.positions:
                    if i.pst_tp == "in":
                        i.real_material.amount = 0
                    elif i.pst_tp == "out":
                        i.real_material.amount = i.volume  # 等于设置产出；
                    elif i.pst_tp == "hold":
                        pass
                    else:  # other
                        pass
                # 重置参数
                self.timer = 0
                self.is_processing = False
            else:
                pass

    def insert_position(self, position):
        '''
        增加空位
        '''
        self.positions.append(position)

    def set_positions(self, formula):
        self.positions.clear()  # 清空
        for i in formula.material_positions:
            self.positions.append(
                Position(i.type_material,  i.num, i.type_material + "_位", i.type_material))
