#Task Age

##age = int(input('Enter  age - '))
##
##if age < 4:
##    print('Price - 0')
##elif age < 18:
##    print('Price - 10')
##elif age < 60:
##    print('Price - 20')
##elif age > 60:
##    print('Price - 5')
##else:
##    print('Please enter a correct value')


#Task bus


##day = int(input('Enter a day - '))
##
##if day % 2 == 0:
##    print('Depart at 14:00')
##else:
##    print('Depart at 12:00')

#Task bus2
# 5 % 3 -> 0.6666 * 3 = 2
# 5 % 3 -> 5 - ((5//3)*3) = 2
# 1, 4, 7, 10.. 12:00
# 2, 5, 8, 11.. 13:00
# 3, 6, 9, 12.. 14:00

##day = int(input('Enter a day - '))
##
### if (day == 1 or day == 4 or day == 7 or
###      day == 10 or day ...
##
##if day % 3 == 1:
##    print('12:00')
##elif day % 3 == 2:
##    print('13:00')
##elif day % 3 == 0:
##    print('14:00')
##else:
##    print('Enter a correct value')

#Task bus3


##day = int(input('Enter a day - '))
##month = int(input('Enter a month - '))
##
##if (month == 1 or month == 3 or month == 5 or month == 7 or
##    month == 8 or month == 10 or month == 12):
##    if day > 31:
##        print('&&& ->')
##    else:
##        if day % 3 == 1:
##            print('12:00')
##        elif day % 3 == 2:
##            print('13:00')
##        elif day % 3 == 0:
##            print('14:00')
##    
##elif (month == 4 or month == 6 or month == 9 or month == 11):
##    if day > 30:
##            print('&&& ->')
##    else:
##        if day % 3 == 1:
##            print('12:00')
##        elif day % 3 == 2:
##            print('13:00')
##        elif day % 3 == 0:
##            print('14:00')
##
##elif month == 2:
##     if day > 29:
##        print('&&& ->')
##else:
##        if day % 3 == 1:
##            print('12:00')
##        elif day % 3 == 2:
##            print('13:00')
##        elif day % 3 == 0:
##            print('14:00')


#Task5
#age and gender
# 0 - 1 and male -> boy
# 15 >... and male -> man
# 0 - 15 and female -> girl
# 15... and female -> woman

age = int(input('Age - '))
gender = input('Gender (m/f) - ')


if gender == 'm' and age < 16:
    print('Boy')
elif gender == 'm' and age >= 16:
    print('Man')
elif gender == 'f' and age < 16:
    print('Girl')
elif gender == 'f' and age >= 16:
    print('Woman')
else:
    print('Correct gender')













 























