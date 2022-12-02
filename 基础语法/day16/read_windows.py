try:
    f = open('WindowsFile.txt', 'rb')
    b = f.read()
    print(len(b)) # 20
    print(b.decode('GB18030')) # 一二三四五六七八九十
    f.close()
except IOError:
    print("打开文件失败")