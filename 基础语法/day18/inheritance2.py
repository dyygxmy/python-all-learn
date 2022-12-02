
# 此示例示意单继承的语法及使用方法
class Human:
    def __init__(self,name):
        self.name = name
    def say(self,what):
        print(self.name,"说:",what)
    def walk(self,distance):
        print(self.name,"走了",distance,"公里")

h1 = Human("小红")
h1.say("今天天气不错!")
h1.walk(5)

class Student(Human):
    # def __init__(self,name):
    #     Human.__init__(self,name) # 如果要调用超类的__init__方法，这里不需要调用，直接会传过去
    def study(self,subject):
        print(self.name,"学习了",subject)

class Teacher(Student):
    def teach(self,that):
        print(self.name,"正在教",that)

s1 = Student("小明")
s1.say("今天要好好学习!")
s1.walk(3)
s1.study("数学")

t1 = Teacher("计算机老师")
t1.say("同学们好好听课")
t1.walk(1)
t1.teach("面向对象")
t1.study("魔方")