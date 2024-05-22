
#levels of access.
#Public, Private, Protected

# import random
#
# class Person:
#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age
#
#         #private -
#         self.__personID = random.randint(1, 100)
#
#
#         # public methods
#     def get_info(self):
#         return f"Person first name - {self.firstName}; last name - {self.lastName}; age - {self.age}."
#
#     def get_hi(self, msgText):
#         return f"{msgText}! I am {self.firstName}."
#
#     def change_age(self):
#         self.age += 1
#     def __getID(self):
#         return f'{self.__personID}\n'
#
#
#
#
# person1 = Person("Joe", "Black", 30)
# print(person1.get_info())
# # можем изменить содержимое публичного атрибута класса
# person1.__personID = 100
# print(person1.get_info())
# person1.__getID()
# # person1.change_age()
# # print(person1.get_info())

class Student:

    def __init__(self, __name, __age, __branch):

        