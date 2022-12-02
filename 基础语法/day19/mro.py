class A:
    m = "A"
    print("调用的是A类")

class B:
    m = "B"
    print("调用的是B类")

class C:
    m = "C"
    print("调用的是C类")

class D:
    m = "D"
    print("调用的是D类")

class AB(A,B):
    # m = "AB"
    print("调用的是AB类")

class CD(C,D):
    m = "CD"
    print("调用的是CD类")

class ABCD(AB,CD):
    # m = "ABCD"
    print("调用的是ABCD类")

a = ABCD()
print(a.m)

print(ABCD.__mro__)
# [OUT]
# (<class '__main__.ABCD'>, <class '__main__.AB'>, <class '__main__.A'>, <class '__main__.B'>,
# <class '__main__.CD'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)