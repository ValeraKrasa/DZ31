#Task1

##our_list = []
##
##n = int(input('Enter a number - '))
##
##for i in range(1, n + 1):
##    our_list.append(i)
##
##for index in range(0, n, 2):
##    print(f'The element with index {index} equal {our_list[index]}')


#Task2


    
##our_list = []
##
##n = int(input('Enter a number n - '))
##
##for i in range(1, n + 1):
##        our_list.append(i)
##
##for index in range(0, n):
##    if index % 2 != 0:
##        print(f'The element with index {index} equal {our_list[index]}')
##
##print('****************')
##
##for index2 in range(n - 1, -1, -1):
##    if index2 % 2 == 0:
##        print(f'The element with index {index2} equal {our_list[index2]}')


#Task3

##import random
##
##list_numbers = []
##list_even = []
##
##n = int(input('Enter a number - '))
##    
##for i in range(n):
##    list_numbers.append(random.randint(-10,10))
##    
##print(list_numbers)
##
##
##for index in range(len(list_numbers)):
##    if index % 2 == 0:
##        list_even.append(index)
##print(list_even)              
                
####for i in list_numbers:
####    if i % 2 == 0:
####        list_numbers_index = list_numbers.index(i)
####        list_even.append(list_numbers_index)
####print(list_even)



#Task4

##import random
##
##list_numbers = []
####
####for i in range (20):
####  number = random.randint(-10,10)
####    if number not in list_numbers:
####        list_numbers.append(number)
##
##while len(list_numbers) < 20:
##   number = random.randint(-10,10)
##   if number not in list_numbers:
##        list_numbers.append(number) 
##
##print(list_numbers)


#Task5


import random

victory = []


for i in range (20):
  victory.append(random.randint(0,50))
print(victory)

list_numbers_index = 0

for i in range (len(victory)):
    if victory[i] <= 3:
        print(f'Team No{i + 1} has less than 3 wins')














