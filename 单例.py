"""

python  单例

单例模式:通常某一个类只有一个实例存在    节省内存避免不必要的支出
通过如下示例可看出第二次初始化并没有被进行。

"""

def Singleton(cls):
    _instance = {}

    def _singleton(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]

    return _singleton

@Singleton
class A(object):
    a = 1

    def __init__(self,x=0):
        self.x = x
        print(self.x)

a1 = A(2)
a2 = A(3)
