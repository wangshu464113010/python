# 对象
# 多态，封装，继承
# 多态，isinstance函数
# 类 同C++/java
# 父类/超类-子类
__metaclass__ = type  # 使用Python2，请包含该行代码


# 旧式类和新式类是有差别的。
# 现在实在没有理由再使用旧式类了，但在Python 3之前，默
# 认创建的是旧式类。


class Person:

    def setName(self, name):  # self表示对象自身
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello World! I'm {}.".format(self.name))


# 简单的类
foo = Person()
bar = Person()
foo.setName("Alice")
bar.setName("Luke")
foo.greet()
bar.greet()
foo.name = "Tom"
# 属性、函数和方法
# 可以使用一个变量指定一个方法
newVar = foo.greet
newVar()


# 私有化：使其(属性/方法)名称前面加两个_
class A:
    def __a1(self, __a=2):  # 私有方法
        print("Hello World1")

    def get__a(self):
        print(self.__a)

    def a2(self):
        print("Hello World2")


a = A()  # 此时对象a不能调用__a1()方法
a._A__a1()  # 但是可以这种方式调用__开头的私有方法【_类名方法名/属性名】
a._A__a = 1
a.get__a()


# 上述私有方式只是一种规范(约定)
# from module import * 不会导入以下划线打头的名称

# 指定超类
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):  # 该类继承了Filter类
    def init(self):  # 重新超类中的init方法
        self.blocked = ['SPAM']
    # filter方法直接继承了超类的


f = Filter()
f.init()
print(f.filter([1, 2, 3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))

# 判断一个类是否是另一个类的子类,可以使用内置方法issubclass
print(issubclass(SPAMFilter, Filter))
# 了解一个类的基类，访问其特殊属性__bases__
print(SPAMFilter.__bases__)
# 判断对象是否是一个类的实例isinstance,还可以访问属性__class__
print(isinstance(s, Filter))
print(s.__class__)


# 多重继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi, my value is ", self.value)


class TalkingCalculator(Calculator, Talker):  # 多继承
    pass


tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
# 多个超类的超类相同时，查找特定方法或属性时访问超类的顺序称为方法解析顺序（MRO），使用的算法非常复杂。

# 内省
# 检查方法是否存在hasattr函数
print(hasattr(tc, 'talk'))
# 检查属性talk是否可以调用，callable,getattr
print(callable(getattr(tc, 'talk', None)))
# setattr与getattr功能相反，可用于设置对象的属性
setattr(tc, 'name', 'Miss Alice')
print(tc.name)
# 等等，后续详细讲解

# 抽象基类,抽象类是不能够实例化的类(至少是不应该)，职责是定义子类应实现的一套抽象方法
# 抽象类，python通过引入abc模块提供官方的解决方案
from abc import ABC, abstractmethod


class aTalker(ABC):
    @abstractmethod  # 装饰器,后面详解，该装饰器表示将方法标记为抽象的
    def talk(self):
        pass


class Knigget(aTalker):  # 该类没有重现抽象方法talk，故也是抽象类
    pass


class Knigget1(aTalker): # 该类不是抽象的
    def talk(self):
        print("Hi")


atalker = Knigget1()
atalker.talk()
