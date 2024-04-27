from material import ResourceFactory
from workshop import Factory

from layout import Layout
from design_manager import DesignManager


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

    def __init__(self, file_path=None):
        # resource list, include resource, formula, station, section, workshop, factory
        # couple of layouts. include layouts

        self.dict_all = None

        self.design_manager = None  # 设计管理器
        self.layouts = []

        self.load_data_from_disk(file_path)  # load data

        self.design_manager = self.new_design_manager(
            self.dict_all["design_data"])
        self.layouts[0] = self.new_layout(self.dict_all["layout"])

    def build_factory(self):
        # build factory
        self.ftys.append(Factory())

    def add_resource_to_factory(self):
        # add resource to factory
        pass

    def run(self):
        print("sandbox running. ")

    def new_layout(self, dict):
        # create layout.

        lyt = Layout(dict)
        if lyt:
            return lyt
        else:
            return None

    def new_design_manager(self, dict):
        dm = DesignManager(dict)
        if dm:
            return dm
        else:
            return None

    def write_data_to_disk(self, layout, file_path):
        # write resource to disk
        pass
        
    def load_data_from_disk(self, file_path):
        # read resource from disk
        if file_path:
            self.dict_all = self.load_data_from_disk(file_path)  # 导入默认文件
        else:
            self.dict_all = self.load_data_from_disk('./default.json')
