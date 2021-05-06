# from random import random
# print([int(random() * 10) for i in range(10)])
# print([[i * j for j in range(10)] for i in range(10)])
# print([x for x in range(1, 11) if x % 2])
# greeting = "Hello Python"
# print(greeting[0])
# print(len(greeting))
# print("Py" in greeting)
# print("Zebra" in greeting)
# for c in greeting:
#     print(c, end='')
# greeting = "Hello Python"
#
# print(greeting[1:4])
# print(greeting[::-1])
# print(greeting[:3])
# print("Hello" + "World")
# greeting = "Hello Python"
#
# print(greeting.capitalize())
# print(greeting.upper())
# print(greeting.lower())
#
# greeting = "    Hello Python     "
#
# print(len(greeting))
# greeting = greeting.rstrip()
# print(len(greeting))
# print(len(greeting))
# greeting = greeting.strip()
# print(len(greeting))
# greeting = "hello python javascript and java"
# print(greeting.title())
# greeting = "hello,python,javascrip,java"
# print(greeting.replace("a", 'X'))
#
# print(greeting.split(','))
# print("We have " + str(12) + " chair in our shop")
# print("We have {} chair in our shop".format(12))
# print("We have {} chair {} in our shop".format(12, 99))
# print("We have {b} chair {a} in our shop".format(a=12, b=99))
# greeting = "Python"
# print(f"Hello {greeting}") # > 3.7
# print("%s - %d" % ("Hello", 12))
# a = "banana"
#
# print(a.count("a"))
# print(a.zfill(10))
# print(a.find("n"))
# print("abc".isdigit())
# print("abas123".isdigit())
# print(ord("A"))
# print("a" > "A")
# print(chr(ord("A")))
# print(min("A", "B", "Q"))
# sentence = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
# result = ""
#
# for c in sentence:
#     if c == " ":
#         result += " "
#         continue
#     if c.isdigit():
#         continue
#     c = c.upper()
#     cur = ord(c)
#     result += chr(cur - 3) if c >= "D" else chr(cur + 23)
#
# print(result)