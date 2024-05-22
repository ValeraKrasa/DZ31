#def2

#package of the arguments

##def sum_numbers(*args):
##    summa = 0
##
##
##    for number in args:
##        summa += number 
##    return summa
##
##
##print(f'Result = {sum_numbers(1, 2, 3, 4)}')
##print('*******')
##
###unpacking of the arguments
##
##numbers = [1, 2, 3, 4, 5, 6, 7]
##print(sum_numbers(*numbers))

# positioned and named arguments

##def plus(word1, word2): #positioned argument
##    print(word1, word2)
##
##
##
##plus('Hello', 'world')


##def plus(word1, word2): #named argument
##    print(word1, word2)
##
##
##
##plus(word2 = 'world', word1 = 'Hello')


## **kwargs - in the function will be used dictionary

#arguments by default

##def marka_car(firma, model, type_car = 'sedan'):
##    print(f'I have a car - {firma} {model}. It is {type_car}')
##
##
##marka_car('Honda', 'Acord')


# Visibility of the variable in the function. Rule LEGB

##def print_mas(eggs):
##    print(eggs)
##    eggs = 15 # Local memory
##    print(eggs)
##    return (eggs)
##
##
##eggs = 50 # Global memory
##print(print_mas(eggs))
##print(eggs) # ->

#How to amend Global with function

##def print_mas(num):
##    global eggs
##    eggs = 15 
##    print(eggs)
##
##
##
##eggs = 50 
##print(print_mas(eggs))
##print(eggs)


#nonlocal

##def print_mas1(word1):
##    print('Good day', word1)
##    print_mas2(word1)
##
##
##def print_mas2(word2):
##    print('hello', word2)
##
##
##
##print_mas1('Superman')

# rule LEGB
# - L - Local, E - Enclosing
# - G - Global, B - built-in

#Task1

##def summa_numbers(*args): # if * we will have a tuple
##    summa = 0
##    for number in args:
##        summa += number
##    print(f'Summa = {summa}')
##
##
##int_numbers = [1, 2, 3, 4, 5]
##summa_numbers(*int_numbers)

# Task2

##def find_number(number, *args):
##    for i in args:
##        if i == number:
##            print('True')
##        else:
##            print('False')
##
##
##
##numbers = [1, 2, 3, 4, 5, 6, 7, 8]
##find_number(15, *numbers)


# Task3

def new_numbers(*args):
    new_list = []
    for number in args:
        if number % 2 == 0 and number > 10:
            new_list.append(number)
    print(new_list)   


numbers = [5, 12, 3, 8, 16, 20, 4, 9, 10, 22]
new_numbers(*numbers)









































