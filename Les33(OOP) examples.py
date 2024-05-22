

# class Student:
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#         print('The Student object has been created')
#
#     def __display_details(self):
#         return f"Name: {self.__name}\nAge: {self.__age}\nFaculty: {self.__branch}"
#
#     def access_private_method(self):
#         return self.__display_details()
#
# # Create an instance of Student
# obj = Student('Adam', 25, 'IT')
# # Access the private method and display the details
# print(obj.access_private_method())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age}'
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
#
# obj = Dog('Josh', 3)
# print(obj.description())
# print(obj.speak('Woof'))


class Robot:
    robots = 0
    def __init__(self, name):
        self.name = name
        Robot.robots += 1
        print(f'You have {Robot.robots}')
        print(f'{self.name} was cretaed')

    def destroy(self):
        Robot.robots -= 1

        print (f'{self.name} was destroyed')
        print (f'You have {Robot.robots}')

    def say_hello(self):
        print (f'{self.name} is greeting you, human being')

    @classmethod
    def how_many(cls):
        print (f'You have {Robot.robots} left')

d1 = Robot('d2r2')
Robot.how_many()
d1.say_hello()
d1.destroy()
Robot.how_many()
