class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def input_student():
    lst = []
    print("请按要求输入学生信息，姓名为空结束输入!")
    while True:
        name = input("请输入学生姓名:")
        if not name:
            break
        age = input("请输入学生年龄:")
        score = input("请输入学生成绩:")

        student = Student(name,age,score)

        lst.append(student)
    return lst

def output_student(lst):
    print("所有学生信息如下")
    for x in lst:
        print("姓名:",x.name,
              "年龄:",x.age,
              "成绩:",x.score)

def main():
    L = input_student()
    output_student(L)

main()