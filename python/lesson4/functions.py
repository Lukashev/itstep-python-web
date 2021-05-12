# Functions
# PI = 3.14
# 1. Пример функции
# print(sum([10, 20, 30]))
# def foo(a, b):
#     return a + b
#
# print(foo(10, 20))
# Global
# def bar():
#     global a
#     a = 11
#     print(a)
#
# bar()
#
# print(a)
# def foobar():
#     a = 1
#     b = 2
#
#     def inner():
#         return a + b
#
#     def outer():
#         return a * b
#
#     return inner, outer
#
#
# fn = foobar()
# print(fn[0]())
# print(fn[1]())
# for x in fn:
#     print(x())
# Ключевые аргументы, примеры
# def foo(a=12, b=0):
#     return a + b, a * b
# print(foo(10, 20))
# result = foo(a=5, b=12)
# print(type(result), result[1])
# Аргументы в виде словаря **
# def foo(a, b, c):
#     return a + b + c
#
# print(foo(10, 20, 30))
#
# params = {'b': 10, 'c': 20, 'a': 30}
# print(foo(**params))
# Мутабельность объектов, [:]
# a = [1, 2, 3]
# b = a[:]
# b[-1] = 30
# print(a, b)
# def foo(mutable=None, a=1):
#     if mutable == None: mutable = []
#     mutable.append(1)
#     print(id(mutable), mutable)
#
#
# foo(a = 2), foo(a=3), foo(a=4)
# constants = (3.14, 20, 30)
# constants[1] = 35
# def findmagic(a=[]):
#     for i in range(len(a)):
#         if i == a[i]:
#             return i
#
# print(findmagic([-20, -10, 2, 10, 20]))
# def find_index(list_1):
#     for i in range(len(list_1)):
#         if i==list_1[i]:
#             return i
#
#
# list_2=[ 1,2,2,7,7]
# print(find_index(list_2))
# n1 = int(input("Введите целое число: "))
# n2 = 0
# def reverse_number(n):
#     n2=0
#     # if n<0:
#     #     n1=abs(n)
#     # else:
#     #     n1=n
#     n1 = abs(n) if n < 0 else n
#     while n1 > 0:
#         digit = n1 % 10
#         n1 = n1 // 10
#         n2 = n2 * 10
#         n2 = n2 + digit
#     if n<0:
#         return -(n2)
#     return n2
#
# print(reverse_number(n1))
# def reverse(a):
#     stroka = str(a)
#     res = stroka[::-1]
#     if a < 0:
#         return int('-' + res[0:-1])
#     else:
#         return int(res)
#
#
# print(reverse(3246))
# print(reverse(120))
# def rev(a):
#
#     res = ''
#
#     for i in str(a)[::-1]:
#
#         res+=i
#
#     if res[-1] == "-":
#
#         return int(res[-1] + res[:-1])
#
#     return int(res)
#
# print(rev(0))
# def foo(start, end):
#     result = 0
# range(min(start, end), max(start, end)
# 15251
# i = 0, len(str) = 5
# i str - i
# Мутабельность объектов, [:]
# def foo(a):
#     a[0] = 100
#     print(id(a))
#
# l1 = [2, 3, 5]
# foo(l1[:])
#
# print(id(l1))
# Позиционные аргументы *
# def foo(*args, **kwargs):
#     print(args, kwargs)
#
# print(foo(1, 5, 3, 5, 6, a=5))
# def custom_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result
#
# print(custom_sum(2, 3, 5, 10))
# def custom_sum(*args):
#     return sum(args)
#
# print(custom_sum(2, 3, 5, 10))
# def insert(**kwargs):
#     db.create(kwargs)
# def custom_sum(*args):
#     """
#     This function return the sum of all arguments
#     :param args:
#     :return:
#     """
#     result = 0
#     for x in args:
#         result += x
#     return result
#
#
# custom_sum.__doc__ += "Hello Python!"
#
# print(custom_sum.__doc__)
# Поля и методы функций
# def custom_sum(*args):
#     return sum(args)
#
#
# print(dir(custom_sum))
# print(custom_sum.__module__)
# def factorial(n):
#     if n > 1:
#         return n * factorial(n - 1)
#     return 1
#
# print(factorial(3))
# 3 6
# return 3 * factorial(3 - 1)
# return 2 * factorial(2 - 1)
# 1
# from datetime import datetime
#
# def fibonaci(n):
#     if n in (1, 2):
#         return 1
#     return fibonaci(n - 1) + fibonaci(n - 2)
#
#
# start = datetime.now()
# print(fibonaci(100))
# print('Date', datetime.now() - start)
# Переназначение встроенной функции

# sum = {"a": 1}
# del sum
# print(sum([1,3,4]))
# Лямбды
# a = lambda *args: [x for x in range(args[0])]
#
# print(a(3))
# Функции map(), reduce(), filter(), zip()
# def cubic(n):
#     return n**3
#
# l1 = [2,3,4]
#
# a = map(cubic, l1)
#
# print(list(a))
#
# print(list(map(lambda n: n**3, [2,3,4])))
# fn = lambda n: n**3
#
# print(list(map(fn, [2,3,4])))
# from functools import reduce
#
# l1 = [x for x in range(2, 20) if x % 2 == 0]
#
#
# print(reduce(lambda acc, n: acc * n, l1, 1))
# 1
# 1 * 2
# 2 * 3
# 6 * 4
# from functools import reduce
#
# l1 = [x for x in range(2, 20) if x % 2 == 0]
#
# print(reduce(lambda acc, n: acc * n, l1, 1))
# 0 = True
# 1 or 2 or 3 - True
# l = lambda n: n % 2 != 0
# l1 = [x for x in range(2, 19)]
# print(list(filter(l, l1)))
#
# l1 = ["John", "Alex", "Steve", "Ibrahimovic"]
# l2 = [20, 30, 40]
#
# print(list(zip(l1, l2)))
# print(dict(zip(l1, l2)))