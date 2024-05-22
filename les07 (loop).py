# Loop "for" - loop for exact amount of actions/iterations
#if you know how many time loop will work use "for".
#if you do not know how many times you will use loop, use "while"

# for loop works only with int number. float could be converted after

##for i in 1,2,3,4,5:
##    print(i,'=', i * '*')
##
##print('End')

#range(start, end, step)
#start, end, step only int!!!

##for i in range(10):
##    print(i,'=', i * '*')
##print('End')

#range() with 2 numbers

##for i in range(10,20):
##    print(i,'=', i * '*')
##print('End')

# range() with 3 numbers

for i in range(10, 20, 2):
    print(i,'=', i * '*')
print('End')


#range() negative-

##for i in range(20, 10, -2):
##    print(i,'=', i * '*')
##print('End')

# break and continue

##for i in range(50):
##    if i % 2 == 1:
##        continue
##    if i == 46:
##        print('Good bye')
##        break
##    print(i)
##print('End')

#for - else works like with while


##for i in range(50):
##    if i % 2 == 1:
##        continue
##    if i == 45: #-> change number to test else
##        print('Good bye')
##        break
##    print(i)
##else:
##    print('else works if break did not work')
##print('End')




#Task1

#for

##number = int(input('Enter a number - '))
##
##for i in range(1,10):
##    print(number, '*',i,'=',number * i)
##    

#while

##number1 = int(input('Enter a number - '))
##
##i = 1
##while i < 10:
##    print(number1, '*',i,'=',number1 * i)
##    i += 1

#Task1


##while True:
##    print('If you want to buy USD, enter - 1')
##    print('If you want to buy EUR, enter - 2')
##    print('If you want to buy exit, enter - x')
##    number = int(input('Enter a number')
##    if number == 'x' or number == 'X':
##                 print('Good bye')
##                 break
##    elif int(number) == 1:
##        print('Currency PLN to USD = 4,02')
##    elif int(number) == 2:
##        print('Currency PLN to EUR = 4,02')
##    else:
##        print('Currency PLN to $ = 4,02')

#Task2

##while True:
##    number1 = int(input('1e - '))
##    number2 = int(input('2e - '))
##    number3 = int(input('3e - '))
##    #answer = ''
##    if number1 < number3 > number2 or number1 > number3 < number2:
##        print('Number not in the range')
##    else:
##        for i in range(number1, number2 + 1):
##            if number3 == i:
##                print('!',i,'!',sep=' ',end= ' ')
##            else:
##                print(i, end=' ')
##        break

#Task3

import random
number_prog = random.randint(1, 10)
count = 0

while True:
    number_user = int(input('Enter a number - '))
    if number_user == 0:
        break
    elif number_user == number_prog:
        count += 1
        print('Gongratulation. You won. Atempts used - ',count)
    elif number_user > number_prog:
        count += 1
        print('My number less than yours')
    elif number_user < number_prog:
        count += 1
        print('My number bigger than yours')





























