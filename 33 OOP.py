
# class Student:
#
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f'Имя {self.__name} \nВозвраст {self.__age} \nНаправление{self.__branch}')
#
#     def access_private_method(self):
#         self._Student__display_details()
#
#
#
# obj = Student('Adam Smith', 25, 'Information Technology')
# obj.access_private_method()

#Inherit

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def get_info(self):
        return f"Person first name - {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def get_hi(self, msgText):
        return f"{msgText}! I am {self.firstName}."


# дочерний класс
class Student(Person):
    spec = "Computer Science"

    def is_successful(self, meanScore):
        return True if meanScore >= 75 else False

    def get_hi(self):
        return f"Waw. I am {self.firstName}."


student1 = Student("Joe", "Black", 30)
print(student1.get_info())
print(student1.get_hi())
print(f"Is {student1.firstName} successful student?. {student1.is_successful(85)}")
# print(student1.fullName) # вызовет ошибку, так как fulName нет ни в Student не в Person

