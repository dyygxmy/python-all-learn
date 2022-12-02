'''
练习:
list类里只有append向末尾添加一个元素的方法，但没有向列表尾部添加元素的方法，
试想能否为列表在不改变原有功能的基础上添加一个insert_head(n)的方法，在列表头部添加元素
class My_List(list):
    def insert_head(self,element):
        self.insert(0,element)

my_list = My_List(range(3,6))
print(my_list)
my_list.insert_head(2)
print(my_list)
'''

help(__builtins__)