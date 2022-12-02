# 此示例示意初始化方法的定义方法和调用过程

class Car:
    """小汽车类"""
    def __init__(self,c,b,m):
        # print("ini:",self)
        self.color = c # 颜色
        self.brand = b # 品牌
        self.model = m # 型号

    def run(self,speed):
        # print("run:",self)
        print(self.color,"的",self.brand,
              self.model,"正在以",speed,
              "公里/小时的速度行驶")
    def change_color(self,co):
        self.color = co
a4 = Car("红色","奥迪","A4")
# print("a4:",a4)
a4.run(199)
a4.change_color("黑色")
a4.run(220)