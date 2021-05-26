# stdout, stdin, stderr
# import sys
# sys.stdout.write("Hello Python")
# sys.stderr.write("Error")
# data = sys.stdin.write()
# print(data)
# path, mode, encoding
# file = open("email.csv")
# data = file.read(1)
#
# while data != "":
#     print(data, end="")
#     data = file.read(1)

# file = open("email.csv")
# data = file.readline()
#
# print(data)
#
# data = file.readline()
#
# print(data)

# file = open("email.csv")
# data = file.read()
#
# for x in data:
#     print(x, end="")

# file = open("./test.txt", mode="w")
# file.write("Hello Python" * 10)
# file.close()
# try:
#     file = open("./test.txt", mode="w")
#     file.write("Hello Python" * 10)
#     file.close()
# except Exception as e:
#     print(e)
# try:
#     file = open("./test.txt", mode="a")
#     file.write("Hello JS" * 2)
#     file.close()
# except Exception as e:
#     print(e)
# try:
#     file = open("./test1.txt", mode="r")
#     file.write("Hello JS" * 2)
#     file.close()
# except Exception as e:
#     print(e)
# with open("email.csv") as file:
#     print(file.read())
# import os
#
# try:
#     os.remove("test1.txt")
# except Exception as e:
#     print(e)
#
# import os
#
# try:
#     os.remove("test.txt")
# except Exception as e:
#     print(e)
# import os
#
# print(os.unlink())
# Read email.csv
# Parse data and create new list.
# Extract first element from list and split with ;
# Use tabulate for rendering table in console.
# import tabulate
# def read_file(a):
#     try:
#         file = open(a)
#         data = file.read()
#         file.close()
#         return data
#     except Exception as ex:
#         print(ex)
#
#
# def parse_data(text=''):
#     rows = text.split('\n')
#     return rows
#
#
#
#
# data = read_file("email.csv")
# parsed_list = parse_data(data)
# print(parsed_list)
# list_1= []
# with open ("unsorted.txt") as f:
#     contents = f.read()
# 
#     list_1=contents.split(",")
#     temp = map(lambda value: int(value),list_1)
#     temp_1 = sorted(temp)
#     print(type(temp_1))
# 
# 
# # print(sorted((temp)))
# with open("unsorted.txt", 'a') as file_1:
#     val = ", ".join(list(map(lambda value: str(value), temp_1)))
#     file_1.write("\n" + val)