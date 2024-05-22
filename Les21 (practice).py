
##def delta_time(num1, num2):
##    time_plan = num1 * 80
##    time_real = num2 * 60
##    delta = time_plan - time_real
##    if delta > 0:
##        print(f'Still pending {delta} minutes')
##    elif delta < 0:
##        print(f'Overused {delta * -1} minutes') # you can use {abs(delta)} to reduce -
##    else:
##        print(f'Used all required time')
##
##
##while True:
##    print('Choose an option of action:')
##    print('1 - Enter data')
##    print('2 - Exit')
##    answer = int(input('Enter your choice - '))
##    if answer == 1:
##        lesson_plan = int(input('Enter a number of the 80 minutes lessons'))
##        lesson_real = int(input('Enter a number of the 60 minutes lessons'))
##        delta_time(lesson_plan, lesson_real)
##    elif answer == 2:
##        print('Goodbye')
##        break
##    else:
##        print('Please enter 1 or 2')


##Напишите функцию averageValue(), которая принимает на вход список целых неотрицательных чисел. 
##
##Эта функция должна вернуть среднее значение четных чисел из данного списка, которые ещё при этом делятся на 3. Это значение должно быть округлено вниз до ближайшего целого значения. Если в списке нет значений, которые бы удовлетворяли этим условиям, функция должна вернуть 0.
##
##Примеры работы данной функции:
##
##averageValue([1,3,6,10,12,15]) --> 9
##averageValue([1,2,4,7,10]) --> 0


##def averageValue(args):
##    new_list = []
##    for i in args:
##        if i % 2 == 0 and i % 3 == 0:
##            new_list.append(i)
##    if bool(new_list):
##        average = int(round(sum(new_list) / len(new_list),0))
##        return average
##    else:
##        return
##
##        
##
##mylist = [1,3,6,10,12,15]
##print(averageValue(mylist))


    
