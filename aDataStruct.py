# Python支持一种数据结构的基本概念，名为容器（container）。容器基本上就是可包含其
# 他对象的对象。两种主要的容器是序列（如列表和元组）和映射（如字典）。在序列中，
# 每个元素都有编号，而在映射中，每个元素都有名称（也叫键）。
# 有一种既不是序列也不是映射的容器，它就是集合（set）
# 序列:列表和元组
print("通用的序列操作")
l = ['123', '456', 123456, ['a', [1, 2, 3], 23.01]]
print(l)
# 索引由正负值,第一个元素是0  -1表示最后一个元素,
print("l[0] = " + l[0])
print("l[-1][1][0] = " + str(l[-1][1][0]))
print('Hello'[1])
# 切片slicing,访问指定范围内的元素
pString = '<a href="http://www.python.org">Python web site</a>'
print(pString[9:30])  # ：第一个索引是包含的第一个元素的编号，但第二个索引是切片后余下的第一个元素的编号
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[-3:-1])
# 第一个索引值为0可以省略, 若取到最后一个值，最后一个索引也可以省略
print(numbers[:])
print(numbers[:3])
print(numbers[-3:])
# 步长 第三个数表示步长,步长不能为0,可以为负数
# 步长为正数,表示从左到右移动;为负数，表示从右到左移动
# !!! 步长不能为0，否则无法向前移动
print(numbers[0:10:2])
print(numbers[8:0:-1])
# 序列相加和相乘(拼接) +  和  *
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)
# 创建空列表,可以使用[]表示
sequence0 = []
# 若讲sequence的长度初始化为10
sequence = [None] * 10
sequence[2] = 100
print(sequence[2])

# 成员资格 in运算符,检查该成员是否在该容器里,返回值为True或者False
print('o' in 'Hello')
print('a' in 'Hello')
print(1 in numbers)
# 获取容器长度,最大值,最小值
print(len(l))
print(max(numbers))
print(min(numbers))
# 列表 ##############################
print("列表list")
# 函数list
print(list('Hello'))  # ['H', 'e', 'l', 'l', 'o']
# 修改列表
updateList = [1, 2, 3, 4, 5, 6]
updateList[0] = 7
print(updateList)
# 删除 del
del updateList[0]
print(updateList)
# 给切片赋值
name = list('Perl')
name[2:] = list('ar')
print(name)
# 插入新元素
updateList[0:0] = [1]  # updateList的中的第一个元素在上面已经被删除了
print(updateList)
# 利用空切片删除多个元素
updateList[1:5] = []  # 此行代码等价于 del updateList[1:5]
print(updateList)
# 列表中的方法
# append(),clear(),copy(),count(),extend(),index(),
# 在尾添加，清空，复制，统计某一值得个数，扩展，获取某一值得索引
# insert(),pop(),remove(),reverse(),sort()
# 在指定位置插入，删除最后一个元素，删除指定值得元素(只删除第一个)，反转，排序
# !!!没有push()方法
methodListLearn = [1, 2, 3, 4, 5, 1, 1]
methodListLearn.append(1)
print(methodListLearn.index(1))
print(methodListLearn.count(1))
# 元组 不可修改的序列#####################################
print("元组tuple")
yuanZu = (1, 2, 3)
# 空元组的 ()，若元组只有一个值，必须在其后面加一个逗号(原因:(1) = 1,此时不再是元组，而是一个数)
OneElementTuple = (1,)
# 函数tuple工作原理与list类似,将一个序列转换成元组
print(tuple([1, 2, 3]))
print(tuple('Hello World'))
# 元组的访问
print(yuanZu[0])
# 序列的函数
# len(seq),list(seq),max(seq),min(seq),
# reversed(seq)【可以使用该方法反向迭代序列】,
# sorted(seq)【返回一个有序表】,tuple(seq)
print("字符串")
# 字符串  序列的标准操作都是适用于字符串######################
# （索引、切片、乘法、成员资格检查、长度、最小值和最大值）
# 由于字符串不可变，故给字符串赋值和切片赋值是非法的
# website = 'http://www.python.org'
# website[-3:] = 'com'  # 此两行代码非法

# 格式化输出
values = "World"
print("Hello %s" % values)
values1 = ('Hello', 'World')
print("Tom ,%s,%s" % values1)

newString = "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)
print(newString)
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
# 字符串格式设置中的类型说明符
# 类型  含义
# b  将整数表示为二进制数
# c  将整数解读为Unicode码点
# d  将整数视为十进制数进行处理，这是整数默认使用的说明符
# e  使用科学表示法来表示小数（用e来表示指数）
# E  与e相同，但使用E来表示指数
# f  将小数表示为定点数
# F  与f相同，但对于特殊值（nan和inf），使用大写表示
# g  自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数
# G  与g相同，但使用大写来表示指数和特殊值
# n  与g相同，但插入随区域而异的数字分隔符
# o  将整数表示为八进制数
# s  保持字符串的格式不变，这是默认用于字符串的说明符
# x  将整数表示为十六进制数并使用小写字母
# X  与x相同，但使用大写字母
# %  将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上 %）

# 宽度、精度和千位分隔符
# 宽度是在格式中指定的
print("{num:10}".format(num=3))  # '          3'
print("{name:10}".format(name="Bob"))  # 'Bob       '
# 精度的指定，需要在前面加上一个表示小数点的句点(.)
print("Pi day is {pi:.2f}".format(pi=3.14))  # Pi day is 3.14
# 千位分隔符使用逗号,
print("One google is {:,}".format(10 ** 10))  # One google is 10,000,000,000
# 符号、对齐和用0填充
print('{:010.2f}'.format(3.14))  # 0000003.14
# 对上行代码解释：第一个0表示前面使用0填充(可以使用别的字符填充)，往后10表示占10个字符，小数点后面的2f表示2位小数位
# 左对齐使用<,右对齐使用>,居中使用^
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(3.14))  # 结果如下
# 3.14
#    3.14
#       3.14
#  等等
# 字符串的方法
print("字符串的方法")
# center() 居中,两个参数，第一个数据个数，第二个填充字符类型(默认是空格)
print("Hello World".center(30, '-'))
# find()查找子串，返回值是第一个字符的索引,若子串不在字符串中，则返回-1
# (可选参数)第二个参数表示检索的索引的起点，第三个参数表示检索索引的终点
print("Hello World".find('ll'))
# ! 与in的区别之一是，in只用于检查单个字符是否包含在字符串中
# join()方法与split相反，用于合并序列元素
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))  # 1+2+3+4+5
dirs = ['', 'usr', 'bin', 'env']
print('C:' + '\\'.join(dirs))  # C:\usr\bin\env
# lower()返回字符串的小写版本
# title()返回字符串中单词的首字母大写版本
# replace()讲指定子串替换为另一个字符串，并返回替换后的结果
# split()切割字符串，返回一个序列
# strip()删除字符串开头和末尾的空白,并返回删除后的结果
# translate()类似replace()，但是该方法只能进行单个字符替换，优势是在于能够同时替换多个字符
# 因此效率要高与replace(),使用前需要建立一个转换表
# 1.建立转换表maketrans() 该方法接受三个参数，两个参数的字符串格式一致，
# 且表达的是将第一个字符串的每一个字符替换成第二个字符串中的相应的字符
# 第三个参数是指定要将那些字母删除
table = str.maketrans("cs", 'kz')
print(table)  # 查看Unicode码点之间的映射
# 2.执行translate() 参数传入转换表
print('This is an incredible test'.translate(table))
print('   123456    '.strip())
print('1+2+3+4+5'.split('+'))
print('This is a test'.replace('is', 'eez'))
print("hello world".title())
"""
附录：其他方法
isalnum、isalpha、isdecimal、isdigit、isidentifier、islower、isnumeric、
isprintable、isspace、istitle、isupper。
"""
# 字典(java中map集合，映射)，是Python中唯一的内置映射类型
# key:value 键值对
phoneBook = {'Alice': '2341', 'Beth': 9102, 'Cecil': '3258'}
# 字典的函数
# 使用dict函数从其他映射或键值对序列创建字典
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
print(dict(name="Gumby", age=42))
# 基本操作
print(len(phoneBook))
print(phoneBook['Alice'])
del d['name']
print('Alice' in phoneBook)
az = {}
az[42] = 'Foobar'
print(az)
# 字典中的方法
# clear()清空
# copy()复制(浅复制)，需要执行深复制，执行copy模块中的deepcopy函数
# fromkeys方法，创建一个新字典，其中包含指定的键，第二个参数设置值，默认值是None
print({}.fromkeys(['name', 'age'], 'a'))
# get()方法，如果试图访问字典中没有的项，不会发生错误，而是返回None
print(phoneBook.get('a'))
# items方法返回一个包含所有字典项的列表
print(phoneBook.items())
# keys()返回一个字典视图，其中包含字典的键
print(phoneBook.keys())
# pop()删除字典的键值对，并把删除的键对应的值对作为返回值返回
newItem = {'x': 1, 'y': 2}
print(newItem.pop('x'))
# popitem()随机删除字典的一项，可以高效地方式逐个删除并处理所有的字典项
# setdefault()类似get(),获取指定的键关联的值，若字典中不包含指定的键时，则执行插入操作
# update() 使用一个字典中的项来更新另一个字典
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'}
x = {'title': 'Python Language Website'}
d.update(x)
print(d)
# values()返回一个有字典的值组成的字典视图，返回的值中不包含重复的值
