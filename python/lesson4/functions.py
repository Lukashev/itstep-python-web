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
# # «амыкание
# hello = 1
# def foo():
#     x = 10
#     def bar():
#         y = 20
#         return x, y, hello
#     def baz():
#         y = 20
#         return x, y, hello
#     return bar
#
# a = foo()
# print(a(), a.__closure__[0].cell_contents)

# def calc(a):
#
#     def mul(b):
#         return a * b
#
#     def div(b):
#         return a / b
#
#     def plus(b):
#         return a + b
#
#     return mul, div, plus
#
# [mul, div, plus] = calc(8)
#
# print(mul(10))
# print(div(10))
# print(plus(10))

# def foo():
#     x = 10
#     def bar():
#         y = 22
#         x = 9
#         return x + y
#     return bar
#
# print(foo()())

#  аррирование

# def sum(a):
#     def foo(b):
#         def bar(c):
#             return a + b + c
#         return bar
#     return foo
#
# print(sum(10)(20)(30))

# def sum(a):
#     def foo(b):
#         def bar(c):
#             return a + b + c
#         return bar
#     return foo
#
# print(sum(10)(20)(30))

# def sum(a, b, c):
#     return a + b + c


# def curry(func):
#     def inner(*args1):
#         if len(args1) == func.__code__.co_argcount:
#             return func(*args1)
#         else:
#             def bar(*args2):
#                 return inner(*(args1 + args2))
#             return bar
#     return inner
#
#
# fn = curry(sum)
#
# print(fn(10)(20)(30))
# print(fn(10, 20, 30))
# print(fn(10, 20)(30))
# print(sum(10, 20, 30))
# print(sum(10,20)(30))

# ƒекораторы

# from datetime import datetime as dt
#
#
# def get_time(func):
#     def inner():
#         start = dt.now()
#         res = func()
#         print(dt.now() - start)
#         return res
#     return inner
#
#
# @get_time
# def test1():
#     res = [x for x in range(10000) if x % 2 == 0]
#     return res
#
#
# @get_time
# def test2():
#     result = []
#     for x in range(10000):
#         if x % 2 == 0:
#             result.append(x)
#     return result
#
#
# print(test1())
# print(test2())
#
# fn = get_time(test1)
# print(fn())

#  ортежи, словари, множества

# a = (1, 2, 3)
#
# print(a)
#
# a = tuple("Hello World")
# print(a)
#
# a = tuple([1, 10, 2])
# print(a)
#
# a = 1, 2, 3
# print(a)
#
# # a[0] = 100
#
# print(a + (2, 4, 5))
#
# b = (1, 2, 3)
# c = [1, 2, 3, 'abc']
#
# print(a.__sizeof__(), c.__sizeof__())

# a = ([1, 2], [1, 2])
#
# a[0][0] = 100
#
# a[0] = [2, 3]
#
# print(a)

# a = {}
#
# print(a)
#
# a = {'a': 1, 'b': 2}
#
# print(a)
#
# key = 'a'
#
# a = {key: 1, 'b': 10}
#
# print(a)
#
# a['a'] = 100
#
# print(a)
#
# a = dict(a=5, c=10, b=2**3)
#
# print(a)

# a = dict([('a', 1), ('b', 2), ('c', 3)])
#
# print(a)


# a = {i: val**2 for i, val in enumerate([20, 30, 5])}
#
# print(a)

# a = { i: i for i in range(2, 10) if i % 2 == 0}
# print(a)

# a = { 'a': 20, 'b': 30, 'c': 40 }
#
# for key in a:
#     print(key)

# a = { 'a': 20, 'b': 30, 'c': 40 }
#
# for key in a:
#     print(a[key])

# print(2 in (2, 3, 5))

# print('a' in { 'a': 1, 'b': '2'})

# a = {'a': 20, 'b': 30, 'c': 40}
#
# b = a.copy()
#
# b['a'] = 100
#
# print(id(a), id(b), a, b)

# a = {'a': 20, 'b': 30, 'c': 40}
#
# b = a.pop('a')
#
# print(b)

# a = {'a': 20, 'b': 30, 'c': 40}
#
# b = a.popitem()
#
# print(b)

# a = {'a': 20, 'b': 30, 'c': 40}
#
# b = (1, 2, 3)
#
# a[b] = 100
#
# print(a)
# print(a[b])
# print(a[(1,2,3)])

# a = {'a': 20, 'b': 30, 'c': 40}

# print(a['e'])
# print(a.get('e'))

# a = {'a': 20, 'b': 30, 'c': 40}

# a.clear()
#
# print(a)

# print(a.keys())
#
# for key in a.keys():
#     print(key)
#
# for val in a.items():
#     print(val)
#
# for val in a.values():
#     print(val)

# b = {}.fromkeys(['c', 'b'], 100)
#
# print(b)

# b = {}.fromkeys([x for x in range(10)], 100)
#
# print(b)

# a = [1, 1, 2, 3, 6, 6]
#
# print(set(a))

# a = [(1, 2), (1, 2)]
# print(set(a))

# a = {1, 2, 3}
#
# print(a.difference({1, 2}))

# a = { 1, 2, 3}
#
# print(a.intersection({1, 2}))

# a = { 1, 2, 3}
# print(a.isdisjoint({4, 5, 6}))

# A = {1, 2}
# B = {2, 3, 4}
# C = {5}
#
# print(A.union(B).union(C))


# ¬ы живете в городе, где все дороги расположены в идеальной сетке.
# ¬ы пришли на прием на 10 минут раньше, поэтому решили прогул€тьс€.
# √ород предоставл€ет своим гражданам приложение дл€ построени€ пешеходов
# на их телефонах - каждый раз, когда вы нажимаете кнопку, он отправл€ет
# вам массив однобуквенных строк, представл€ющих маршруты ходьбы
# (например, ['n', 's', 'w', 'е']).
# ¬ы всегда проходите только один квартал дл€ каждой буквы (направлени€),
# и вы знаете, что вам понадобитс€ 1 минута, чтобы пройти один городской
# квартал.
# ѕоэтому создайте функцию, котора€ вернет true, если прогулка, которую
# дает вам приложение, займет у вас ровно 10 минут  и, конечно же, вернет
# вас в исходную точку. ¬ противном случае верните false.
#
# ѕримечание: вы всегда будете получать действительный массив, содержащий
# случайный набор букв направлени€ (только Ђnї, Ђsї, Ђeї или Ђwї).
# ѕустого массива никогда не будет.

# def is_valid_walk(walk):
#     pass

# print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']));  False
# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])); // True
# print(is_valid_walk(['w'])); // False
# print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])); // False
