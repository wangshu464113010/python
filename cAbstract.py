# 抽象
# 斐波那契数列
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)


# 自定义函数
def fibsFunction(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-1] + result[-2])
    return result


print(fibsFunction(50))


# 给函数写文档
# 在有些地方，如def语句后面（以及模块和类的开头），
# 添加这样的字符串很有用。放在函数开头的字符串称为
# 文档字符串（docstring），将作为函数的一部分存储起来
def square(x):
    'Calculate the square of the number x'  # 函数文档
    return x * x


# 可以使用square.__doc__访问文档
print(square.__doc__)
print(help(square))  # help函数，在交互式解释器中，可使用它获取有关函数的信息，其中包含函数的文档字符串。


def hello_1(greeting, name):
    print('{}, {}'.format(greeting, name))


# 使用参数名称时，传入的参数顺序可以改变(关键字参数)
hello_1(greeting='Hello', name='world')
hello_1(name='world', greeting='hello')


# 形参中的默认值，有默认值得参数，在函数调用的时候可以不必传入参数
# !但是无默认值的参数，在函数调用的时候必须要有参数
def hello_2(name, greeting="Hello", punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))


hello_2("Alice")
hello_2('Tom', 'Hi', '.')


# 收集参数，跟赋值中的*一样
def printName(*params):
    print(params)


printName('Nice', 'to', 'meet', 'you')


# 与赋值时一样，带星号的参数也可放在其他位置（而不是最后），
# 但不同的是，在这种情况
# 下你需要做些额外的工作：必须使用名称来指定后续参数！！！
def in_the_middle(x, *y, z):
    print(x, y, z)


in_the_middle(1, 2, 3, 4, 5, 6, z=7)


# 一个*不会收集关键字参数，若想收集关键字参数，用**
def print_param_3(**params):
    print(params)


print_param_3(x=1, y=2, z=3)  # 指定的名称的就是关键字参数


def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)


# 带*的参数也可以不用传入值
# 作用域(命名空间),vars()函数返回一个不可见的字典，var()函数返回的字典不应修改
# 读取全局变量的值通常不会有问题，但还是存在出现问题的可能性。如果有一个局部
# 变量或参数与你要访问的全局变量同名，就无法直接访问全局变量，因为它被局部变量遮住了。
# 如果需要，可使用函数globals来访问全局变量。这个函数类似于vars，返回一个包含全
# 局变量的字典。（locals返回一个包含局部变量的字典。）
# 例如，如果有一个名为parameter的全局变量，如果无法在函数combine
# 中有一个与之同名的参数。然而，必要时可使用globals()['parameter']来访问它。

# 作用域嵌套，Python中的函数可以嵌套
def f1():
    def f2():
        print("Hello World")

    f2()  # 函数内部访问f2函数
    return 1


print(f1())


# 闭包
def mutiplier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor  # 返回值为一个函数


# 在这里，一个函数位于另一个函数中，且外面的函数返回里面的函数。也就是返回一个
# 函数，而不是调用它。重要的是，返回的函数能够访问其定义所在的作用域。换而言之，它
# 携带着自己所在的环境（和相关的局部变量）！
# 每当外部函数被调用时，都将重新定义内部的函数，而变量factor的值也可能不同
# 像multiplyByFactor这样存储其所在作用域的函数称为闭包。
# 通常，不能给外部作用域内的变量赋值，但如果一定要这样做，可使用关键字nonlocal。
# 这个关键字的用法与global很像，让你能够给外部作用域（非全局作用域）内的变量赋值。
double = mutiplier(3)  # double = multiplyByFactor,factor = 3
print(double(5))  # number = 5 此时double是一个函数


# 递归
# 阶乘
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))


# 不使用递归
def facotial1(n):
    if n == 1 or n == 0:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):  # range包含第一个数，不包含第二个数
            result *= i
        return result


print(facotial1(10))


# 算法：二分查找
def binarySearch(sequence, number, lower, upper):
    if lower == upper:
        assert number == sequence[lower]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return binarySearch(sequence, number, middle + 1, upper)
        elif number < sequence[middle]:
            return binarySearch(sequence, number, lower, middle - 1)
        else:
            return middle


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 0, 9))

# 函数式编程(lambda表达式)，语言Erlang,scheme和Lisp
# Python提供了一些有助于进行这种函数式编程的函数：map、filter和reduce。在较新的
# Python版本中，函数map和filter的用途并不大，应该使用列表推导来替代它们。你可使用map
# 将序列的所有元素传递给函数。
list(map(str, range(10)))  # 与[str(i) for i in range(10)]等价
# lambda表达式
seq = ['foo', 'x41', '!?', "***"]
filter(lambda x: x.isalnum(), seq)
print(seq)
