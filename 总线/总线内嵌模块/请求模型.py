




class 请求对象():
    """封装解析后的HTTP请求数据."""
    def __init__(self, 方法, 路径, 头部, 请求体, 查询参数=None):
        if 查询参数 is None:
            查询参数 = {}
        self.方法 = 方法
        self.路径 = 路径
        self.查询参数=查询参数
        self.头部 = 头部
        self.请求体 = 请求体



class 响应对象:
    """框架返回的响应对象，由服务器转换为HTTP字节流."""
    def __init__(self, 状态码=200, 头部=None, 内容=""):
        self.状态码 = 状态码
        self.头部 = 头部 or {"Content-Type": "text/plain; charset=utf-8"}
        self.内容 = 内容

