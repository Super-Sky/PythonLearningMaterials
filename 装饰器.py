"""
python 装饰器  简化代码组成  增强函数的功能

如下是一个计算函数运行时间的装饰器使用用例
"""

import time

# 定义装饰器
def time_calc(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        f = func(*args,**kwargs)
        exec_time = time.time()-start_time
        print(exec_time)
        return f
    return wrapper

@time_calc
def add(a,b):
    return a+b


if __name__ == '__main__':
    b = add(3,4)
    print(b)
