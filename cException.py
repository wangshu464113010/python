# 异常Exception
# raise语句引发异常
# raise Exception
# 1/0
# raise Exception("hyperdriver overload")
# 一些内置的异常类
# Exception 几乎所有的异常类都是从它派生而来的！！！
# AttributeError 引用属性或给它赋值失败时引发
# OSError 操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
# IndexError 使用序列中不存在的索引时引发，为LookupError的子类
# KeyError 使用映射中不存在的键时引发，为LookupError的子类
# NameError 找不到名称（变量）时引发
# SyntaxError 代码不正确时引发
# TypeError 将内置操作或函数用于类型不正确的对象时引发
# ValueError 将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
# ZeroDivisionError 在除法或求模运算的第二个参数为零时引发
from warnings import warn  # 警告模块


# 自定义异常类 ,继承Exception即可
class someCustomException(Exception): pass


# 捕获异常
# try/except
try:  # 下面下可能发生异常的代码
    x = int(input('Enter the first number:\n'))
    y = int(input('Enter the second number:\n'))
    print((x / y))
except ZeroDivisionError:  # 处理异常
    print("The second number can't be zero!")
except TypeError:
    print("Other exception")


# 捕获异常后，如果需要重新已发它(即继续向上传播)，可调用raise且不提供任何参数
class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise  # 用于测试


calculator = MuffledCalculator()
calculator.calc('10/1')  # 把1改成0，可测试上述代码

# 多个异常的情况不止可以使用多个except语句,还可以使用以下情况
try:
    a = int(input('Enter the first number:\n'))
    b = int(input('Enter the second number:\n'))
    print((a / b))
except (ZeroDivisionError, TypeError, NameError) as e:  # 若想要异常的对象(e)
    print('Your numbers were bogus ...')
    print(e)

# 一网打尽（不建议使用）
try:
    a = 10
    b = 0
    c = a / b
except:
    print("Something wrong happened ...")

# try/except语句后面可以添加else语句
while True:
    try:
        pass
    except:
        print("Invalis input. Please try again.")
    else:  # 用于退出死循环
        break
# finally语句，用于在发生异常时执行清理工作
try:
    x = 1 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print('Cleaning up ...')
    del x
# 警告，模块warnings中的函数warn

warn("I've got a bad felling about this.")
