# 文件路径: setup.py

"""
中文化 Python 包安装配置示例
流程原理：
1. 定义包名、版本、作者信息和描述。
2. 指定包含的模块/包，可以使用中文化模块名。
3. 支持本地开发安装（pip install .）和打包上传。
"""

from setuptools import setup, find_packages

# 配置安装信息
setup(
    # PyPI 上传用英文包名，兼容 pip 上传
    name="event_bus"

    # 包版本号
    ,version="0.1.0"

    # 作者
    ,author="null"

    # 作者邮箱
    ,author_email="null@example.com"

    # 简短描述
    ,description="事件总线"

    # 详细描述
    ,long_description="这是一个事件总线，支持发布和订阅事件。"

    ,long_description_content_type="text/markdown"

    # 项目主页，可选
    ,url="https://github.com/yourusername/event_bus"

    # 自动查找包，包括中文模块名
    ,packages=find_packages()

    # Python 最低版本
    ,python_requires='>=3.7'

    # 依赖包列表
    ,install_requires=[
        "pydantic>=2.12.5",
        "obj2dist @ git+https://github.com/mrnfqrbl/obj2dist.git@main#egg=obj2dist"


    ]

    # 分类信息，可选
    ,classifiers=[

    ]
)
