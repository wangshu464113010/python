# 导入
# from someModule import oneFunction,twoFunction,...
# 导入所有函数
# from someModule import *
# 仅当你确定要导入模块中的一切时，采用使用最后一种方式。但如果有两个模块，它们都包
# 含函数open，该如何办呢？你可使用第一种方式导入这两个模块，并像下面这样调用函数：
# module1.open(...)
# module2.open(...)
# 给模块名设置别名 as
import math as foobar
# 给函数设置别名
from math import sqrt as foobarSqrt

print(foobarSqrt(4))
print(foobar.sqrt(9))
# print函数
print('Hello,', 'Gumby', 'Mr.')
# 上述分割符默认是空格,指定需要添加参数sep
print('I', 'wish', 'to', 'register', 'a', 'complaint', sep='_')
# 赋值魔法
# 序列解包(可迭代对象解包) 可以同时(并行)给多个变量复制
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
# 还可用于交换多个变量的值
x, y = y, x
print(x, y, z)  # 2 1 3
# values变成一个元组
values = 1, 2, 3
print(values)
a, b, c = values  # 也可以这样赋值(使用元组)
print(a, b, c)
# !!!要解包的序列包含的元素个数必须与你在等号左边列出的目标个数相同，否则Python将引发异常。
# 可以使用*来收集多余的值，这样无需确保值和变量的个数相同
d, e, *rest = [1, 2, 3, 4]
print(rest)
# 注：*的位置不固定，可以放在任何位置，但是带*的变量最终是一个列表
# 链式赋值
s = t = 1
print(s, t)
# 增强赋值+-/*,Python中没有++，--运算符
s += 1
print(s)
# ####################################
# 条件语句
# bool类型，True == 1/False == 0
print(True + False + 42)  # 与Python解释器有关
print(bool(5), bool(0))  # 跟C语言类似，0表示假，非0为真
# if elif  else
name = input("What's your name?")
if name.endswith("Alice"):
    print("Hello,Mr. Alice")
elif name.endswith("Tom"):
    print("Hello,Mr. Tom")
else:
    print("Hello,stranger")
# 比较运算符，大部分同C,Java...
# x == y       x 等于y
# x < y        x小于y
# x > y        x大于y
# x >= y       x大于或等于y
# x <= y       x小于或等于y
# x != y       x不等于y
# x is y       x和y是同一个对象
# x is not y   x和y是不同的对象
# x in y       x是容器（如序列）y的成员
# x not in y   x不是容器（如序列）y的成员
# ==用来检查两个对象是否相等，而is用来检查两个对象是否相同（是同一个对象）
# 注：不要将is用于数和字符串等不可变的基本值
# 获取字符的Unicode码ord,chr
print(ord('🙈'))  # 通过字符获取码
print(chr(128584))  # 通过码获取字符 🙈
# and,or,not对应C语言中的与,或,非(存在短路逻辑)
# 断言 assert关键词，后面的条件满足，程序才能执行下去，否则程序崩溃
age = 1
assert 0 < age < 10  # Python中支持这种写法，与C,java不同

# 循环语句
# 1.while循环
l = 1
while l <= 10:
    print(x)
    l += 1
# 2.for循环
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)
# python提供了一个创建范围的内置函数renge()，包含第一个参数值，不包含第二个参数值
print(list(range(0, 10)))
# 小程序，打印1~100的数
for number in range(1, 101):
    print(number)
# 建议使用for循环
# for循环迭代字典
newD = {'x': 1, 'y': 2, 'z': 3}
for key in newD:  # 迭代方式一
    print(key, ' = ', newD[key])
for key, value in newD.items():  # 迭代方式二
    print(key, ' corresponds to', value)

# break(结束循环)/continue(结束本次循环，进入下一个循环)语句与C中一致

# 并行迭代,内置函数zip,将两个序列"缝合"起来，并返回一个有元组组成的序列
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
print(list(zip(names, ages)))

# 简单推导
# 列表推导是一种从其他列表创建列表的方式，类似数学中的集合推导
# 列表推导的工作原理非常简单，类似for循环，如下
r = [x * x for x in range(10)]
print(r)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 打印只能够被3整除的数
print([x * x for x in range(10) if x % 3 == 0])  # [0, 9, 36, 81]
# 还可以这样，
print([(x, y) for x in range(3) for y in
       range(3)])  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 小程序，男女配对（首字母相同的用+拼接在一起）
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b + '+' + g for b in boys for g in girls if b[0] == g[0]])
# 上述男孩/女孩配对示例的效率不太高，因为它要检查每种可能的配对
# 效率更高的解决方法(Alex Martelli推荐的解决方案)
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])
# 字典推导
# 使用花括号{}
squares = {i: "{} squared is {}".format(i, i ** 2) for i in range(10)}
print(squares)
# 总结简单推导大致格式
# 列表使用[],字典使用{}
# 首先是数据格式+空格+类似for循环的东西(也不知道应不应该称之为语句)(表达式？)

# 三人行，另外三条语句：pass，del，exec
# pass 什么都不 做，可以使用占位符，但是感觉没什么用
pass
# del删除，前面已讲
# exec会将字符串作为代码执行，还有一个eval函数类似
exec('print("Hello World")')
# !!! 调用函数exec时只给它提供一个参数绝非好事。在大多数情况下，还应向它传递一个
# 命名空间——用于放置变量的地方；否则代码将污染你的命名空间，即修改你的变量。
# 如下列注释的代码就会污染sqrt函数
"""
from math import sqrt
exec("sqrt = 1")
sqrt(4)
此处会报错 
"""
# 为了安全起见，提供一个字典已充当命名空间(作用域)
from math import sqrt

scope = {}
exec('sqrt = 1', scope)
print(sqrt(4))
print(scope['sqrt'])  # 访问sqrt变量
# eval用于计算字符串表达式的值,eval也可以提供一个命名空间
print("8+3*9 = ", eval("8+3*9"))
# 如下
scope1 = {}
scope1['x'] = 2
scope1['y'] = 3
print(eval('x * y', scope1))
