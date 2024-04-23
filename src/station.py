from solution import Frame, Point, Line


class Station(Point):

    def __init__(self, name, id,  resource, formula):
        super().__init__(name)  # 继承父类

        self.name = name
        self.object_id = id

        self.resources = []
        self.formulas = []

        # local data
        self.aera = None

    def build(self):
        if self.__Configuration == None:
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
