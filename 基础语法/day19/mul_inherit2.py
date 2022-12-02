class A:
    def m(self):
        print("A.m()被调用")

class B:
    def m(self):
        print("B.m()被调用")

class AB(A,B):
    pass

ab = AB()
ab.m()