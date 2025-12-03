# 文件路径: src/utils/日志事件生成工具.py
# 中文说明：
# 本模块提供一个中文命名的“日志事件生成器”，用于生成标准化日志事件，
# 方便总线适配。特点：
#   1. 自动捕获调用信息：包名、函数名、行号、时间戳
#   2. 日志等级支持：DEBUG/INFO/WARNING/ERROR/CRITICAL
#   3. 简单易用中文 API：debug/info/warning/error/critical
#   4. 与总线解耦，可随时发送事件到总线
from event_bus.公共类型定义.事件对象模型 import 日志事件
import inspect
import time



# ----------------------------------------------------------------------
# 日志事件生成器
# ----------------------------------------------------------------------
class 日志事件生成器:
    """
    中文命名日志事件生成器，提供 debug/info/warning/error/critical 方法
    生成日志事件并返回，方便总线发送。
    """
    def __init__(self):
        pass  # 可以扩展默认等级、全局属性等

    def _生成事件(self, 等级: str, 消息: str, 帧:inspect.currentframe().f_back = None) -> 日志事件:
        调用信息 =_获取调用者信息(帧)
        return 日志事件(
            等级=等级,
            消息=消息,
            包名=调用信息["包名"],
            函数名=调用信息["函数名"],
            行号=调用信息["行号"],
            时间戳=time.time()
        )

    def debug(self, 消息: str, 调用帧:inspect.currentframe().f_back = None) -> 日志事件:
        return self._生成事件("DEBUG", 消息, 调用帧)

    def info(self, 消息: str, 调用帧:inspect.currentframe().f_back = None) -> 日志事件:
        return self._生成事件("INFO", 消息, 调用帧)

    def warning(self, 消息: str, 调用帧:inspect.currentframe().f_back = None) -> 日志事件:
        return self._生成事件("WARNING", 消息, 调用帧)

    def error(self, 消息: str, 调用帧:inspect.currentframe().f_back = None) -> 日志事件:
        return self._生成事件("ERROR", 消息, 调用帧)

    def critical(self, 消息: str, 调用帧:inspect.currentframe().f_back = None) -> 日志事件:
        return self._生成事件("CRITICAL", 消息, 调用帧)

# ----------------------------------------------------------------------
# 使用示例
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # 实例化日志事件生成器
    日志生成器 = 日志事件生成器()

    # 生成日志事件（模拟模块调用）
    event1 = 日志生成器.debug("这是调试信息")
    event2 = 日志生成器.info("普通信息")
    event3 = 日志生成器.warning("警告信息")
    event4 = 日志生成器.error("错误信息")
    event5 = 日志生成器.critical("严重错误")

    # 输出事件字典（模拟总线发送）
    for e in [event1, event2, event3, event4, event5]:
        print(e.转字典())
