import types
class Aaa:
    pass
va1 = 5
va2 = ""
va3 = b""
va4 = Aaa()

def func():
    print("调用了函数")
    pass
print(type(va1)) # <class 'int'>
print(type(va2)) # <class 'str'>
print(type(va3)) # <class 'bytes'>
print(type(va4)) # <class '__main__.Aaa'>
print(type(func)) # <class 'function'>

print(isinstance(va1,int))
print(isinstance(va2,str))
print(isinstance(va3,bytes))
print(isinstance(va4,(int,Aaa)))
print(isinstance(func,(int,types.FunctionType)))
