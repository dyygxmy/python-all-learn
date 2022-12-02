class Dog:
    pass
dog1 = Dog # 不加括号直接等于的Dog类，不是创建，加括号才是构造函数，创建新对象
dog1.kinds = "京巴" # 为dog1绑定的实例添加kinds属性
dog1.color = "白色" # 添加属性
print(dog1.kinds,dog1.color) # 访问属性
dog1.color = "黄色" # 再次属性赋值
print(dog1.kinds,dog1.color)

print(dir(dog1)) # 查看类的所有变量