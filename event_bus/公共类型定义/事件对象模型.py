
from typing import Dict, Any, Optional, List

import datetime
import uuid
from typing import Any, Dict, List

# -------------------------------------------------------------
# 订阅者事件返回模型
# 说明：用于存放每个订阅者处理事件后的返回信息
# -------------------------------------------------------------
import datetime
from dataclasses import is_dataclass, asdict
from typing import Any, Dict

from obj2dist import 可序列化基类 as 可序列化类基础模型


class 订阅者事件返回模型(可序列化类基础模型):
    def __init__(self, 订阅者名: str, 序号: int = None):
        self.序号: int = 序号 if 序号 is not None else -1  # 默认-1表示未设置
        self.订阅者名: str = 订阅者名
        self.状态: str = ""              # 可选，可在处理时更新
        self.成功:str = "成功"
        self.失败:str = "失败"
        self.数据: Any = None            # 处理结果，可为空

        self.订阅者处理耗时: float = 0.0   # 默认0.0，处理完成后更新
        self.错误信息: Optional[str] = None  # 处理过程中出现错误时赋值
        self.开始时间: Optional[datetime.datetime] = None  # 处理开始时赋值
        self.结束时间: Optional[datetime.datetime] = None  # 处理完成时赋值

# -------------------------------------------------------------
# 总线通用事件模型
# 说明：表示一个事件实例及其所有订阅者的返回信息
# -------------------------------------------------------------
class 总线通用事件模型(可序列化类基础模型):
    def __init__(self, 事件名: str, 订阅者列表: List[str]=None, 事件数据: Any = None):
        # 校验必需字段
        if not 事件名 :
            raise ValueError("事件名不能为空")

        self.事件名: str = 事件名
        self.订阅者列表: List[str] = 订阅者列表
        self.事件uuid: str = uuid.uuid4().hex[:8]  # 8位短UUID
        self.事件提交时间: Optional[datetime.datetime] = None  # 提交时赋值
        self.事件数据: Any = 事件数据
        self.事件结束时间: Optional[datetime.datetime] = None  # 所有处理完成时赋值
        self.时间总耗时: float = 0.0   # 默认0.0，处理完成后更新



        # 初始化每个订阅者的返回模型
        if 订阅者列表 :

            self.事件返回: Dict[str, 订阅者事件返回模型] = {
                名: 订阅者事件返回模型(订阅者名=名,序号=索引) for 索引,名 in enumerate(订阅者列表,start=1)

            }
    def 计算总耗时(self):
        总耗时=0.0
        for 订阅者, 返回模型 in self.事件返回.items():
            总耗时+=返回模型.事件处理耗时
        return 总耗时
    def 重新初始化(self,订阅者列表: List[str]=None, 事件数据: Any = None):
        self.订阅者列表=订阅者列表
        self.事件数据=事件数据
        if 订阅者列表 :
            self.事件返回: Dict[str, 订阅者事件返回模型] = {
                名: 订阅者事件返回模型(订阅者名=名,序号=索引) for 索引,名 in enumerate(订阅者列表,start=1)

            }
        else:
            self.事件返回={}



class 日志事件:
    """
    日志事件数据结构，前端模块生成后发布到总线。
    """
    def __init__(self, 等级: str, 消息: str, 包名: str, 函数名: str, 行号: int, 时间戳: float):
        self.等级 = 等级
        self.消息 = 消息
        self.包名 = 包名
        self.函数名 = 函数名
        self.行号 = 行号
        self.时间戳 = 时间戳
        self.时间=datetime.datetime.fromtimestamp(时间戳).strftime("%Y-%m-%d %H:%M:%S")

    def 转字典(self) -> Dict[str, Any]:
        return {
            "等级": self.等级,
            "消息": self.消息,
            "包名": self.包名,
            "函数名": self.函数名,
            "行号": self.行号,
            "时间戳": self.时间戳
        }


