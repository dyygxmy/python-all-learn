try:
    op = open("mynote.txt", encoding='utf8')
except FileNotFoundError:
    print("打开失败","FileNotFoundError")
else:
    x = 3
    if x == 1:
        print("第一行内容是 :", op.readline(), "e")  # 第一行内容是 : 第一行
        # e
        print("---------------------")
        print(op.read())  # 第二行
        # 第三行
        # 第四行
        print("读完了:", op.readline(), "e")  # 读完了:  e
    if x == 2: # 与x == 1内的读取都是相互影响的，分开安排读
        print(op.readlines()) # ['第一行\n', '第二行\n', '第三行\n', '第四行\n']
    if x == 3:
        print(op.readline(2)) # 第一 (读两个字符个数)
        x = 3
        if x == 0:
            print(op.readlines(0)) # ['行文本内容\n', '第二行文本内容\n', '第三行文本内容\n', '第四行文本内容\n']
        if x == 1:
            print(op.readlines(1)) # ['行文本内容\n'] (size = 5)
        if x == 2:
            print(op.readlines(5)) # ['行文本内容\n']
        if x == 3:
            print(op.readlines(6)) # ['行文本内容\n', '第二行文本内容\n'] 6 >= 5 + 1
        if x == 4:
            print(op.readlines(13)) # ['行文本内容\n', '第二行文本内容\n']
        if x == 5:
            print(op.readlines(14)) # ['行文本内容\n', '第二行文本内容\n', '第三行文本内容\n'] 14 >= 5 + 1 + 7 + 1
        if x == 6:
            print(op.readlines(21)) # ['行文本内容\n', '第二行文本内容\n', '第三行文本内容\n']
    op.close()
