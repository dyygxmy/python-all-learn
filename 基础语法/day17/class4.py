class Dog:
    pass

dog1 = Dog()
print(dog1.__dict__)
dog1.color = "白色"
print(dog1.__dict__)
print(dog1.__class__)