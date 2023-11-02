# 模块是扩展名为.py的文件，可以在其他程序中导入模块，使用模块中的函数功能
def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def say():
    print("Please try some pizza")
