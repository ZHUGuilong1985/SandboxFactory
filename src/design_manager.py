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
            self.material_list .append(material_factory.load_resource(item))
