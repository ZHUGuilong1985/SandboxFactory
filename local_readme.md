
开发手册
---

# 主要任务：

1. 定义一个工序
2. 连接一组工序；

## 如何定义一个工序

输入：材料
环境：场地、设备
能源：水、电、气和其他
人员：操作工人

输出：产品A的半成品1

### 评价指标

评价指标：
1. 材料损耗：
   1. 作为基础工序时，可以直接定义；
2. 人员利用率：
   1. 作为基础工序时，可以直接定义；
3. 良品率：
   1. 影响因素：人为操作的因素
   2. 机器的因素，可能会坏；保养不善的话；
4. 工序成本
   1. 指的是增加的成品。比如，材料损耗、水电气、人员工资等；

## 如何定一个产品生产线

输入原材料
能源
生产线 x N
人工 x N

产品

解决一个算法的问题：
120kg的材料，得到100kg的产品；
- 120kg原料，加热，无损耗；——成本：120原料，20的加工费；每公斤为；1220。
- 第一道工序，提纯，去掉5%，1140，——成本：原材料，1220，损耗5%（61），加工费80，则输出为114kg，多少钱？1239元（1220*0.95+80）；，本道工序成本19元；
- 第二道工序，热轧，去掉2%，——成本
- 第三道工序，切割，去掉3%，——成本
- 打标记，增加1%的成本； ——成本

如此条件下，如何计算成本分配？

120kg * 10，1200元；
100 * 20，2000元；

cost？

成本，要算上前置工序的所有成本，进行叠加；

通过底层逻辑建模，建立程序；图形化的事情，往后放；

图形化的模块如何搭建？

公司、车间（可以不管）、工段、工位；

每件的计算？每个月的计算？

如何把时间、成本、人员等细化到每个工序里面，进行汇总；
靠底层逻辑来决定；

产品流速， 20 mim/件；或者 5 件/hour；
操作人员跟随，操作人员等成本（这一部分可以细化，各个时段的成本等等）；
输入的主材料、辅助材料的流速；
良品率，成本；
损耗，成本；
设备启动运营的非循环成本（热机、冷却等等；）
流出速度，制造速度，50min/件，2件/hour；

旭光，


                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Mammal    │           │    Bird     │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
└─────────┘  └─────────┘  └─────────┘  └─────────┘

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99



Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

# 达到什么样的目的？



# 程序如何来用？

1. 通过excel来定义材料、工位、人员、能源等等
2. 如果有条件，可以写材料、定义图形化界面，来配置；
3. 通过编写配置文件，来定义工厂，设置运行条件和约束；
4. 点击开始，运行；
5. 监控；

1. 需要增加材料时，通过改变配置文件来调整；

# 开发日志

2023-09-23：
1. 今天主要解决建立工厂的流程函数；
2. 计算和更新的问题暂缓；

2023-09-24:
1. 写factory
2. 写blueprint, configuration, formula
3. 创建素材
4. 清理注释

2023-10-03:
1. 梳理程序的结构；
2. 

模拟一个简单的过程：
1. 预浸料固化；
2. 机械加工；
3. 前面有几个发生器；
4. 后面有一个收集器；
5. 计算产能和费用



2023-10-03:
1. 加入一个材料，在里面流动；
2. 加入过滤器，过滤；
3. 定制流动方向；

2023-10-05：
1. 从A装入一个材料；
2. 一定周期后，自动运送到D

2023-10-15:
1. 把point改为 新的名称；
2. point和line本质上都一样，只有vessel不一样；

# 程序运行流程

程序定义的：
1. 设备
2. 人员

运行中定义的：
1. 增加材料
2. 修改配方

程序的配置文件：

如何考虑检验站等问题？

如果从底层逻辑看，可以分为：
1. 设备
2. 人员
3. 材料
4. 配方
5. 统计方法
6. 小组件。

layout (大布局) > factory（工厂） > workshop（车间） > section(工段) > station （工位）

这个程序里，不涉及工厂基本元素；搞清楚底层逻辑；

5000行之内，能不能搞定？

核心算法：处理器的核心算法
1. 工位自检，包括人员、设备等等；
1. 按照公式，检查输入；
    输入可以分为一次性输入和持续输入；
    持续输入如果不满足条件，可以暂停，也可以报废；比如停电。
2. 具备条件，进入生产周期；
    生产周期由公式决定；
3. 周期完成后，输出产出物

输出：
现金流
产品流（电力、水力、压缩空气也包含在内）

核心算法：循环的核心算法

1. 一个需要解决的问题：
如何定义半成品


# 典型工作流程

1. 打开界面
2. 打开已经配置好的工厂，或者新建工厂
3. 新建或者获取材料数据库；
4. 组件工位
5. 组件配方
6. 连接，启动工厂
7. 监控，查看运行状态
8. 输出结果

## 界面

采用CLI模式，命令行界面；

## 材料数据库

# 转移的信息

'material mould. 定义具体的材料、设备、人员等等，相当于Excel表格。'
'''
系统自带的材料库
材料归类：
1. 预浸料
2. 天然气；
5. 铝合金
6. 废水
7. 电
8. 筒装材料；
9. 胶带
3. 人员
4. 设备；
'''


# 有用的资料

在 Python 中使用 JSON 时，确保正确处理编码问题非常重要。以下是一些解决编码问题的方法：

1. **指定编码**：
   - 当将数据写入 JSON 文件时，确保指定正确的编码。默认情况下，`json` 模块使用 UTF-8 编码。
   - 示例代码：
     ```python
     import json

     # 将数据写入 JSON 文件（指定 UTF-8 编码）
     with open('data.json', 'w', encoding='utf-8') as f:
         json.dump(data, f)
     ```

2. **处理特殊字符**：
   - 如果 JSON 数据中包含特殊字符（例如 Unicode 字符、换行符等），`json.dumps()` 方法会自动处理它们。
   - 示例代码：
     ```python
     import json

     # 处理特殊字符
     data = {'message': 'Hello, 世界\n'}
     json_string = json.dumps(data, ensure_ascii=False)
     print(json_string)
     ```

3. **读取 JSON 文件时指定编码**：
   - 在读取 JSON 文件时，确保指定正确的编码。
   - 示例代码：
     ```python
     import json

     # 从 JSON 文件读取数据（指定 UTF-8 编码）
     with open('data.json', 'r', encoding='utf-8') as f:
         loaded_data = json.load(f)
     ```

4. **处理复杂数据类型**：
   - 如果 JSON 数据包含复杂的数据类型（例如复数、小数等），你可以自定义编码和解码方法。
   - 示例代码：
     ```python
     import json
     import decimal

     # 自定义解码方法
     def as_complex(dct):
         if '__complex__' in dct:
             return complex(dct['real'], dct['imag'])
         return dct

     # 使用自定义解码方法
     json_string = '{"__complex__": true, "real": 1, "imag": 2}'
     complex_number = json.loads(json_string, object_hook=as_complex)

     # 自定义浮点数解析方法
     json_string = '1.1'
     parsed_float = json.loads(json_string, parse_float=decimal.Decimal)
     ```

总之，使用 `json` 模块时，确保正确处理编码问题，以避免出现乱码或其他不良影响。希望这些方法对你有帮助！如果你还有其他问题，欢迎继续提问。😊

源: 与必应的对话， 2024/4/20
(1) json — JSON encoder and decoder — Python 3.12.3 .... https://docs.python.org/3/library/json.html.
(2) PythonでJSON出力する際、日本語が文字化けする件 - Qiita. https://qiita.com/kurousa/items/f59ea18db9e33ef446f0.
(3) Python JSON encoding - Stack Overflow. https://stackoverflow.com/questions/983855/python-json-encoding.
(4) Pythonでエンコーディングを指定してJSONファイルの文字コード .... https://ittrip.xyz/python/resolve-json-encoding-issue-python.



# 代表事项

解决solution和layout之间的关系。
