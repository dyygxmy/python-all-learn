class Student:
    pass

stu = Student()
stu.name = 'xiaozhang'
stu.age = 14
print(stu.name,stu.age)
del stu.age
print(stu.name,stu.age) # AttributeError: 'Student' object has no attribute 'age' 报错，因为属性已经不存在了