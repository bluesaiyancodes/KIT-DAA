from insertionSort import insertSort

def mergeSort(arr, show=False):
    '''
    The show is for seeing the working of the Merge Sort, and serves no value to the sorting process.
    '''
    if show:
        print("mergeSort called, arr=", arr)
    returnedArr = arr
    if len(arr)>2:
        if show:
            print("startingRecurssion, arr=", arr)
        start = 0
        end = len(arr)
        mid = len(arr) // 2
        if show:
            print("start=",start,", end=",end,", mid=",mid)
        returnedArr = mergeSort(arr[start:mid])
        if show:
            print("returnedArr1=", returnedArr)
        returnedArr = returnedArr + mergeSort(arr[mid: end])
        if show:
            print("returnedArrMerged=", returnedArr)
    if show:
        print("Sorting happened")
    arr = insertSort(returnedArr)
    if show:
        print("returning back, arr=", arr)
    return arr




def exe():
    print("Merge Sort")
    arrString = input("Enter array of numbers to sort separated by space: ")
    arrSplit = arrString.split(" ")
    # Convertion of String type inputs into int
    for i in range(0, len(arrSplit)):
        arrSplit[i] = int(arrSplit[i])
    
    # Insertion Sort Call
    sortedArr = mergeSort(arrSplit)
    print("Sorted Array: ", sortedArr)

if __name__ == '__main__':
    exe()