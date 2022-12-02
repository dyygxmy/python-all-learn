import show_menu as menu
import operate_func as opt
def input_operate():
    L = []
    while True:
        menu.show_menu()

        choice = input("请选择操作选项:")
        if choice == 'q':
            break
        else:
            L = opt.operate_manage(L,choice)
