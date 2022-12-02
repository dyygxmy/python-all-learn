class Student:
    pass

def input_student():
    lst = []
    print("请按要求输入学生信息，姓名为空结束输入!")
    while True:
        name = input("请输入学生姓名:")
        if not name:
            break
        student = Student() # 括号不能省，不然是Student对象，而不是构造函数
        student.name = name
        student.age = input("请输入学生年龄:")
        student.score = input("请输入学生成绩:")
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