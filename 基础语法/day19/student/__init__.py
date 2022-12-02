from student_info import StudentInfo as Stu

from show_menu import ShowMenu as Show_Mu
from choice_manage import Choice_Manage as Cho_Mag
def choice(cho):
    pass

def main():
    show = Show_Mu()
    choice = Cho_Mag()
    while True:
        show.show_menu()
        if not choice.choice_manage():
            break


if __name__ == '__main__':
    main()

