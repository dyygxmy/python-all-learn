
# 此程序示意运算符重载

class MyNumber:
    def __init__(self,v):
        self.data = v
    def __repr__(self):
        print("data:", self.data)
        return "MyNumber(%d)"%self.data
    def __add__(self, other):
        print("__add__方法被调用")
        return MyNumber(self.data + other.data)
    def __sub__(self, other):
        print("__add__方法被调用")
        return MyNumber(self.data - other.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1+n2 # 等同于 n3 = n1.__add__(n2)
print(n3) # MyNumber(300)
print(n1-n2)