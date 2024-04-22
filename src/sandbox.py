from material import MaterialFactory
from solution_layer import Factory


class Sandbox():
    # 对应存档文件
    # 管理资源，layout
    # 运行
    # 记录运行结果
    # 输出

    def __init__(self):
        self.resource = None  # 资源
        self.instance = None  # 实例

        self.ftys = []  # 工厂列表

        self.ftys[0].build(self.resource['factories'][0])  # 建造第一工厂

    def load_resource(self, resource):
        # read resource from dict.

        self.resource = resource

    def instance_all(self):
        # 将资源里面的所有材料全部初始化
        materials_items = self.resource['materials']
        material_list = []
        material_factory = MaterialFactory()
        for item in materials_items:
            material_list.append(material_factory.new_material(item))

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
