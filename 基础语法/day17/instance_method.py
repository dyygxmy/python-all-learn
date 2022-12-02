# 本示例示意实例方法的定义方式和调用方法
class Dog:
    """这是一个类，用于描述一个小动物的行为"""
    def eat(self,food):
        """小狗能够有吃东西的行为"""
        print("小狗吃了",food)
        self.fo = food # 添加fo属性来记录小狗吃的什么

    def sleep(self,hour):
        print("小狗睡了",hour,"小时")

    def food_info(self):
        """能否在此方法内得到小狗上次吃的食物是什么"""
        print("小狗上次吃的是:",self.fo)

dog1 = Dog()
dog1.eat("骨头")
dog1.sleep(2)

dog2 = Dog()
Dog.eat(dog2,"狗粮")
Dog.sleep(dog2,3)

dog1.food_info()
dog2.food_info()