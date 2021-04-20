# num1 = 10

# try:
#     print("1231")
#     res = num1 / 0
# except ZeroDivisionError:
#     print("Zero Exception") 
# except NameError:
#     print("NameError")       
# finally:
#     print("Done")

# Для записывания ошибок в базу данных или в файл, для того , чтобы потом увидеть в каком месте произошло исключение (ошибка).
# Чтобы показать клиенту ошибку сервера.

# num1 = 10

# try:
#     res = um1 / 0
# except (ZeroDivisionError, NameError):
#     print("Zero Exception and NameError")      
# finally:
#     print("Done")

# num1 = 20
# num1 -= 10

# try:
#     if num1 == 10:
#         raise Exception("This value is 10")
# except Exception as ex:
#     print(ex)


