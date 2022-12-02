class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(B):
    pass


print(issubclass(B,A)) # True
print(issubclass(C,B)) # True
print(issubclass(D,A)) # True
print(issubclass(D,C)) # False
print(issubclass(C,(int,str))) # False
print(issubclass(C,(int,str,object))) # True
print(issubclass(bool,int)) # True bool是int的子类