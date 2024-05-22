#Loops
#while

##number = 0
##while number <= 5:
##    print(number)
##    number += 1 #number = number + 1 (+=, -=, *=, /=, **=, //=)
##print('Count is over')

#Task 2

##number = int(input('Enter a number - '))
##
##
##while number <= 15:
##    print(number)
##    number += 1 
##
##
##while number >= 15:
##    print(number)
##    number -= 1 
##print('Count is over')


#Task3

##number = int(input('Enter a number - '))
##
##if number >= 15:
##    while number >= 15:
##        print(number)
##        number -= 1 
##else:
##    while number <= 15:
##        print(number)
##        number += 1 
##print('Count is over')



#Task4

##piece = int(input('Amount of the cake pieces - '))
##
##while piece > 0:
##    print(piece, 'Yummy')
##    piece -= 1

#Task5

##number1 = int(input('1 number - '))
##number2 = int(input('2 number - '))
##
##tempa = number1
##while tempa <= number2:
##    print(tempa)
##    tempa += 1
##
##
##number1 = int(input('1 number - '))
##number2 = int(input('2 number - '))
##
##while number1 <= number2:
##    print(number1)
##    number1 += 1

#Task6


##number1 = int(input('1 number - '))
##number2 = int(input('2 number - '))
##
##if number1 < number2:
##    while number1 <= number2:
##        print(number1)
##        number1 += 1
##
##elif number1 > number2:
##     while number1 >= number2:
##        print(number1)
##        number1 -= 1
##else:
##    print(number)

#Task7

##number1 = int(input('1 number - '))
##number2 = int(input('2 number - '))
##
##if number1 < number2:
##
######    
######    if number1 % 2 == 1:
######         while number1 <= number2:
######             print(number1)
######             number1 += 2            <- not clean code, but understandable
######    else:
######        number1 +=1
######        while number1 <= number2:
######             print(number1)
######             number1 += 2
##   
##       if number1 % 2 == 0:
##         number1 += 1            
##       while number1 <= number2:
##           print(number1)
##           number1 += 2
##
##             
##elif number1 > number2:
##    if number2 % 2 == 0:
##         number2 += 1            
##    while number2 <= number1:
##           print(number2)
##           number2 += 2
##else:
##    if number1 % 2 == 1:
##        print(number1)

#Task8

# Endless loop
#True == True
##while True: #True == True
##    print('close')
    
   
#break and continue
##while True:
##     print('***')
##     answer = input('Enter s(stop) or c(continue)')
##     if answer == 's':
##         break
##print('End')


#while - else
##number = int(input('Enter number - '))
##while number < 50:
##    if number == 35:
##        break
##    print(number)
##    number += 1
##else:
##    print('***')
##print('End')


















































