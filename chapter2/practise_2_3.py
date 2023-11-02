msg = "Ada ADA ada"
# 将单词首字母大写
print(msg.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# 在字符串中插入变量的值，3.6版本引入f，3.6之前的版本需要使用format()
full_name = f"{first_name} {last_name}"
print(full_name)
full_name = "{} {}".format(first_name, last_name)
print(full_name)

print("python")
# 制表符
print("\tpython")
# 换行符和制表符
print("Languages:\n\tPython\n\tJava")

favorite_language = " python "
# 删除右侧的空白字符
print(favorite_language.rstrip())
# 删除左侧的空白字符
print(favorite_language.lstrip())
# 删除两侧的空白字符
print(favorite_language.strip())
