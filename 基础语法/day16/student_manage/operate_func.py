
def operate_manage(L=[],choice=""):
    if choice == "1": # 添加学生信息
        L = add_datas()
    elif choice == "2": # 显示所有学生的信息
        show_datas(L)
    elif choice == "3": # 删除学生信息
        L = delete_data(L)
    elif choice == "4": # 修改学生成绩
        L = update_scores(L)
    elif choice == "5": # 按学生成绩高低来显示
        L = mySort(L,"成绩",True)
        show_datas(L)
    elif choice == "6": # 按学生成绩低高来显示
        L = mySort(L,"成绩",False)
        show_datas(L)
    elif choice == "7": # 按学生年龄高低显示
        L = mySort(L,"年龄",True)
        show_datas(L)
    elif choice == "8": # 按学生年龄低高显示
        L = mySort(L,"年龄",False)
        show_datas(L)
    elif choice == "9": # 保存学生信息到文件
        save_file(L)
    elif choice == "10": # 从文件中读取数据
        L = read_file()
    else:
        print("您的输入有误，请重新输入!!!")
    return L


# 添加学生信息操作
def add_datas():
    L = []
    print("请按下面要求输入学生信息，姓名为空结束输入!!!")
    while True:
        name = input("请输入学生姓名:")
        if not name:
            return L
        age = input("请输入学生年龄:")
        scores = input("请输入学生成绩:")
        data = {}
        data["姓名"] = name
        data["年龄"] = age
        data["成绩"] = scores
        L.append(data)


# 按格式替换学生信息各节点数据
def replace_node(data="",isend=True):
    str_ini = "|          "
    index = int((len(str_ini) - 1) / 2) - int((len(data) - 1) / 2)
    str = str_ini[:index] + data + str_ini[index + len(data):]
    if isend:
        str += "|"
    return str


# 显示所有学生信息操作
def show_datas(L=[]):
    print("+----------+----------+----------+")
    name_title = replace_node("name", False)
    age_title = replace_node("age", False)
    scores_title = replace_node("scores", True)
    print(name_title + age_title + scores_title)
    for x in L:
        name_node = replace_node(x["姓名"],False)
        age_node = replace_node(x["年龄"],False)
        scores_node = replace_node(x["成绩"],True)
        print(name_node+age_node+scores_node)
    print("+----------+----------+----------+")


# 删除学生信息操作
def delete_data(L=[]):
    while True:
        name = input("请输入需要删除的学生姓名(输入为空则退出):")
        if not name:
            return L
        for x in L:
            if x["姓名"] == name:
                L.remove(x)


# 修改学生成绩操作
def update_scores(L=[]):
    while True:
        name = input("请输入需要修改成绩的学生姓名(输入为空则退出):")
        if not name:
            return L
        scores = input("请输入修改后的成绩:")
        for x in L:
            if x["姓名"] == name:
                x["成绩"] = scores


# 自定义对列表的排序处理
def mySort(L=[],key="",reverse=False):
    def myKey(L=[]):
        return int(L[key])
    return sorted(L,key=myKey,reverse=reverse)


# 保存学生信息到文件
def save_file(L=[]):
    try:
        f = open("si.txt", "w+")
        if f:
            for x in L:
                f.write(x["姓名"] + "," + x["年龄"]+"," + x["成绩"] + "\n")
            f.close()
    except IOError:
        print("打开si.txt文件失败")


# 从文件中读取学生信息
def read_file():
    L = []
    try:
        f = open("si.txt")
        if f:
            datas = f.read()
            f.close()

            datas = datas.strip()
            data_lines = datas.split("\n")
            for x in data_lines:
                data = {}
                one_lines = x.split(",")
                data["姓名"] = one_lines[0]
                data["年龄"] = one_lines[1]
                data["成绩"] = one_lines[2]
                L.append(data)
    except IOError:
        print("打开si.txt文件失败")
    return L