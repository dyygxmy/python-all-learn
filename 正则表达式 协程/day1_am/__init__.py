
def createList():
    l = []
    for i in range(18):
        l.append("学" + str(i+1) + "楼")
    return l

def pingan(ls,l):
    len1 = len(l)
    for i in l:
        print(ls[i-1]+"平安")

ls = createList()
print(pingan(ls,[4,2,6]))