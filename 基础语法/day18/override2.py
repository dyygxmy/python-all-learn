
class A:
    def work(self):
        print("A类的work方法被调用")

class B(A):
    def work(self):
        print("B类的work方法被调用")

    def dowork(self):
        self.work()

    def dowork2(self):
        super(B, self).work() # A类的work方法被调用

    def dowork3(self):
        super().work() # A类的work方法被调用 推荐方法

    def dowork4(self):
        super(__class__,self).work() # 可能会出问题，不建议使用

b = B()
b.work() # B类的work方法被调用
A.work(b) # A类的work方法被调用 该调用方式不适合编程思想，用下面的方式

super(B,b).work() # A类的work方法被调用

b.dowork() # B类的work方法被调用

b.dowork2() # A类的work方法被调用
b.dowork3() # A类的work方法被调用
b.dowork4() # A类的work方法被调用