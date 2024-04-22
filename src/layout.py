
from material import ResourceFactory

class Layout:
    
    def __init__(self, document):
        self.layout_name = document

        self.resource = {
            'materials':[],
            'workers':[],
            'machines':[]

        }


        self.instance = {
            'materials':[],
            'workers':[],
            'machines':[]
        }

        fty = ResourceFactory()
        for item in document['resource']:
            fty(item)
            

