def mycp(src_file,dst_file):
    try:
        with open(src_file,'rb') as fr , \
            open(dst_file,'wb') as fw: # 一行代码换成两行
            while True:
                b = fr.read(4096) # 分段读取，防止文件过大
                if not b:
                    break
                fw.write(b)
    except:
        return False
    return True

def main():
    src = input("请输入源文件名:")
    dst = input("请输入目标文件名:")
    if mycp(src,dst):
        print("复制文件成功")
    else:
        print("复制文件失败")
main()