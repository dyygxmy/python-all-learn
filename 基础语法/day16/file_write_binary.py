# 此程序示意以二进制方式打开文件后进行写操作
try:
    f = open('mydata.bin', 'wb')
    print("打开文件成功")
    r1 = f.write(b'hello123\xe4\xb8\xad') # 写入文件内容为:hello123中
    print("本次写入%d个字节"%r1) # 本次写入11个字节  8个英文+1个中文 = 8+1*3 字节
    r2 = f.write('汉字'.encode('utf8'))    # 写入文件内容:汉字
    print("本次写入%d个字节" % r2) # 本次写入6个字节 2个中文=2*3 字节
    f.close()
except IOError:
    print("打开文件失败")