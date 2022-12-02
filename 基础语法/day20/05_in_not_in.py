# 此示例示意 in / not in 运算符的重载

class MyList:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __contains__(self, item):
        for x in self.data:
            if x == item:
                return True
        return False

L1 = MyList([1,-2,3,-4,5])
x = 1
if x in L1:
    print(x,"在L1中")
else:
    print(x,"不在L1中")