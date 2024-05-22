#Пользователь вводит с клавиатуры строку. Произве-
#дите поворот строк и полученный результат выведите
#на экран.
#
##result = ''
##result2 = ''
##answer = input('Enter text - ')
### 1 var - slice
##result = answer[::-1]
### 2 var - for
##for index in range(-1, -1 * (len(answer) + 1), -1):
##    result2 += answer[index]
##print(result)
##print(result2)

#Пользователь вводит с клавиатуры строку. Посчи-
#тайте количество букв, цифр в строке. Выведите оба
#количества на экран
##count_alpha = 0
##count_digit = 0
##answer = input('Enter text - ')
##for symbol in answer:
##    if symbol.isalpha():
##        count_alpha += 1
##    elif symbol.isdigit():
##        count_digit += 1
##print(f'Count alpha = {count_alpha}')
##print(f'Count digit = {count_digit}')
        
#Пользователь вводит с клавиатуры строку и символ
#для поиска. Посчитайте сколько раз в строке
#встречается искомый символ.
#Полученное число выведите на экран.
##answer = input('Enter text - ')
##symbol = input('Enter symbol - ')
### 1 var - .count()
##number = answer.count(symbol)
##print(f'Symbol {symbol} is {number} times')
### 2 var
##count_symbol = 0
##for letter in answer:
##    if letter == symbol:
##        count_symbol += 1
##print(f'Symbol {symbol} is {count_symbol} times')

#Пользователь вводит с клавиатуры строку и слово
#для поиска. Посчитайте сколько раз в строке встречается
#искомое слово. Полученное число выведите на экран
##answer = input('Enter text - ')
##word = input('Enter word - ')
### 1 var
##number = answer.count(word)
##print(f'Number {number}')
### 2 var
##text_list = answer.split(' ')
##count_word = 0
##for i in text_list:
##    if i == word:
##        count_word += 1
##print(f'Number {count_word}')        

#Есть некоторый текст. Реализуйте следующую функциональность:
#■ Изменить текст таким образом, чтобы каждое пред-
#ложение начиналось с большой буквы;
#■ Посчитайте сколько раз цифры встречаются в тексте;
#■ Посчитайте сколько раз знаки препинания встреча-
#ются в тексте;
#■ Посчитайте количество восклицательных знаков в
#тексте.

##text = 'есть некоторый текст.123 реализуйте следующую функциональность'
# p.1
##if text.count('.') == 0 or text.index('.') == len(text) - 1:
##    result = text.capitalize()
##elif text.count('.') > 0:
##    text_list = text.split('. ')
##    for index in range(len(text_list)):
##        tempa = text_list[index].capitalize() + '. '
##        text_list[index] = tempa
##    result = ''.join(text_list)
##print(result)

# p.2
# var 1.0
##number0 = text.count('0')
##number1 = text.count('1')
##number2 = text.count('2')
##number3 = text.count('3')
##number4 = text.count('4')
##number5 = text.count('5')
##number6 = text.count('6')
##number7 = text.count('7')
##number8 = text.count('8')
##number9 = text.count('9')
##result = number0 + number1 + number2 +....

# var 1.1
##count_number = 0
##for i in range(9):
##    count_number += text.count(str(i))
##print(f'Numbers = {count_number}')

# 2 var
##count_number = 0
##for symbol in text:
##    if symbol.isdigit():
##       count_number += 1
##print(f'Numbers = {count_number}')


# Пользователь с клавиатуры вводит элементы списка
#целых и некоторое число. Необходимо посчитать сколь-
#ко раз данное число присутствует в списке. Результат
#вывести на экран.
##answer = input('Введите числа через запятую - ').split(',')
##number = int(input('Введите число - '))
##
##count_number = 0
##for i in answer:
##    if int(i) == number:
##        count_number += 1
##print(f'Число {number} встречается {count_number} раз')
##

# Пользователь с клавиатуры вводит элементы списка
#целых. Необходимо посчитать сумму всех элементов
#и их среднеарифметическое. Результаты вывести на
#экран.
answer = input('Введите числа через запятую - ').split(',')
summa = 0
eq = 0
for number in answer:
    summa += int(number)
eq = summa / len(answer)
print(f'Сумма чисел равна {summa}')
print(f'Сред.ариф. равно {eq}')

