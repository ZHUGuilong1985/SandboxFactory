from material import ResourceFactory
from constant import TIME_UNIT


class Layout:
    '''
    a instance in memory. 
    '''

    def __init__(self, dict):

        self.layout_name = dict

        self.instance = {
            'materials': [],
            'workers': [],
            'machines': []
        }

        fty = ResourceFactory()
        for item in dict['resource']:
            fty(item)

        self.instance_list = []

    def load_data(self):
        # load all date into memory.

        # instance
        self.load_layout()

    def add_instance(self, type_id):
        # add a instance to layout from memory resource list.
        pass

    def run(self, delay_time=60):
        # run the layout, and delay 60min.
        time_count = 0
        while time_count < delay_time:
             # update all the instance. 
            for item in self.instance_list:
                item.update()

            time_count += TIME_UNIT
        print(f'Finished. ')
