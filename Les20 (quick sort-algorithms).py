#quick sort algorithm

##def quick_sort(s):
##    if len(s) <= 1:
##        return s
##    elem = s[0]
##    left =list(filter(lambda x: x < elem , s))
##    center =[i for i in s if i == elem]
##    right =list(filter(lambda x: x > elem , s))
##
##    return quick_sort(left) + center + quick_sort(right)
##
##print(quick_sort([7,6,10,5,9,8,3,4]))




##a = [2, 1, 4, 5, 6,3 ,5,3 ,5 ,3]
##
##count = [0] * 6
##for i in a:
##    count[i] += 1
##print(count)
##for i in range(6):
##    if count[i] > 0:
##        print((str(i)+' ')*count[i],)


##def merge_two_list(a, b):
##    c = []
##    i = j = 0
##    while i < len(a) and j < len(b):
##        if a[i] < b[j]:
##            c.append(a[i])
##            i += 1
##        else:
##            c.append(b[j])
##            j+=1
##    if i < len(a):
##        c+= a[i:]
##    if i > len(a):
##        c+= a[:i]
##                                 
##
##
##
##def merge_sort(s):
##    if len(s == 1):
##          return s
##    middle = len(s) // 2
##    left = merge_sort(s[:middle])
##    right = merge_sort(s[middle:])
##    return merge_two_list(left,right)
##
##my_list = [0, 10, 15, 5, 10, 25]
##my_new_list = merge_sort(my_list)
##    
##print(my_list)
##print(my_new_list)



#DZ



def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
        print(c)
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left,right)


my_list = [100, 10, 15, 25, 55, 60, 10, 25]
middle = len(my_list) // 2
list1 = my_list[:middle]
list2 = my_list[middle:]
my_list_down = merge_sort(list1)
my_list_up = merge_sort(list2)

my_new_list = my_list_down[::-1] + my_list_up
print(my_list)
print(my_new_list)



def ShellSort(myList):
    subListN = len(myList) // 2
    step = 1
    while subListN > 0:
        for startInd in range(subListN):
            InsertionSort(myList, startInd, subListN)
        print(f'Interval={subListN}. After step {step}: {myList}')
        subListN = subListN // 2
        
def InsertionSort(myList, startInd, gapValue):
    for i in range(startInd + gapValue, len(myList), gapValue):
        currentElem = myList[i]
        currentInd = i
        while currentInd >= gapValue and myList[currentInd-gapValue] > currentElem:
            myList[currentInd] = myList[currentInd - gapValue]
            currentInd = currentInd - gapValue
            myList[currentInd] = currentElem
            
numbers=[33, 31, 40, 8, 12, 17, 25, 42]
print(f'Original list: {numbers}')
ShellSort(numbers)
print(f'Sorted list: {numbers}')













