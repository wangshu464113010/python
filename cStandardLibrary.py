# 模块，标准库
import sys
import zhello  # 自定义的模块，当前路径
# 包
import a # 导入包中的的模块，导入包时，默认执行__init__.py文件中的内容

print(sys.path.append('C:/python'))

# 标准库sys
# 函数/变量    描 述
# argv        命令行参数，包括脚本名
# exit([arg]) 退出当前程序，可通过可选参数指定返回值或错误消息
# modules     一个字典，将模块名映射到加载的模块
# path        一个列表，包含要在其中查找模块的目录的名称
# platform    一个平台标识符，如sunos5或win32
# stdin       标准输入流——一个类似于文件的对象
# stdout      标准输出流——一个类似于文件的对象
# stderr      标准错误流——一个类似于文件的对象

# os
# 函数/变量         描 述
# environ         包含环境变量的映射
# system(command) 在子shell中执行操作系统命令
# sep             路径中使用的分隔符
# pathsep         分隔不同路径的分隔符
# linesep         行分隔符（'\n'、'\r'或'\r\n'）
# urandom(n)      返回n个字节的强加密随机数据

# 集合set，堆(heapq)，双端队列(deque)
# time(时间)，random(随机数)，shelve(永久性映射)，re(正则)
