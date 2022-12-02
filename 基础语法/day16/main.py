# bytearray的方法的示例
# ba = bytearray(b"ABCDEFGH")
# print(ba) # bytearray(b'ABCDEFGH')
# ba.clear()
# print(ba) # bytearray(b'')
# ba = bytearray(b"ABCDEFGH")
# ba.append(73) # 只能是整数 73就是I
# print(ba) # bytearray(b'ABCDEFGHI')
# ba.remove(66) # 只能是整数 66就是B
# print(ba) # bytearray(b'ACDEFGHI')
# ba.reverse()
# print(ba) # bytearray(b'IHGFEDCA')
# st = ba.decode("utf8")
# print(ba,st) # bytearray(b'IHGFEDCA') IHGFEDCA
# print(ba.find(65)) # 找65也就是A的下标 是 7
# print(ba.find(b'H')) # 找H的下标 是 1
# print(ba.find(b'z')) # 找不到，返回-1


# 练习:
# 将如下数据用文本编辑器sublime写入到data.txt文件中
# 数据如下:
# 小张 138888888888
# 小李 139999999999
# 小赵 136666666666
# 写程序读取数据，打印出姓名和电话号码，格式如下:
# 姓名 : 小张，电话 : 138888888888

# F = open("data.txt","rt",encoding="utf8")
# # 方法一 : 直接全读出来处理数据
# def print_all1():
#     data = F.readlines()
#     # print(data)
#     data_all = []
#     for x in data:
#         s = {}
#         data_line = x.strip().split(" ")
#         s["姓名"] = data_line[0]
#         s["电话"] = data_line[1]
#         data_all.append(s)
#     # print(data_all)
#     for x in data_all:
#         print("姓名 :",x["姓名"],"， 电话 :",x["电话"])
#
# # 方法二 : 一行一行的读并处理
# def print_all2():
#     while True:
#         s = F.readline()
#         if not s:
#             break
#         s = s.rstrip() # 去掉右边的换行符
#         index = s.find(" ")
#         name = s[:index]
#         tel = s[index+1:]
#         print("姓名 :",name,"， 电话 :",tel)
# # print_all1()
# print_all2()
# F.close()


# 练习:
# 1.写一个程序，读入任意行的文字信息，当输入空行时结束输入
# 将读入的字符串存于列表中，然后将列表里的内容写入文件input.txt中
# def writeFile_input():
#     data_all = []
#     while True:
#         data_one = input("请输入任意内容:")
#         if data_one:
#             data_all.append(data_one)
#         else:
#             break
#     input_len = len(data_all)
#     if input_len > 0:
#         try:
#             f = open("input.txt","w")
#             if f:
#                 print("文件打开成功")
#                 # 方法一，用writelines写入列表
#                 # for x in range(input_len):
#                 #     data_all[x] += "\n"
#                 # f.writelines(data_all)
#                 # 方法二，分段写
#                 for x in data_all:
#                     f.write(x)
#                     f.write("\n")
#                 f.close()
#         except IOError:
#             print("文件打开失败")
# writeFile_input()
# 2.写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号进行打印显示
# 显示格式如下:
# 第1行 : zzzzzzz
# 第2行 : xxxxxx
# def read_print():
#     try:
#         f = open("input.txt")
#         if f:
#             print("打开文件成功")
#             datas = f.readlines()
#             for k,n in enumerate(datas,1):
#                 n = n.rstrip() # 去掉右边换行符
#                 print("第%d行 : %s"%(k,n))
#             f.close()
#     except IOError:
#         print("打开文件失败")
# read_print()