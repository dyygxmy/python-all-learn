class myFile:
    def __init__(self,filename):
        self.filename = filename
    def __enter__(self):
        try:
            self.file = open(self.filename,'r+b')
            print("打开已存在文件%s"%self.filename)
        except:
            print("新建并打开文件%s"%self.filename)
            self.file = open(self.filename, 'w+b')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is None:
            print("退出with时无异常")
        else:
            print("退出with时有异常，异常类型是:%s，错误是:%s" % (exc_type, exc_val))
        print("exit方法被调用，已离开with语句，文件%s已关闭" % self.filename)

    def readDatas(self):
        return self.file.read()

    def writeDatas(self,s):
        print("写入数据:",s)
        if self.file.write(s):
            print("文件复制成功")
        else:
            print("文件复制失败")

try:
    datas = None
    with myFile('abcd.txt') as f_a:
        datas = f_a.readDatas()
        print("读出数据:%s"%datas)
    with myFile('log.txt') as f_w:
        f_w.writeDatas(datas)
except:
    print("有错误发生，已转为正常")

print("程序结束")