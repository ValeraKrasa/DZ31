# dict

# for dictionary use a pare of key:value

##my_dict1 = {}
##my_dict2 = dict()
##print(type(my_dict1))
##print(type(my_dict2))
##
my_dict3 = {1:'Monday', 'day2':'Tue','day3':3,'day4':['Mon','Tue','Wed']}
##print(my_dict3)
##
##my_dict4 = dict(firstName='Jon', lastName='Smith')
##print(my_dict4)


# methods dict

# .get()

##name = my_dict3.get('day4')
##print(name)

# in False or True

#.key() -> return the keys

#print(my_dict3.keys())

# .values() - return all values
#print(my_dict3.values())

# .items() - return all pares

#print(my_dict3.items())

# .update

my_dict3.update({'day5':'Fri'})
print(my_dict3)

# del remove all dictionary
#my_dict3.del({'day5':'Fri'})
#print(my_dict3)

# .clear whole dictionary
#my_dict3.clear({'day5':'Fri'})
#print(my_dict3)

# .pop() - remove element by key
aaa = my_dict3.pop('day5')
print(aaa)



#for - iteration by key

for bbb in my_dict3:
    print(bbb)
    print(f'Value of the key {bbb} equals {my_dict3[bbb]}')

























