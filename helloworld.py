#print(100)
#》》》》》》》》》》》》》》》》list
#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
#classmates = ['Michael', 'Bob', 'Tracy']
#print(classmates)

#》》》》》》》》》》》》》》》》元组
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
#classmates = ('Michael', 'Bob', 'Tracy')

# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

#》》》》》》》》》》》》》》》》循环
# 1.for...in循环，依次把list或tuple中的每个元素迭代出来：
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
# 2.while 循环
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# break 跳出循环 continue 跳过本次循环

#》》》》》》》》》》》》》》》》字典
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
# d['Michael']=100
# print(d['Michael'])
# print('Michael' in d)

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
# add(e) remove(e)
# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

# 函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回

#导入其它文件函数 from 文件名 import 函数名
# from utils import my_abs
# print(my_abs(-5))

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
# def nop():
#     pass
#
# if age >= 18:
#     pass
# 缺少了pass，代码运行就会有语法错误

# 返回多个函数
# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
#
# >>> r = move(100, 100, 60, math.pi / 6)
# >>> print(r)
# (151.96152422706632, 70.0)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s