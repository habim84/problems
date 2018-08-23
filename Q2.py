def min(arr):
    minVal, minIndex = arr[0], 0
    for i in range(1, len(arr)):
        minIndex, minVal = i if arr[i] < minVal else minIndex, arr[i] if arr[i] < minVal else minVal
    del arr[minIndex]
    return minVal

def sort(arr):
    newArr = [element for element in arr]
    sortedList = [min(newArr) for x in range(len(newArr))]
    return sortedList

theList = [100, 2, 5, 13, 29, 68, 87, 4, 17, 45, 54]
print("Unsorted: {0}\nSorted: {1}".format(theList, sort(theList)))
