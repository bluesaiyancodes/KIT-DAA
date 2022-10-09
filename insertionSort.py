def swap(arr, num1, num2):
    tmp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = tmp
    return arr

def insertSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j>=0 and arr[j]>arr[j+1]:
            arr = swap(arr, j+1, j)
            j-=1

    return arr


def exe(arrString = ""):
    print("Insertion Sort")
    if not len(arrString):
        arrString = input("Enter array of numbers with separated by space for sorting: ")
    arrSplit = arrString.split(" ")
    # Convertion of String type inputs into int
    for i in range(0, len(arrSplit)):
        arrSplit[i] = int(arrSplit[i])
    
    # Insertion Sort Call
    sortedArr = insertSort(arrSplit)
    print("Sorted Array: ", sortedArr)

def fileExe(fname):
    f = open(fname, 'r')
    arrString = f.read()
    exe(arrString[:-1])
    f.close()

if __name__ == '__main__':
    # File Execution
    fileExe("small_10.txt")
    # Manual Execution
    exe()
