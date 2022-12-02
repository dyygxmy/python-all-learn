from student_info import StudentInfo as Stu
class Choice_Manage:
    def choice_manage(self):
        cho = input("请输入功能选项 :")
        stu = Stu()
        if cho == "1":
            stu.add_datas()
        elif cho == "2":
            stu.show_stu_info()
        elif cho == "3":
            pass
        elif cho == "4":
            pass
        elif cho == "5":
            pass
        elif cho == "6":
            pass
        elif cho == "7":
            pass
        elif cho == "8":
            pass
        elif cho == "9":
            pass
        elif cho == "10":
            pass
        elif cho == "11":
            pass
        elif cho == "q":
            return False
        return True