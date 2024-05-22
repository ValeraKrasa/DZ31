# #OOP part 1


# #Class announcment
# class Cat:
#     #variables of the class
#     paws = 4
#     tail = 1
#     mustache = True
#     head = 1
#     color = 'Red'


#     def __init__(self, color):
#         self.color = color

# #creation of the object

# # my_cat1 = Cat()
# # print(type(my_cat1))
# # print(f'My cat has {my_cat1.tail} tail')
# # print(f'My cat is {my_cat1.color}')

# my_cat2 = Cat('white')
# print(type(my_cat2))
# print(f'My cat has {my_cat2.tail} tail')
# print(f'My cat is {my_cat2.color}')

# my_cat3 = Cat('black')
# print(f'My cat is {my_cat3.color}')


#Task 2

class Student:
    spec = 'Cumputer science'


    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('The Student object has been created')

    def sleep(self):
        return f'Studet {self.name} sleeps during the classes'

    def study(self):
        return f'Student {self.name} studies at the university'

    def name_change(self,new_name):
        self.name = new_name
        return f'A student changed a name'
    def add_age(self):
        self.age += 1

student1 = Student('Pavlo', 25)
print(student1.name)
print(student1.sleep())
print(student1.study())

student2 = Student('Yan', 25)
print(student2.name)
student2.name_change('John')
print(student2.name)
student2.add_age()
print(student2.age)



