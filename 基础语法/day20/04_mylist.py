# 此示例示意一元运算符的重载

class MyList:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __neg__(self):
        # L = [-x for x in self.data] # 所有的元素都加个负号
        L = (-x for x in self.data)  # 可以用生成器表达式，不用生成变量再消掉了
        return MyList(L)

L1 = MyList([1,-2,3,-4,5])
print('L1=',L1)
L2 = -L1
print('L2=',L2)