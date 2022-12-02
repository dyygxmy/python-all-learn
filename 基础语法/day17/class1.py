# 类的示例

class Dog: # 定义一个类
    pass
dog1 = Dog() # 用类来创建一个对象用dog1绑定
print(id(dog1)) # 打印dog1所在的内存地址
dog2 = Dog() # 用类来创建一个对象用dog2绑定
print(id(dog2)) # 打印dog2所在的内存地址
print(dog1 is dog2) # 判断dog1与dog2是不是同一条狗(False)
