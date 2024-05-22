#  povtor
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Student(Human):
    # атрибут екзмепляра класа
    spec = 'Computer scine'

    def __init__(self, name, age, student_ID):
        super().__init__(name, age)
        self.student_ID = student_ID

    # метод екзмепляра класcа
    def change_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f'Student: {self.name}. Age: {self.age}. Student_ID: {self.student_ID}' 

    def __repr__(self):
        return f'Obj class Student'
    
    def __eq__(self, otherObj):
        if self.age == otherObj.age:
            return True
        else:
            return False

    def __gt__(self, otherObj):
        if self.age > otherObj.age:
            return True
        else:
            return False


        # метод класса
    @classmethod
    def change_spec(cls, new_spec):
        cls.spec = new_spec

    # static method
    @staticmethod
    def say_hi():
        print('Hello student')

    
student1 = Student('Adam', 25, 'CS_123')
student1.change_age(27)
print(student1.spec)
Student.change_spec('data analyst')
student2 = Student('Jon', 22, 'CS_125')
print(student2.spec)
student1.say_hi()

print('****')

# материал урока - Magic-методы, конструкторы
# все маг. методы имеют двойное подчеркивание в имени - __init__()
# method __init__() 

# method __str__() - метод что візивается при print()
# method __repr__() - метод что візивается при обращении в объкету
# если нет __str__ то имеем <__main__.Student object at 0x0000022771C90590>
# а если есть, то ...
print(student1)

# object.__lt__(self, other) - сравнение <
# object.__le__(self, other) - сравнение <=
# object.__eq__(self, other) - сравнение ==
# object.__ne__(self, other) - сравнение !=
# object.__gt__(self, other) - сравнение >
# object.__ge__(self, other) - сравнение >=

# сравним двух студентов по возрасту на == -> __eq__
print(student1 == student2) # Fasle

print(student1 > student2) # True

print(student1 < student2) # False, но __lt__ мы не задавали )))

# математические действия
# __add__ - +
# __mul__ - *
# __sub__ - -
# __truediv__ - /


