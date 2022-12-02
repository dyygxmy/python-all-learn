# 本示例示意with语句的使用方法

# 打开文件读取文件数据(try-finally来实现关闭文件)
def read_file1():
    try:
        f = open("abcd.txt")
        try:
            while True:
                s = f.readline()
                if not s:
                    break
                int(input("请输入任意数字打印下一行:"))
                print(s)
        finally:
            print("关闭文件")
            f.close()
    except IOError:
        print("文件错误，已捕获")
    except ValueError:
        print("程序已转为正常状态")
# read_file1()

# 打开文件读取文件数据(with来实现关闭文件)
def read_file2():
    try:
        with open("abcd.txt") as f: # 跳出with语句时文件会自动关闭
            while True:
                s = f.readline()
                if not s:
                    break
                int(input("请输入任意数字打印下一行:"))
                print(s)
            print("关闭文件")
    except IOError:
        print("文件错误，已捕获")
    except ValueError:
        print("程序已转为正常状态")
read_file2()

print("程序结束")