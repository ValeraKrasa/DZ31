#Set

my_set1 = {'Mango', 'Ananas', 'Apple'}
##print(type(my_set1))
##print(my_set1)

#Set elements could be only
#int, float, str, tuple, set

##my_set2 = {'Mango', True, 1} # should be in output 1 and Mango
##
##print(my_set2)
##print(type(my_set2))

##my_set3 = set(('Hello', 'hello', 'world'))
##print(my_set3)

##my_set4 = {1, True, 'Mango'}
##
##print(my_set4)


##my_setA = {1, 2, 3}
##my_setB = {3, 2, 1}
##print(my_setA == my_setB) #-> True

##my_set6 = my_set1 + my_setA
##print(my_set6)

##for item in my_set1:
##    print(item)


##for i in range(len(my_set1)): # for with range does not work
##    print(my_set1[i])

# .add elements to the set

##my_set1.add('Orange')
####print(my_set1)
##
### .update() - adding tuples, lists, str...
##
##my_set1.update([1, 2, 3])
####print(my_set1)
##
### .discard() remove a specific element
##
####my_set1.discard('Orange')
####print(my_set1)
##
##my_set1.remove('Orange')
##print(my_set1)

# .clear() - clean all set

##my_set1.clear()
##print(my_set1)

# set works with the operators & | -
# & or method .intersection()

my_set7 = {1, 2, 3}
my_set8 = {2, 4, 6}
##
##my_set9 = my_set7 & my_set8
##print(my_set9) # shows only common elements

# | or method .union() - connection

##my_set10 = my_set7 | my_set8
##print(my_set10)

# - pr method .different()
##my_set11 = my_set7 - my_set8
##print(my_set11)

# functions enumerate(), len(), max(), min(), sorted(), sum()

ls = [10, 15, 20]
for i in enumerate(ls):
    print(i) #element of the index and content of the index
















































