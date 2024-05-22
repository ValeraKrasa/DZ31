# сортировка слиянием - сортування злиттям

def MergeSort(myList):
    if len(myList) > 1:
        # Finding the middle of the list
        m = len(myList) // 2
        print(f'm: {m}')
        # Splitting a list into left and right parts
        leftPart = myList[:m]
        rightPart = myList[m:]
        print(f'left: {leftPart}')
        print(f'right: {rightPart}')
        # Sorting the left part
        MergeSort(leftPart)
        # Sorting the right part
        MergeSort(rightPart)
        #merge steps
        i = j = k = 0
        # Copy data to sorted list from leftPart-list and rightPart-list
        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] < rightPart[j]:
                myList[k] = leftPart[i]
                i += 1
            else:
                myList[k] = rightPart[j]
                j += 1
                k += 1
        # Checking if any element was left in leftPart-list
        while i < len(leftPart):
            myList[k] = leftPart[i]
            i += 1
            k += 1
        # Checking if any element was left in rightPart-list
        while j < len(rightPart):
            myList[k] = rightPart[j]
            j += 1
            k += 1
            
#print(f'temp merge: {myList}')
numbers = [35, 22, 41, 4, 10, 80, 11]
print(f'Original list: {numbers}')
MergeSort(numbers)
print(f'Sorted list: {numbers}')
