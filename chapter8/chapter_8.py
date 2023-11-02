def greet_users(users):
    for name in users:
        name = name.title()
        print('hello ' + name)


names = ['ksh', 'xiaoMing', 'zhangSan', 'wangWu']

# 遍历列表时，修改列表元素值，列表本身不变
greet_users(names)
print(names)


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_models(completed_models):
    """显示模型。"""
    print("\nshow_models:")
    for completed_model in completed_models:
        print(completed_model)


var_unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
var_completed_models = []

# 参数为列表的副本，保证原列表内容不变
print_models(var_unprinted_designs[:], var_completed_models)
show_models(var_completed_models)
show_models(var_unprinted_designs)


# *可变长参数，类型为tuple，多个形参时，必须将可变长参数放在最后
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    # print(type(toppings))
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# **可变长参数为一个个的键值对(关键字形参**kwargs)，类型为dict
def build_profile(first, last, **user_info):
    """创建一个字典变量，其中包含我们知道的有关用户的一切。"""
    # print(type(user_info))
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
