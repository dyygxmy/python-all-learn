class Human:
    def __init__(self,name="",age=0,address=""):
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        print(self.name,self.age,self.address)

    def update_age(self):
        self.age += 1

def input_human():
    L = []
    while True:
        name = input("请输入一个人的姓名 :")
        if not name:
            break
        age = input("请输入一个人的年龄 :")
        address = input("请输入一个人的地址 :")
        hm = Human()
        hm.name = name
        hm.age = int(age)
        hm.address = address
        L.append(hm)
    return L

def main():
    docs = input_human()
    for h in docs:
        h.show_info()

    for h in docs:
        h.update_age()

    for h in docs:
        h.show_info()

main()