filename = 'pi_digits.txt'
with open(filename, encoding='utf-8') as file_object:
    # 读取所有内容
    print("读取所有内容")
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    print("读取每行内容")
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    # 每行内容存储在列表中
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    # 向文件写入多行
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 在文件内容后追加
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
