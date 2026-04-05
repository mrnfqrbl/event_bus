import inspect
import threading
import asyncio
from asyncio import futures
from collections import defaultdict
from typing import Callable, List, Dict, Any


from event_bus.公共类型定义.事件对象模型 import 总线通用事件模型
from event_bus.总线.日志事件生成工具 import 日志事件生成器 as 日志事件生成器类
# from event_bus.总线.总线内嵌模块bak.http框架 import 总线内嵌http框架
# from event_bus.总线.总线内嵌模块bak.http服务器 import 总线内嵌http服务器
from event_bus.总线.工具函数类 import 总线工具函数

class 事件总线:
    def __init__(self):
        self._订阅表: Dict[str, List[tuple[str, Callable]]] = defaultdict(list)
        self._锁 = threading.Lock()
        self.日志事件生成器=日志事件生成器类()
        # self.loop=None
        # self._get_loop()


        self.总线工具函数=总线工具函数



        # self.总线内嵌http框架=总线内嵌http框架(总线=self)
        # self.总线内嵌http服务器=总线内嵌http服务器


    def _get_loop(self):
        # 🔥 唯一正确、全版本、全线程兼容的获取 loop 方式
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)


        return loop


    async def _执行异步回调(self, fn, 订阅者,*args, **kwargs):
        try:
            await fn(*args, **kwargs)
        except Exception as e:
            print(f"异步事件回调异常: {订阅者} -> {e}")
    def 订阅(self, 事件名: str, 订阅者: str, 处理函数: Callable):
        with self._锁:
            self._订阅表[事件名].append((订阅者, 处理函数))
    def 取消订阅(self, 事件名: str, 订阅者: str):
        with self._锁:
            self._订阅表[事件名] = [
                (sub, fn) for sub, fn in self._订阅表[事件名] if sub != 订阅者
            ]

    def 发布(self,*args,**kwargs) -> 总线通用事件模型:
        loop = self._get_loop()
        事件=self.异步发布(*args,**kwargs)
        # asyncio.create_task(事件.等待完成())

        return 事件



    def 异步发布(self, 事件名: str, 事件数据: Any) -> 总线通用事件模型:
        loop = self._get_loop()
        订阅者映射 = self._订阅表[事件名]

        事件 = 总线通用事件模型(事件名=事件名,订阅者列表=[订阅者 for 订阅者, _ in 订阅者映射],事件数据=事件数据)
        事件.事件提交时间 = self.总线工具函数.获取当前时间()

        with self._锁:
            if not self._订阅表[事件名]:
                self.发布日志(级别="warning", 消息=f"事件名 {事件名} 没有订阅者")

                事件.完成一个()
                self.发布事件记录(事件)
                return 事件


            # 总数 = len(订阅者映射)
            # 事件.初始化(订阅者列表=[订阅者 for 订阅者, _ in 订阅者映射], 事件数据=事件数据)
            # 事件.初始化等待(总数)  # 👈 初始化计数器



        # ===================== 统一调度 + 统一计数 =====================
        for 订阅者, 处理函数 in 订阅者映射:
            if asyncio.iscoroutinefunction(处理函数):
                # 异步包装：执行完自动计数
                async def 异步任务():
                    print(f"异步事件回调: {订阅者}")
                    try:

                        await 处理函数(数据=事件数据, 事件=事件)
                    except Exception as e:
                        raise e
                    finally:
                        事件.完成一个()

                loop.create_task(异步任务())



            else:
                # 同步包装：丢线程池，执行完自动计数
                loop.run_in_executor(
                    None,
                    lambda: (
                        处理函数(数据=事件数据, 事件=事件),
                        事件.完成一个()
                    )
                )

        # 注意：这里不再立即设置结束时间！由最后一个回调设置

        self.发布事件记录(事件)
        return 事件








    #总线日志区域
    def 发布日志(self, 级别: str, 消息: str, ):
        调用帧=inspect.currentframe().f_back
        日志事件=self.日志事件生成器._生成事件(级别,消息,调用帧)
        订阅者映射 = self._订阅表["日志"]
        for 订阅者, 处理函数 in 订阅者映射:
            处理函数(日志事件)
    def 发布事件记录(self,事件:总线通用事件模型):
        订阅者映射 = self._订阅表["记录事件"]
        for 订阅者, 处理函数 in 订阅者映射:
            处理函数(事件)

    def 获取订阅者列表(self, 事件名: str) -> List[str]:
        with self._锁:
            return [订阅者 for 订阅者, _ in self._订阅表[事件名]]

    def 获取所有事件名(self) -> List[str]:
        with self._锁:
            return list(self._订阅表.keys())


if __name__ == "__main__":
    pass
