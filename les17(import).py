# import

# import is important element in the connection of the other modules, libraries, etd.


# 1 option

##import random
##
##number = random.randint(10,50)
##print(number)


# 2 option (use of the different name)

##import random as rd
##
##number = rd.randint(10,50)
##print(number)

# 3 option

##from random import randint
##
##number3 = randint(10, 50)
##
##print(number3)

# 4 option

##from random import randint as ni
##
##number4 = ni(10,50)
##print(number4)


# option 5

#from randint import *


# Task

##import math
##
##def sqrt_number(num1):
##    result = math.sqrt(num1)
##    return result
##
##
##user_number = int(input('Enter number - '))
##number = sqrt_number(user_number)
##print(f'Result = {number:.2f}')



#how to install outside library
# 1 -find a library on
# 2 - in the console (cmd) insert pip install pyautogui
# 3 - use a library  in your project
# 

##import pyautogui
##pyautogui.write('Hello World', 0.5)
##pyautogui.move(600, 1000)

#for the control  of the module start or import we use a construction


##def main():
##    print('I start')
##
##def print_name(name):
##    print(f'Hello {name}')
##
##if "__main__" == __name__:
##    print('Launched Les17_def')
##    main()

##import Les17_def
##                
##
##Les17_def.print_name('Pavlo')

# Practice

# A)

##def print_start(num1):
##    for i in range(1, num1 + 1):
##        print('*' * i)
##
##
##if "__main__" == __name__:
##    number = int(input('Enter number - '))
##    print_start(number)



# B)

def print_start(num1):

    for i in range(1, num1 + 1):
        print('*' * i)
    for i in range(num1 - 1, 0, -1):
        print('*' * i)
    


if "__main__" == __name__:
    number = int(input('Enter number - '))
    print_start(number)



















































