


from definition import Definition


class Line(Definition):
    ''' 
    线. 特殊的点，只包含：一个插座、一个插头、一个容器。容器不具公式，只是传递。
    '''

    def __init__(self, name=None):
        '''
        创建连接，并连接到两个对象
        '''
        self.name = name

        self.sockets = []
        self.sockets.append(Socket(self, 0))    # socket
        self.plugs = []
        self.plugs.append(Plug(self, 0))        # plug，插头

        self.vessel = Vessel("-", "-")           # 容器

        Element.element_list.append(self)

        self.report()

    def draw(self):
        pass

    def __str__(self):
        return self.name

    def report(self):
        print(f"Line {self.name} created. ")

    def refresh():
        pass

    def refresh_pre(self):
        pass

    def refresh_process(self):
        pass

    def refresh_post(self):
        pass
