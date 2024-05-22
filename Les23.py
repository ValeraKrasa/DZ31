#Exceptions
# construction try, except,else, finally, raise


##try:
##    number1 = int(input('Number 1 = '))
##    number2 = int(input('Number 2 = '))
##    result = number1 / number2
##    print(f'Result:{number1} / {number2} = {result}')
##
##except ZeroDivisionError:
##    print('Error - division by zero')
##except ValueError:
##    print('Error - invalid literal')
##
##else:
##    print('Programm was successful')


##import random
##
##def generate_list():
##
##    my_list = []
##
##    
##    try:
##        number = int(input('Enter number - '))
##        
##
##    except ValueError:
##        print('You should enter only number')
##        number = int(input('Enter number - '))
##        
##    finally:
##        for i in range(number):
##            my_list.append(random.randint(0,100))
##        return my_list
##    
##
##            
##
##if __name__ == '__main__':
##    print('Start')
##    my_super_list = generate_list()
##    print(my_super_list)





def calculator():

    result = 0


    try:
        operator = input('Enter mathematical action +, -, * or / - ')
        number1 = int(input('Enter a number 1 - '))
        number2 = int(input('Enter a number 2 - '))
                      
        if operator == '+':
             result = number1 + number2
             return result
    
        elif operator == '-':
             result = number1 + number2
             return result
    
        elif operator == '*':
             result = number1 * number2
             return result
    
        elif operator == '/':
             result = number1 / number2
        return result
    except ValueError:
        operator = input('Enter mathematical action +, -, * or / - ')
        number1 = int(input('Enter a number 1 - '))
        number2 = int(input('Enter a number 1 - '))
    except ZeroDivisionError:
        print(f'{number1} {operator} {number2} = 0')
      


if __name__ == '__main__':
    print('Start')
    res = calculator()
    print(res)














