# def - function

# 1 - write funtion in the beginning of the programm (after import)
# 2 - use a command def name_of_the_function():
# 3 - name_of_the_fundtion- Latin!! word1_word2
# 4 - after function seperate code with 2 blank lines
# 5 - call in the progran by name word1_word2()

# 1st option of function

##def test():
##   print('text')
##
##test()


##
##def add_two():
##    result = 2 + 2
##    print(result)
##
##
##print('*')
##add_two()
##print('***')
##add_two()


# 2nd option of function with arguments

##def add_numbers(num1, num2):
##    print(num1 + num2)
##
##
##number1 = int(input('1 number - '))
##number2 = int(input('2 number - '))
##add_numbers(number1, number2)
##print('***')


# 3rd option of function with arguments with return of the work in the main program


##def proc_depozit(summa, procent, termin):
##    money = summa * (procent/100) * termin
##    return money
##
###main prog
##
##money_in = int(input('Enter money - '))
##proc_dep = int(input('Enter % deposit - '))
##chas = int(input('Enter termin - '))
##
##print('****')
##money_out = proc_depozit(money_in,proc_dep,chas)
##print(f'Money out {money_out}')
##print('****')


##def add_numbers(num1, num2):
##    result = num1 + num2
##    print(result)
##    if result > 0:
##        return 'positive'
##    elif result < 0:
##        return 'negative'
##    elif result == 0:
##        return'zero'
##    
##
##
##number1 = int(input('1 number - '))
##number2 = int(input('2 number - '))
##text = add_numbers(number1, number2)
##print(f'Sum is {text}')


##def steve():
##    text = '"Don\'t let the noise of others\' opinions \n\
## drown out your own inner voice."\n \
##                    Steve Jobs'
##    print(text)
##
##steve()

def odd_number(num1, num2):
    if num1 < num2:
        for number in range(num1, num2 + 1, 2):
            print(number)
    else:
        for number in range(num1, num2 + 1, -2):
            print(number)
    


number1 = int(input('Enter a number 1 - '))
number2 = int(input('Enter a number 2 - '))
odd_number(number1, number2)





















































































