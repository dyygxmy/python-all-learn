try:
    f = open("mydata.txt", "w")
    print("文件打开成功")
    f.write("我是第一行数据\n")
    f.write("我是第二行数据\n")
    f.writelines(["我是第三行数据\n","我是第四行数据\n","five\n"])
    f.close()
except IOError:
    print("文件打开失败")