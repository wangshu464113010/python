# 模块 import 关键字引入math模块
import math  # math默认引入了
from math import sqrt  # 导入函数
import cmath
# 数学函数
print("---------math function---------")
print("pow(10, 2) = " + str(pow(10, 2)))  # 乘方函数
print("abs(-10) = " + str(abs(-10)))  # 绝对值
print("round(1.5) = " + str(round(1.5)))  # 取整  四舍五入

# 可使用math.pow()调用函数
print("math.floor(-36.1) = " + str(math.floor(-36.1)))  # 取整  往负无穷方向取整
print("math.ceil(32.3) = " + str(math.ceil(32.3)))  # 取整  往正无穷方向取整
print("sqrt(1) = " + str(sqrt(1)))  # 开方
# cmath和复数
print("cmath.sqrt(-1) = " + str(cmath.sqrt(-1)))  # 1j
print("(1+3j)+(2+4j) = " + str((1+3j)+(2+4j)))  # 复数支持

print("---------强转---------")
# 强转 不是函数
print(int(12.3))
print(float(10))
print(str(123456))



