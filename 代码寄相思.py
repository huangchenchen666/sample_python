import time
from turtle import *
from random import randint
import sys
try:
    from colorama import Fore, init
    init()
except:
    pass
# ========================
# 文字致敬部分
# ========================
def print_with_effect(text):
    """实现逐字打印效果"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
def text_tribute():
    colors = [Fore.RED, Fore.YELLOW, Fore.WHITE, Fore.GREEN]
    message = [
        "\n山河无恙，英雄不朽",
        "铁血忠魂，永垂青史",
        "缅怀先烈，砥砺前行",
        "这盛世如您所愿！\n"
    ]
    for line, color in zip(message, colors):
        print(color, end='')
        print_with_effect(line)
        time.sleep(0.5)
# ========================
# 图形绘制部分
# ========================
def draw_candle():
    # 初始化画布
    setup(600, 600)
    bgcolor("black")
    title("永恒的火焰")
    speed(10)
    penup()
    # 绘制烛台
    goto(0, -180)
    pendown()
    color("gray")
    begin_fill()
    for _ in range(2):
        forward(40)
        left(90)
        forward(200)
        left(90)
    end_fill()
    # 绘制火焰
    penup()
    goto(20, 80)
    pendown()
    color("orange")
    begin_fill()
    for _ in range(3):
        forward(10)
        left(120)
    end_fill()
    # 添加文字
    penup()
    goto(-120, -220)
    color("white")
    write("英雄之火永不熄灭", font=("楷体", 18, "bold"))
# ========================
# 主程序
# ========================
if __name__ == "__main__":
    text_tribute()  # 执行文字致敬
    time.sleep(10)
    # 绘制图形
    if 'turtle' in sys.modules:
        reset()  # 重置画布
    draw_candle()

    # 彩色结束语
    print(Fore.YELLOW + "\n\n请关闭图形窗口结束程序")