"""
全局解释器锁：GIL
单CPU执行操作
GIL的作用：多线程情况下必须存在资源的竞争，GIL是为了保证在解释器级别的线程唯一使用共享资源（cpu）。


同步锁的作用：为了保证解释器级别下的自己编写的程序唯一使用共享资源产生了同步锁


死锁：指两个或两个以上的线程或进程在执行程序的过程中，因争夺资源而相互等待的一个现象


递归锁：
在Python中为了支持同一个线程中多次请求同一资源，Python提供了可重入锁。
这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，
从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源


悲观锁：操作任务时回认为别人也会修改数据，因此操作数据时直接把数据锁住，
知道操作完成才会释放锁，上锁期间不允许其他人修改。


乐观锁：操作任务时认为别人不会同时修改数据，因此不会上锁，
只会在执行更新的时候判断一下在此期间是否有人修改了数据
如果有人修改了数据则放弃操作，否则执行操作。

悲观锁：写入频繁
乐观锁：读取频繁

"""

# 同步锁
import time
import threading

R = threading.Lock()

def sub():
    global num
    R.acquire() # 加锁，保证同一时刻只有一个线程可以修改数据
    num -= 1
    R.release() # 修改完成就可以解锁
    time.sleep(1)


num = 100  # 定义一个全局变量
l = []  # 定义一个空列表，用来存放所有的列表
for i in range(100):  # for循环100次
    t = threading.Thread(target=sub)  # 每次循环开启一个线程
    t.start()  # 开启线程
    l.append(t)  # 将线程加入列表l
for i in l:
    i.join()  # 这里加上join保证所有的线程结束后才运行下面的代码
print(num)
# 输出结果为0


#死锁
import time
import threading

A = threading.Lock()
B = threading.Lock()
import threading


class obj(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.a()   # 如果两个锁同时被多个线程运行，就会出现死锁现象
        self.b()
    def a(self):
        A.acquire()
        print('123')
        B.acquire()
        print(456)
        time.sleep(1)
        B.release()
        print('qweqwe')
        A.release()
    def b(self):
        B.acquire()
        print('asdfaaa')
        A.acquire()
        print('(⊙o⊙)哦(⊙v⊙)嗯')
        A.release()
        B.release()
for i in range(2):  # 循环两次，运行四个线程，第一个线程成功处理完数据，第二个和第三个就会出现死锁
    t = obj()
    t.start()


#递归锁
import time
import threading

A = threading.RLock()  # 这里设置锁为递归锁
import threading

class obj(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.a()
        self.b()

    def a(self): # 递归锁，就是将多个锁的钥匙放到一起，要拿就全拿，要么一个都拿不到
        # 以实现锁
        A.acquire()
        print('123')
        print(456)
        time.sleep(1)
        print('qweqwe')
        A.release()
    def b(self):
        A.acquire()
        print('asdfaaa')
        print('(⊙o⊙)哦(⊙v⊙)嗯')
        A.release()
for i in range(2):
    t = obj()
    t.start()