# практика ))))

# Задачка 1
# Имеем количество пар по 1час 20минут
# а также количество пар по 1 часу
# Необходимо посчитать разницу времени между ними

##def delta_time(num1, num2):
##    time_plan = 80 * num1 # время в минутах
##    time_real = 60 * num2 # время в минутах
##    delta = time_plan - time_real
##    if delta > 0:
##        print(f'В запасе есть {delta} минут')
##    elif delta < 0:
##        print(f'Мы перебрали {abs(delta)} минут')
##    else:
##        print(f'Идем по плану ))')
##
##while True:
##    # Menu
##    print('Выберите вариант действий:')
##    print('1 - для ввода данных')
##    print('2 - для выхода из программы')
##    answer = int(input('Введите свой выбор - '))
##    if answer == 1:
##        lesson_plan = int(input('Введите количество пар за планом - '))
##        lesson_real = int(input('Введите количество пар проведенных - '))
##        delta_time(lesson_plan, lesson_real)
##    elif answer == 2:
##        print('До свидания')
##        break
##    else:
##        print('Слабо ввести 1 или 2???')
   
# Задачка 2
##Напишите функцию averageValue(), которая
##принимает на вход список целых неотрицательных
##чисел. 
##Эта функция должна вернуть среднее значение
##четных чисел из данного списка, которые ещё
##при этом делятся на 3. Это значение должно
##быть округлено вниз до ближайшего целого значения.
##Если в списке нет значений, которые бы
##удовлетворяли этим условиям, функция должна
##вернуть 0.
##Примеры работы данной функции:
##averageValue([1,3,6,10,12,15]) --> 9
##averageValue([1,2,4,7,10]) --> 0

##def averageValue(args):
##    new_list = []
##    # 1 шаг
##    # 1 var через for
##    #for i in args:
##    #    if i % 2 == 0 and i % 3 == 0:
##    #        new_list.append(i)
##    # 2 var
##    tempa = lambda x: True if x % 2 == 0 and x % 3 == 0 else False
##    new_list = list(filter(tempa, args))
##    # 2 шаг
##    # 1 var
##    if bool(new_list):
##        average = int(round(sum(new_list) / len(new_list), 0))
##        return average
##    else:
##        return 0
##    # 2 var
##    #average = int(round(sum(new_list)/len(new_list), 0)) if bool(new_list) == True else 0
##    #return average
##
##
##my_list = [1, 3, 6, 10, 12, 15]
###my_list = [1, 2, 4, 7, 10]
##print(averageValue(my_list))


# Задачка 3
#Напишите функцию, которая находила бы сумму
#элементов от 1 до N (включительно).
#Функция должна быть рекурсивной.

##def sum_numbers(n):
##    # 1 var - рекурсия
##    #return n + sum_numbers(n-1) if n else 0
##    # 2  var - без рекурсии
##    summa = 0
##    for i in range(1, n + 1):
##        summa += i
##    return summa
##
##print(sum_numbers(5))

# Задачка 4
##В предложение были добавлены лишние пробелы.
##Напишите функцию, которая будет принимать такое
##предложение и возвращать его же в исправленном
##виде. Все слова должны быть разделены одним
##пробелом, а в начале и конце предложения
##пробелов быть не должно.

def correct_spacing(text):
    # 1 var
    my_list = text.split(' ')
    my_clear_list = []
    for i in my_list:
        if bool(i) != True:
            continue
        else:
            my_clear_list.append(i)
    return ' '.join(my_clear_list)
    # 2 var
    return ' '.join(sentence.split())
        
print(correct_spacing("The film   starts       at      midnight. "))





