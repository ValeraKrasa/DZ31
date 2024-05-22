
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        return f'{self.name} is {self.age} years old'
    
    def speak(self, mas):
        return f'{self.name} says {mas}'

jack = Dog('Jack', 4)
print(jack.description())
print(jack.speak('Woof Woof'))


# class Student:
#     def __init__(self, name, age, branch):
#         #  задаем приватные праметры
#         self.__name = name
#         self.__age = age
#         self.__branch = branch

#     def __display_details(self):
#         print(f'Name: {self.__name}\nAge:{self.__age}\nBranch:{self.__branch}')
    
#     def access_private_method(self):
#         self.__display_details()

# obj = Student('Adam Smith', 25, 'Information technology')
# obj.access_private_method()

