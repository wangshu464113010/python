# 构造函数(constructor),python中的构造函数__init__
class FooBar:
    def __init__(self):  # 构造函数
        self.somevar = 42

    def __del__(self):  # 析构函数,在对象被销毁（作为垃圾被收集）前被调用，但鉴于你无法知道准确的调用时间，建议尽可能不要使用__del__。
        pass


f = FooBar()
print(f.somevar)


# super调用父类的内容
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No,thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()
sb.eat()


# 元素访问item
# __len__(self)：返回集合包含的项数
# __getitem__(self,key):返回与指定键关联的值
# __setitem__(self,key,value):存储键值对
# __delitem__(self,key):对对象的组成部分使用__del__语句是被调用

def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value


s = ArithmeticSequence()
print(s[4])


# 静态方法和类方法
# @staticmethod   @classmethod
# 类名调用，与java类似

# _getattr__、__setattr__等方法
#  __getattribute__(self, name)：在属性被访问时自动调用（只适用于新式类）。
#  __getattr__(self, name)：在属性被访问而对象没有这样的属性时自动调用。
#  __setattr__(self, name, value)：试图给属性赋值时自动调用。
#  __delattr__(self, name)：试图删除属性时自动调用。
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

# 迭代器 __iter__用于返回一个对象,__next__
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b, self.b +self.a
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
# 更正规的定义是，实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器。

# 生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested = [[1,2],[3,4],[5]]
print(list(flatten(nested)))

# yield语句的函数都被称为生成器。这可不仅仅是
# 名称上的差别，生成器的行为与普通函数截然不同。差别在于，生成器不是使用return返回一个
# 值，而是可以生成多个值，每次一个。每次使用yield生成一个值后，函数都将冻结，即在此停
# 止执行，等待被重新唤醒。被重新唤醒后，函数将从停止的地方开始继续执行。

# 递归生成器
def flatten1(nested):
    try:
        for sublist in nested:
            for element in flatten1(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten1([[1, 2], 3, 4, [5, [6, 7]], 8])))

# 通用生成器，
# 生成器由两个单独的部分组成：生成器的函数和生成器的迭代器。生成器的函数
# 是由def语句定义的，其中包含yield。生成器的迭代器是这个函数返回的结果。用不太准确的话
# 说，这两个实体通常被视为一个，通称为生成器。
def simple_generator():
    yield 1

# 生成器方法
# throw：用于在生成器中（yield表达式处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
# close：用于停止生成器，调用时无需提供任何参数。
# 等等
