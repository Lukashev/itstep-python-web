# stack = []
#
#
# def push(val):
#     """
#     We append element to the end of the list
#     :param val:
#     :return:
#     """
#     stack.append(val)
#
#
# def pop():
#     """
#     We get element from the last position of list
#     :return:
#     """
#     val = stack[-1]
#     del stack[-1]
#     return val
#
#
# for x in range(5):
#     push(x)
#
#
# print(stack)
# print(pop())
# print(stack)
# print(pop())
# print(stack)
# class Stack(object):
#     stackList = []
#
#     def push(self, val):
#         self.stackList.append(val)
#
#     def pop(self):
#         val = self.stackList[-1]
#         del self.stackList[-1]
#         return val
#
#
# ### CLIENT CODE
#
# stackObject = Stack()
#
# print(stackObject)
# # We check if stackOBject is subclass of Stack
# print(isinstance(stackObject, Stack))
#
# for x in range(5):
#     stackObject.push(x)
#
# print(stackObject.stackList)
#
# print(stackObject.pop())
# print(stackObject.stackList)
# Here we apply inheritance paradigm
# class Stack(object):
#     stackList = []
#
#     def push(self, val):
#         self.stackList.append(val)
#
#     def pop(self):
#         val = self.stackList[-1]
#         del self.stackList[-1]
#         return val
#
#
# class AddingStack(Stack):
#
#     sum = 0
#
#     def __init__(self):
#         self.stackList = self.stackList[:]
#
#     def push(self, val):
#         self.sum += val
#         self.stackList.append(val)
#
#     def pop(self):
#         val = self.stackList[-1]
#         self.sum -= val
#         del self.stackList[-1]
#         return val
#
# addingStack = AddingStack()
#
# for x in range(5):
#     addingStack.push(x)
#
# print(addingStack.sum)
# print(addingStack.stackList)
#
# print(addingStack.pop())
# print(addingStack.sum)
# print('OBJ', addingStack.stackList)
# print('CLASS', AddingStack.stackList)
# class Stack(object):
#     """
#     This is Stack
#     """
#     stackList = []
#
#     def __init__(self):
#         print("Constructor")
#
#     def __del__(self):
#         print("Destructor")
#
#     def __str__(self):
#         return f"<Stack: {​​​len(self.stackList)}​​​>"
#
#     def push(self, val):
#         self.stackList.append(val)
#
#     def pop(self):
#         val = self.stackList[-1]
#         del self.stackList[-1]
#         return val
#
# stackObject = Stack()
# print(dir(stackObject))
# stackObject.push(10)
# print(Stack.__dict__)
# for x in Stack.__dict__:
#     print(x, Stack.__dict__[x])
# class Person:
#     name = 'John'
#     age = 26
#
#     def __str__(self):
#         return str(self.as_dict())
#
#     def as_dict(self):
#         return {​​​'name': self.name, 'age': self.age}​​​
#
#
# p = Person()
#
# # print(p)
# # print(p.as_dict())
#
# print(p)
# class Person:
#     _name = 'John'
#     _age = 26
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.getter
#     def age(self):
#         return f"<Person: {​​​self._age}​​​>"
#
#     @age.setter
#     def age(self, value):
#         if str(value).isdigit():
#             self._age = value
#         else:
#             raise ValueError("Value of age should gonna be number...")
#
# try:
#     p = Person()
#     print(p.age)
#     p.age = 32
#     print(p.age)
# except Exception as ex:
#     print(ex)
# class Person:
#     _name = 'John'
#     _age = 26
#
#     def get_age(self):
#         return f"<Person: {​​​self._age}​​​>"
#
#     def set_age(self, value):
#         if str(value).isdigit():
#             self._age = value
#         else:
#             raise ValueError("Value of age should gonna be number...")
#
#     age = property(get_age, set_age)
#
# try:
#     p = Person()
#     print(p.age)
#     p.age = 32
#     print(p.age)
# except Exception as ex:
#     print(ex)
# class Person:
#     _name = 'John'
#     _age = 20
#     _names = []
#
#     # def __getattribute__(self, item):
#     #     print(f"Attribute: {​​​item}​​​")
#     #     return item
#     def __init__(self, names):
#         self._names= [None] * names
#
#     def __setitem__(self, idx, data):
#         self._names[idx] = data
#
#     def __getitem__(self, item):
#         print(f"Item: {​​​item}​​​")
#         return self._names[item]
#
#     def get_age(self):
#         return f"<Person: {​​​self._age}​​​>"
#
#     def set_age(self, value):
#         if str(value).isdigit():
#             self._age = value
#         else:
#             raise ValueError("Value of age should gonna be number...")
#
#     age = property(get_age, set_age)
#
#
# p = Person(8)
# p[0] = "Alex"
# print(p[0])
# class Person:
#     __name = 'John'
#     __age = 26
#
#     def __get_info(self):
#         return f"Name: {​​​self.__name}​​​, Age: {​​​self.__age}​​​"
#
# try:
#     p = Person()
#     print(p._Person__get_info())
# except Exception as ex:
#     print(ex)