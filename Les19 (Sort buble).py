# сортировка пузырьком - сортування бульбашкою

def myBubbleSort_v1(myList):
    for i in range(len(myList) - 1):
        sortedFlag = True
        for j in range(len(myList) - i - 1):
            if myList[j] < myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
                sortedFlag = False
        print(sortedFlag)
        if sortedFlag:
            break


##def myBubbleSort(myList):
##    for i in range(len(myList) - 1):
##        for j in range(len(myList) - i - 1):
##            if myList[j] < myList[j + 1]:
##                temp = myList[j]
##                myList[j] = myList[j + 1]
##                myList[j + 1] = temp


def printList(myList):
    for index, elem in enumerate(myList):
        print(f'element {index+1}: {elem}')


#numbers = [5, 2, 4, 7, 6]
numbers = [7, 6, 5, 4, 2]

print('Original list:')
print(numbers)
#printList(numbers)
myBubbleSort_v1(numbers)
print('Sorted list:')
#printList(numbers)
print(numbers)

