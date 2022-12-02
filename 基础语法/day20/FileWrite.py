# 本程序示意自定义的类作为环境管理器使用

class FileWrite:
    def __init__(self,filename):
        self.filename = filename # 此属性用于记住文件名

    def writeline(self,s):
        '''此方法用于向文件内写入字符串，同时自动添加换行'''
        self.file.write(s+'\n')

    def __enter__(self):
        '''此方法用于实现环境管理器'''
        self.file = open(self.filename,'w')
        print("进入enter方法，文件打开成功")
        return self # 返回值用于with中的as绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        exc_type: 为异常类型，没有异常时为None
        exc_val:  为错误对象，没有异常时为None
        exc_tb:   为错误的 traceback 对象
        '''
        self.file.close()
        if exc_type is None:
            print("退出with时无异常")
        else:
            print("退出with时有异常，异常类型是:%s，错误是:%s"%(exc_type,exc_val))
        print("exit方法被调用，已离开with语句，文件%s已关闭"%self.filename)

try:
    with FileWrite('log.txt') as fw:
        while True:
            s = input("请输入一行:")
            if s == 'exit':
                break
            if s == 'error':
                raise ValueError("故意制造的值错误")
            fw.writeline(s)
except:
    print("有错误发生，已转为正常")

print("程序结束")