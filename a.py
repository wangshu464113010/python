# UNIX系统中的运行命令
#  python hello.py

print("Hello World")

name = 'Tom'
print(name)
age = 10
print(age)
z = 123456
print(z)
print("She said: \"Let\'s go!\" ")  # 转义  \
# 拼接字符串
print("Hello " + "World")  # 换行符 \n
# str与repr区别
print("str = \n" + str("Hello\nWorld"))  # 结果如下
#        Hello
#        World
print("repr = " + repr("Hello\nWord"))  # 'Hello\nWord'
# 长字符串,续接符  \
defg = "1" + "2" + \
       "4 + 5"
print("defg = " + defg)
# 原始字符串
print(r'C:\nProgram Files\python\project')
print(r'C:\nProgram Files\python\project' '\\')
# 10 的 引用计数增加
a = 10
b = 10
c = 10
# 10的引用计算为4
# 引用计算减少 del
del c
# 10的引用计算减1
# print(c)  # 报错

# 数和表达式
# 四则运算 / * - + %
# 浮点数的四则运算(整除) //
print(10 / 2.4)  # 4.166666666666667
print(10.0 // 2.4)  # 4.0
# 乘方(幂) **
print(2 ** 3)
# 进制 0x(16) 0(8) 0b(2)

# Unicode编码
print('\u00C6')
print('\U0001F60A')
print('\N{Cat}')
print("Hællå, wørld!".encode())
# 获取用户的输入
x = input("The meaning of file:")
print(x)
"""
三个单引号或者三个双引号就是多行注释
"""
