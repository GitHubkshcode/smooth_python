# 创建列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

# 在列表指定位置插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除列表指定位置的元素
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 弹出列表最后的元素并返回该元素的值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 弹出列表指定位置的元素并返回该元素的值
first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)

# 删除列表中的值
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# 列表升序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 列表降序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# 返回列表升序的结果，不修改原列表的顺序
print(sorted(cars))
# 返回列表降序的结果，不修改原列表的顺序
print(sorted(cars, reverse=True))
print(cars)

# 将列表翻转
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# 获取列表的长度
print(len(cars))
