magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 生成一系列数
for value in range(1, 5):
    print(value)
print("\n")
for value in range(5):
    print(value)

# 将range()生成的一系列数转为列表
print(list(range(6)))
# 指定步长为2
print(list(range(0, 6, 2)))

# 对列表进行统计
digits = list(range(10))
print(min(digits))
print(max(digits))
print(sum(digits))

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 取列表前4个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
# 取列表第3个到最后的元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
# 取列表后3个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# 遍历列表的部分元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 使用包含整个列表的切片复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
# 不是复制，将my_foods_new关联到同一个列表
my_foods_new = my_foods
print(my_foods_new)

# 不可变的列表被称为元组
# 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
my_t = (3,)

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# 相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组。
