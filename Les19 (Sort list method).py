# method .sort() for list
##cars0 = ['Ford', 'BMW', 'Volvo', 'volva']
##cars0.sort(reverse=True) # Z > A, z > a
##print(cars0) #['Volvo', 'Volva', 'Ford', 'BMW']

##cars0.sort() # без ключа сортировка A -> Z, a -> z
##print(cars0) # ['BMW', 'Ford', 'Volva', 'Volvo']

### A function that returns the length of the value:
##def myFunc(e):
##  return len(e)
##
##cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
##cars.sort(key=myFunc)
##print(cars)

### A function that returns the 'year' value:
##def myFunc(e):
##  return e['year']
##
##cars = [
##  {'car': 'Ford', 'year': 2005},
##  {'car': 'Mitsubishi', 'year': 2000},
##  {'car': 'BMW', 'year': 2019},
##  {'car': 'VW', 'year': 2011}
##]
##
##cars.sort(key=myFunc)
##print(cars)


# fun. sorted()
##a = ("b", "g", "a", "d", "f", "c", "h", "e")
##x = sorted(a)
##print(x)


### fun with key
##fruits = ['apple', 'banana', 'kiwi', 'pomegranate']
### sorts the list based on the length of each string
##sorted_fruits = sorted(fruits, key=len)
##print('Sorted list:', sorted_fruits)




