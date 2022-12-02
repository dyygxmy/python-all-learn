class Bicycle: # 自行车类(默认人力自行车)
    def run(self,km):
        print("人力骑行了",km,"公里")

class EBicycle(Bicycle): # 电动自行车类
    def __init__(self,v):
        self.vol = v
        print("电动自行车电量为",v,"度")
    def fill_charge(self,vol):
        print("充电",vol,"度")
        self.vol += vol
    def run(self,km):
        cru_km = km - self.vol*10 # 剩余里程为总里程与续航的差
        if cru_km <= 0: # 续航足够
            self.vol -= int(km/10)
            print("电动自行车行驶",km,"公里")
        else: # 续航不够
            print("电动自行车行驶",self.vol*10,"公里")
            self.vol = 0
            super().run(cru_km)

b = EBicycle(12) # 创建一个电动自行车，电量有5度
b.run(10) # 骑行10km
b.run(100) # 骑行100km
b.fill_charge(6) # 充6度电
b.run(70) # 又骑行70km
