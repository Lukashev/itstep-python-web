# Lists

# numbers = [10, 20, 30, -40]
# print(numbers[0])
#
# del numbers[-2]
# print(numbers)
#
# numbers.append(90)
# print(numbers)
#
# numbers.insert(10, -68)
# print(numbers)
#
# numbers[-1] = 100
# print(numbers)
#
# print(len(numbers))
#
# numbers = [10, 20, 30, -40]
# for i in range(len(numbers)):
#     print(numbers[i])

# for i in numbers:
#     print(i)

# numbers = [10, 20, 30, -40]
#
# i = 0
#
# while(i < len(numbers)):
#     print(numbers[i])
#     i += 1

# numbers = [10, -20, 30, -40, 10, 90]
# new_list = []
#
# for n in numbers:
#     new_list.insert(0, n) # [-40, 30, -20, 10]
#
# print(new_list)

# numbers = [10, 20, 30, -40]
# total = 0
#
# for n in numbers:
#     total += n
#
# print(total)
#
# num1, num2 = 10, 20
#
# print(num1, num2)
#
# numbers = [10, 20, 30, -40]
# numbers[0], numbers[1] = numbers[2], numbers[3]
# print(numbers)

# unsorted_list = [5, -10, 20, -40, 8, 7, 99]
# # 6 * 6 = 36 steps
# length = len(unsorted_list)
# swapped = True
#
# for i in range(len(unsorted_list) - 1):
#     current = unsorted_list[i]
#     next = unsorted_list[i + 1]
#     if next < current:
#         unsorted_list[i], unsorted_list[i + 1] = next, current
#
# print(unsorted_list)


# unsorted_list = [5, -10, 20, -40, 8, 7, 1]
# # 6 * 6 = 36 steps
# length = len(unsorted_list)
# swapped = True
#
# while swapped:
#     swapped = False
#     for i in range(len(unsorted_list) - 1):
#         current = unsorted_list[i]
#         next = unsorted_list[i + 1]
#         if next < current:
#             unsorted_list[i], unsorted_list[i + 1] = next, current
#             swapped = True
#
# print(unsorted_list)

# from random import random
# print(int(random() * 10))

# from random import random
#
# list_ = []
# for i in range(10):
#     list_.append(int(random() * 10))
#
# print(list_)

# try:
#     hasError = False
#     new_list = []
#     limit = int(input("Enter list limit: "))
#     for i in range(limit):
#         hasError = True
#         while hasError:
#             try:
#                 current = int(input("Enter " + str(i) + " element of the list"))
#                 new_list.append(current)
#                 hasError = False
#             except:
#                 hasError = True
# except Exception as ex:
#     print(ex)
# finally:
#     print(new_list)

# unsorted_list = [5, -10, 20, -40, 8, 7, 1]
# unsorted_list.sort(reverse=True)
# print(unsorted_list)

# list1 = [10, 20, 30]
# list2 = []
#
# list2 = list1[:]
# list2[0] = 40
#
# print(list1, list2)

# list1 = [10, 20, 50, 60, -90, 77]
#
# print(list1[::2])

# list1 = [10, 20, 50, 60, -90, 77]
# print(-90 in list1)
# print(128 not in list1)
# print("q" in "bac")

# list1 = [-10, 50, 20, 77, 60, -90]
# max = list1[0]
#
# for i in list1[1:]:
#     if i < max:
#         max = i
#
# print('Max: ', max)