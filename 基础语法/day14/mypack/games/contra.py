
from ..menu import show_menu # 此为相对导入，当前所在位置为mypack.games.contra

# 以下导入是错误的，已超出包的范围
# from ...mypack.menu import show_menu # ValueError: attempted relative import beyond top-level package

def play():
    print("正在玩魂斗罗")
def gameover():
    print("游戏结束!!!")
    show_menu()
print("魂斗罗模块被加载!")