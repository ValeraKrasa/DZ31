# lambda - лямда функции

# функция в одну строку
# lambda arg1, agr2,... : выражение

# standart def
##def add10(x):
##    return x + 10
##
##number = add10(10) # -> 20
##
### lambda
##new_number = lambda x: x + 10

# Задание - имеем на входе список целых чисел
# Надо получить список квадратов этих чисел
numbers = [1, 2, 3, 4, 5]
list_numbers = lambda x: x ** 2
for number in numbers:
    print(list_numbers(number))


# zip() - функция высшего порядка

#zip(), активно используется в задачах перебора
# данных и объединения данных из нескольких
#коллекций в один набор.

#у нас есть два списка: список логинов и
#паролей пользователей. И нам необходимо вывести
#их в формате «логин — пароль», т. е. одним
#циклом пройтись по двум спискам.

##userLogs = ['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']
##userPass = ['111', 'abc', '2345', '45fg', 'dffdg']
##for log, passw in zip(userLogs, userPass):
##    print(f'login: {log} — password: {passw}')

##userLogs = ['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']
##userPass = ['111', 'abc', '2345', '45fg', 'dffdg']
##for i in range(len(userLogs)):
##    print(f'login: {userLogs[i]} — password: {userPass[i]}')
##

#Функция zip() принимает итерируемые коллекции в
#качестве аргументов и возвращает итератор. Этот
#итератор генерирует серию кортежей, которые
#содержат элементы из каждого объекта-аргумента
#функции zip().
#   zip([iterator1, iterator2,.. iteratorN])
#Функция zip() может не содержать ни одного
#итератора, один или несколько.

list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e']
print(zip(list1, list2))
print(type(zip(list1, list2)))
print(list(zip(list1, list2)))


# map() - функция высшего порядка

# Задача 1
#Нам нужно перевести каждый логин из списка в
#нижний регистр
# на входе - userLogs =
#['Admin', 'STUDENT', 'teacheR', 'User']
# на выходе - userLogs =
#['admin', 'student', 'teacher', 'user']

# Стандартный вариант
##userLogs = ['Admin', 'STUDENT', 'teacheR', 'User']
##userLogsLow = []
##print(userLogs)
##for userLog in userLogs:
##    userLogsLow.append(userLog.lower())
##print(userLogsLow)

# Через функцию высшего порядка map()
##userLogs = ['Admin', 'STUDENT', 'teacheR', 'User']
###userLogsLow = []
##print(userLogs)
##userLogsLow = list(map(str.lower, userLogs))
##print(userLogsLow)

# Задача 2
#Пусть у нас есть список числовых значений в
#формате строк (например, полученный от
#пользователя с помощью функции input()).
#Необходимо получить получить список не целых чисел. 
myValues = ['2.3', '12', '45.67', '-3'] # список с str
print(myValues)
myNumbers = list(map(float, myValues))
#myNumbers = list(map(int, myValues))
print(myNumbers) # [2.3, 12.0, 45.67, -3.0]




# filter() - функция высшего порядка

#Функция filter() принимает два аргумента:
#функцию, которая реализует (описывает) условие
#фильтрации и возвращает логические значения
#(true или false), и итерируемый объект, каждый
#элемент которого будет проверяться условием
#фильтра. Если в результате такой проверки
#элемента функция-проверка вернет true,
#то он будет включен в результат работы фильтра.

# Задание 1
# у нас есть список с ценами на товары.
# Допустим, что нужно выбрать цены, значения
# которых больше 10 долларов.

prices = [100.45, 8.56, 5, 234, 45, 87, 567]
expensive = list(filter(lambda x: x >= 10, prices))
print(expensive) #[100.45, 234, 45, 87, 567]


#нам нужно выбрать такие логины пользователей,
#которые содержат слово «user». Проверку на
#наличие слова «user» в логине реализуем с помощью
#отдельной функции checkLog(user)

userLogs=['123user45', 'USERstudent', '56use3', 'user-23', 'adminUs']

def checkLog(user):
    if user.lower().find('user') != -1:
        return True
    else:
        return False

selectedUser = list(filter(checkLog, userLogs))
print(selectedUser) # ['123user45', 'USERstudent', 'user-23']

