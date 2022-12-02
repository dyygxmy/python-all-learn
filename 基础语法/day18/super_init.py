class Human:
    def __init__(self,n,a):
        self.name = n
        self.age = a
        print("Human类的 __init__ 被调用")
    def show_info(self):
        print("姓名:",self.name)
        print("年龄:",self.age)

class Student(Human):
    def __init__(self,n,a,s=0):
        super().__init__(n,a) # 显式调用基类的初始化方法
        self.score = s
        print("Student 类的 __init__ 被调用")

    def show_info(self):
        super().show_info()
        print("成绩:",self.score)

s1 = Student("小明",14)
s1.show_info()