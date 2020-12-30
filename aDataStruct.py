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
print("Tom ,%s,%s"% values1)










