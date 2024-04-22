from material import ResourceFactory
from solution_layer import Factory

from layout import Layout

class Sandbox():
    '''
    功能清单：
    1. 导入一个默认文件
    2. 在默认文件的基础上，增加、修改资源；
    3. 文件修改时，另存为新的文件；
    4. 新建layout
    5. 在layout中，加载资源
    6. 运行layout
    7. 监测运行情况，保存运行数据
    8. 数据分析和展示
    '''

    def __init__(self,file_path = None): 

        

        if file_path:
            self.layout[0] = self.load_resource_from_disk(file_path)  # 导入默认文件
        else:
            self.layout[0] = self.load_resource_from_disk('./default.json')


        self.resource = None  # 资源
        self.instance = None  # 实例


        self.ftys = []  # 工厂列表

        self.ftys[0].build(self.resource['factories'][0])  # 建造第一工厂

    def init_objects(self):
        self.layout = []

    def load_resource(self, resource):
        # read resource from dict.

        self.resource = resource

    def instance_all(self):
        # 将资源里面的所有材料全部初始化
        materials_items = self.resource['materials']
        material_list = []
        material_factory = ResourceFactory()
        for item in materials_items:
            material_list.append(material_factory.new_resource(item))

    def build_factory(self):
        # build factory
        self.ftys.append(Factory())

    def add_resource_to_factory(self):
        # add resource to factory
        pass

    def run(self):
        #
        print("sandbox running. ")

    def new_layout(self):
        # 新建

        pass

    def new_element(self, element):
        # 新建
        
        pass

    def write_resource_to_disk(self,layout,file_path):
        # write resource to disk
        pass

    def read_resource_from_disk(self,file_path):
        # read resource from disk
        pass

