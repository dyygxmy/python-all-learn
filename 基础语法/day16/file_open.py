try:
    op = open("mynote.txt", "r")
except FileNotFoundError:
    print("打开失败","FileNotFoundError")
else:
    print(op) # <_io.TextIOWrapper name='main.py' mode='r' encoding='cp936'>
    print(op.name) # mynote.txt
    print(op.mode) # r
    print(op.encoding) # cp936
    print(op.buffer) # <_io.BufferedReader name='mynote.txt'>
    op.close()