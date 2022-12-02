# 此示例示意二进制模式读取mynote.txt文件
try:
    f = open('mynote.txt', 'rb')
    print("打开文件成功")
    b = f.read()
    print(b) # b'\xe7\xac\xac\xe4\xb8\x80\xe8\xa1\x8c\xe6\x96\x...(后面省略)
    print("转码后:",b.decode("utf8")) # 转码后: 第一行文本内容...(后面省略)
    f.close()
except IOError:
    print("打开文件失败")