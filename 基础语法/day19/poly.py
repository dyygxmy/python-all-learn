class Shape:
    def draw(self):
        pass

class Point(Shape):
    def draw(self):
        print("正在画一个点")

class Circle(Point):
    def draw(self):
        print("正在画一个圆")

def my_draw(s):
    s.draw() # 直接看是不能确定调用的哪个的draw，只在运行时根据传进来的s后才能决定

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)