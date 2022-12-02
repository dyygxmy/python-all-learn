# 此程序示意tell方法的用法
try:
    f = open('mydata.bin', 'rb')
    print("打开文件成功")
    print("打开文件时文件流的位置:",f.tell()) # 打开文件时文件流的位置: 0
    f.read(5)
    print("读五个字节后文件流的位置:",f.tell()) # 读五个字节后文件流的位置: 5
    f.seek(7)
    print("改变后的文件流的位置:",f.tell()) # 改变后的文件流的位置: 7
    f.seek(-3,1) # 从当前位置向头方向移3个位置
    print("二次改变后的文件流的位置:", f.tell()) # 二次改变后的文件流的位置: 4
    f.seek(-5, 1)  # 从当前位置向头方向移5个位置 (超出直接报错)
    print("三次改变后的文件流的位置:", f.tell())
    f.close()
except IOError:
    print("打开文件失败")