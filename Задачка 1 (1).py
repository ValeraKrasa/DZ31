class Vector:
    
    def __init__(self, *args):
            a = []
            for i in args:
                if isinstance(i, int):
                    a.append(i)
            self.values = sorted(a)

    def __str__(self):
        if self.values:
            b = [str(i) for i in self.values]
            return f'Вектор({', '.join(b)})'
        else:
            return 'Пустий вектор'

    def __add__(self, other):
        if isinstance(other, int):
            b = [i + other for i in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values)==len(self.values):
                b = [i  for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print('Додавання векторів різної довжини не можливо')
        else:
            print(f'Вектор не можна скласти з {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            b = [i * other for i in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(other.values)==len(self.values):
                b = [i[0] * i[1]  for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print('Множення векторів різної довжини не можливо')
        else:
            print(f'Вектор не можна помножити на {other}')        
        
v1 = Vector(1, 2, 3, 5, 7, 4)
print(v1)
v2 = Vector()
print(v2)
v3 = v1 + v2
print(v3)
v4 = v3 + 5
print(v4)
v5 = v1 * 2
print(v5)
v5 + 'hi'
