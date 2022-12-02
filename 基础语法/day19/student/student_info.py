class StudentInfo:
    docs = []
    def __init__(self,name,age,score):
        self.__name = name
        self.__age = age
        self.__score = score
    def add_datas(self):
        while True:
            name = input("请输入学生姓名 :")
            if not name:
                break
            age = input("请输入学生年龄 :")
            score = input("请输入学生成绩 :")
            address = input("请输入学生住址 :")
            self.__name = name
            self.__age = age
            self.__score = score
            self.__address = address
            stu = (name,age,score,address)
            self.__class__.docs.append(stu)

    def show_stu_info(self):
        for x in self.__class__.docs:
            print("name:%s,age:%s,score:%s,address:%s"%x)

    def get_stu(self):
        return (self.__name,self.__age,self.__score,self.__address)

class StudentInfo2(StudentInfo):
    def __init__(self,address):
        self.__address = address

