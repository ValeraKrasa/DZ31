# lambda function


# function in one line

#lambda arg1, arg2... : .....

##def add10(x):
##     return x + 10
##
##number = add10(10)
##print(number)

##new_number = lambda x: x + 10
##print(new_number)


##numbers = [1, 2, 3, 4, 5]
##list_numbers = lambda x: x ** 2
##for number in numbers:
##    print(list_numbers(number))



##Напишите функцию, высчитывающую степень каждого
##элемента списка целых. Значение для степени передаётся
##в качестве параметра, список тоже передаётся в качестве
##параметра. Функция возвращает новый список, содержащий полученные результаты.


#var 1


##def stepen(number, *args):
##    tempa = []
##
##    for i in args:
##        tempa.append(i ** number)
##    return tempa
##
##
##
##
##numbers = [1, 2, 3, 4, 5]
##
##new_numbers = stepen(3, *numbers)
##print(new_numbers)


#var 2

numbers = [1, 2, 3, 4, 5]
stepen = 2
new_numbers = list(map(lambda x: x ** stepen, numbers))
print(new_numbers)




































































