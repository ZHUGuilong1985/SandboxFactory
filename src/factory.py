from solution import Frame 

class Factory(Frame):
    '''
    工厂: 
    1. 工厂
    2. 外协厂
    3. 电网、固废处理站等等
    类似一个容器，可以看出一个循环

    实现逻辑：按照公式配置工段；

    结算单位
    资源的管理来源；

    factory is base element to run. It has a update clock. 
    '''

    def __init__(self, blueprint)  :
        self.__blueprint = blueprint
        self.__elementList = []  # 记录所有节点、连线

        self.material_storage = []  # 资源


    def add_resource(self):
        ''' 
        添加资源
        '''
        pass

    def add_monitor(self):
        ''' 
        添加监视器
        '''
        pass

    def add_point(self, points):
        ''' 
        添加点
        '''
        if self.inlist(points):
            return points
        else:
            points.build()  # 新建
            self.__elementList.append(points)
            

    def add_line(self, start, end):
        ''' 
        添加线
        1. 现阶段简化连接，默认有一个主连接口；

        2. 实际上，不是添加线。原来的两个点，其中必然有一个线；
        3. 实际上，是匹配输出口、输入口；
        '''
        start.outter = end.inner  # 暂时这么写吧
        end.inner = start.outter

    def build_by_link(self, link):
        ''' 
        按照链接建设工厂
        '''
        start = self.add_point(link.start)   # 定义起点
        end = self.add_point(link.end)       # 定义终点
        self.add_line(start, end)            # 定义连线
        return None

    def build(self):
        '''
        1. 新建一个厂区；
            按照蓝图配置工位

            1. 建立工位
                按照配方配置工位
                2. 添加设备
                3. 添加人员；
            4. 添加仓库
            添加电力接口，并计费；
            添加动力站，并计费；
            添加固废处理处理，并计费；
            添加水管，并计费；

        2. 添加资源

        3. 添加规则

        4. 添加监视器、修改汇报机制

        5. 启动工厂

        6. 添加配方

        1. 添加现金

        添加商店（配置好材料等）

        5. 设计一个工段，添加人员、设备和配方；
        设计下一工段，添加人员、设备、配方；

        连接各个工段；

        配置好各个材料（包括水电气、材料等所有）等供应点

        选择需要检测等内容和展示方式；

        具备运行条件；
        这里指的运行条件是工厂情况硬件具备，但是不等于材料就能进行；应为材料有供货期；

        这里可以根据保存的配置文件，来自动配置工厂
        '''

        # 设置蓝图游历起点
        self.__blueprint.resetPointer()

        link = self.__blueprint.getNextLink()  # 游历蓝图
        while link != None:  # 没有下一个链接，退出
            self.build_by_link(link)
            link = self.__blueprint.getNextLink()  # 移动指针

        # 添加资源
        self.add_resource()  # 增加资源；

        # 添加规则
        self.add_rule()  # 增加规则；

        # 添加监视器
        self.add_monitor()  # 增加监视器；

        return True  # 创建成功

    def run(self):
        # 启动运行
        print("I am running. ")
