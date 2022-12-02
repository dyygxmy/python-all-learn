# 此示例示意索引index和切片slice运算符的重载

class MyList:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)'%self.data

    def __getitem__(self, item):
        if type(item) is slice:
            print("切片操作")
        elif type(item) is int:
            print("索引操作")
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        pass


L1 = MyList([1,-2,3,-4,5])
print(L1[2])
L1[1] = 22
print(L1)

print(L1[::2]) # L1[::2] 等同于 L[slice(None,None,2)]
print(L1[2:50:2])