class MyNumber:
    def __init__(self,value):
        self.data = value

n1 = MyNumber(100)
print(str(n1)) # 此句等同于 print(n1)
# [out]
# <__main__.MyNumber object at 0x000001FA4AEB7400>
print(repr(n1))
# [out]
# <__main__.MyNumber object at 0x000001FA4AEB7400>
print(dir(n1))
# [
# '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data'
# ]

class MyNumber2:
    def __init__(self,value):
        self.data = value
    def __str__(self):
        return "重写了str"

n2 = MyNumber2(100)
print(str(n2)) # 此句等同于 print(n2)
# [out]
# 重写了str
print(repr(n2)) # 没重写，还是调用object的 __repr__()
# [out]
# <__main__.MyNumber2 object at 0x0000021804EB65E0>
