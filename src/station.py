from point import Point
from solution import Frame,    Line


class Station(Point):

    def __init__(self, name, sbid,  resource, formula):
        super().__init__(name)  # 继承父类

        self.sbid = sbid

        self.resources = []     # 加载资源
        self.formulas = []      #

        # local data
        self.aera = None

    def build(self):
        return

    def apply_formula(formula):
        pass

    def reset_formula():
        pass

    def report(self):
        print(self)

    def update(self):
        pass


class StationFactory():
    pass


class StationInstance():
    pass
