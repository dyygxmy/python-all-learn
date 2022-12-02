class A:
    def __init__(self):
        self.__p1 = 100 # 创建私有属性

    def __m1(self):
        print("A类的私有方法被调用!")

    def test(self):
        print(self.__p1) # 可以访问
        self.__m1() # 可以访问

a = A()
a.test() # 使用类内的方法来操作私有属性和私有方法
# print(a.__p1) # AttributeError 不能访问，报错
# a.__m1() # AttributeError 在类外部不能调用类的私有方法