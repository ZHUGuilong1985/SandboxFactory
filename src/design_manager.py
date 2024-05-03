from formula import FormulaFactory
from material import ResourceFactory


class DesignManager:
    # manager all design resource.

    def __init__(self, dict):

        self.dict = dict  # all the data.

        self.material_list = []
        self.formulas_lst = []  # contains materials
        self.stations_lst = []  # contains materials and formulas
        self.section_lst = []   # contains ...
        self.workshop_lst = []  # contains ...
        self.factory_lst = []   # contains ...

        self.load_data()  # load the data

    def load_data(self):

        self.load_resource(self.dict["resources"])
        self.load_formulas()
        self.load_stations()
        # self.load_section()
        # self.load_workshop()
        # self.load_factory()

    def load_resource(self, lst):
        # load materials.
        material_factory = ResourceFactory(self)

        self.material_list.clear()
        for item in lst:
            self.material_list.append(material_factory.load_resource(item))

    def load_formulas(self, lst):
        # load formulas
        formula_factory = FormulaFactory(self)

        pass

    def load_stations(self):
        pass

    def load_section(self):
        pass

    def load_workshop(self):
        pass

    def load_factory(self):
        pass

    def get_object_by_sbid(self, sbid):
        # find object by sbid
        for item in self.material_list:
            if item.sbid == sbid:
                return item

        return None

    def show_info(self):
        # show info in terminal
        for item in self.material_list:
            item.show_info()

    def run(self):
        while True:
            input_str = input("Enter command: ")
            if input_str == "exit":
                break
            elif input_str == "help":
                pass
            elif input_str == "new material":
                # command: new_material name price unit
                self.new_material('material1', '100', 'pcs')

            elif input_str == "new formula":
                pass
            else:
                pass

    def new_material(self, name, price, unit):
        dict = {
            "name":  name,
            "price": price,
            "unit":  unit
        }
        # create new material
        material_factory = ResourceFactory(self)
        n_material = material_factory.create_resource(dict)
        self.material_list.append(n_material)

        n_material.show_info()  # 显示信息

    def pack_data(self):
        # pack all data
        return None

    '''
    command list:
    1. new_material: name = 7075, price = 20, unit = pcs
    2. new_formula:  
    CRUD: create, read, update, delete
    
    create material:
    read material:
    update material:
    delete material:

    create material: name,7075;price,20;unit,pcs.

    '''
