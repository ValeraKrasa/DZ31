# быстрая сортировка - швидке сортування

def QuickSort(myList, firstInd, lastInd):
    global C
    global E
    i = firstInd
    j = lastInd
    # pivot element in the middle
    pivotElem = myList[firstInd + (lastInd — firstInd) // 2]
    while i <= j:
        while myList[i] < pivotElem:
            i += 1
            C += 1
        while myList[j] > pivotElem:
            j -= 1
            C += 1
        C += 1
        if i <= j: # swap
            E += 1
            myList[i], myList[j] = myList[j], myList[i]
            i += 1
            j -= 1
    if firstInd < j: # sort left part
        QuickSort(myList, firstInd, j)
    if i < lastInd: # sort right part
        QuickSort(myList, i, lastInd)
        
    print(f'C={C}, E={E}')
    return myList




    
