# 导入模块中的函数，多个函数以,分割，使用as为函数重命名
# from module import * 可以导入模块中的所有函数，但是这样容易自己定义的函数与模块中的函数命名冲突，不建议这样使用
# 建议使用import module，然后module.fn()，或者导入具体的函数
from pizza import say

# 使用导入的函数
say()
