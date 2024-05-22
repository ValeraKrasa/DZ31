# сортировка Шелла - сортування Шелла
#Алгоритм сортировки Шелла — это усовершенствованная
#версия сортировки вставками.

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






