# 文件
# open函数中的mode的常见取值
#  r  读取模式(默认值)
#  w  写入模式
#  x  独占写入模式
#  a  附加模式
#  b  二进制模式（与其他模式结合使用）
#  t  文本模式(默认值)
#  +  读写模式（与其他模式结合使用）
import fileinput  # 实现延迟迭代
f = open('zhello.txt', 'r')
print(f.readlines())  # 读取多行
string = f.read(4)
print(string)
print(f.read())
f = open('zhello.txt', 'w')
f.write('Hello,')
f.write('World\n')
f.write("line2\n")
f.close()
# 迭代文件内容
with open('zhello.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
# 使用fileinput实现延迟迭代
for line in fileinput.input('zhello.txt'):
    print(line)