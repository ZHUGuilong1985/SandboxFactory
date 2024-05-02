from material import ResourceFactory
from factory import Factory

from layout import Layout
from design_manager import DesignManager

from init_default import SetupSystem


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

    def __init__(self, data_dict):
        # resource list, include resource, formula, station, section, workshop, factory
        # couple of layouts. include layouts

        self.dict_all = data_dict  # 数据字典

        self.design_manager = None  # 设计管理器
        self.layouts = []

        self.design_manager =  \
            self.new_design_manager(self.dict_all["design_data"])  # 创建设计管理器
        # self.layouts[0] = self.new_layout(self.dict_all["layout"])  # 创建layout

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
            self.dict_all = SetupSystem.load_setup(file_path)  # 导入默认文件
        else:
            self.dict_all = SetupSystem.load_setup('./default.json')

    def packed_all_data(self):
        # pack all data
        return None

    def run(self):
        '''
        command list:
        1. add material
        2. add formula
        3. add ...        
        '''
        while True:
            input_str = input("Enter command: ")
            if input_str == "exit":
                break
            elif input_str == "load":
                self.load_data_from_disk()
            elif input_str == "save":
                self.write_data_to_disk()
            elif input_str == "new_layout":
                self.layouts.append(self.new_layout(self.dict_all["layout"]))
            elif input_str == "run":
                self.run()
            elif input_str == "help":
                pass
            else:
                pass

        print("sandbox running. ")


def main():
    sb = Sandbox()
    sb.run()


if __name__ == '__main__':
    sb = Sandbox()
    sb.run()
