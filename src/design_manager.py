from material import ResourceFactory


class DesignManager: 
    # manager all design resource.

    def __init__(self, dict):
        
        self.dict = dict # all the data. 
        self.material_list = []

    def load_data(self): 
        
        self.load_resource(self.dict["resource"])
        self.load_formulas()
        self.load_stations()
        self.load_section()
        self.load_workshop()
        self.load_factory()

    def load_resource(self, lst):
        # load materials.
        material_factory = ResourceFactory()

        self.material_list.clear()
        for item in lst:
            self.material_list.append(material_factory.load_resource(item))

    def load_formulas(self,lst):
        # load formulas

        
        pass

    def load_stations(self):
        pass

    def load_section(self):
        pass

    def load_workshop(self):
        pass

    def load_factory(self):
        pass

    def get_object_by_id(self, id):
        for item in self.material_list:
            if item.id == id:
                return item

        return None
    