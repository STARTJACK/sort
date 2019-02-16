'''
冒泡排序,
稳定排序, 数据相同的数据在排序前后顺序不变
时间复杂度: 最好O(n²), 最好O(n), 平均O(n²)
空间复杂度O(1), 因为属于原地排序，
交换次数最多 n(n-1)/2次, 最少0次,
满有序度: n(n-1)/2
逆序度 = 满有序度 - 有序度  = 实际交换次数
'''


# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# 短冒泡排序
def shortBubbleSort(alist):
    exchange = False
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchange = True
            # else:
            # 此处不写exchange = False
            # 只要有交换, 就继续遍历
            # 毫无交换, 才能说明是有序
        if not exchange:
            break



'''
插入排序
稳定排序, 数据相同的数据在排序前后顺序不变
时间复杂度: 最坏O(n²), 最好O(n), 平均O(n²)
空间复杂度: O(1), 因为属于原地排序
交换次数最多 n(n-1)/2次, 最少0次,
'''


def insertSort(alist):
    if len(alist) <= 1:
        return

    for index in range(1, len(alist)):
        position = index
        currentValue = alist[position]
        for i in range(index):
            if alist[position] < alist[position - 1]:
                alist[position] = alist[position - 1]
                position -= 1
            else:
                break
            alist[position] = currentValue


'''
选择排序
不稳定排序, 因为存在相同数据时，会因为交换位置而出现不稳定
时间复杂度, 最好最坏平均 均为O(n²)
空间复杂度O(1)
'''


def selectionSort(alist):
    for i in range(len(alist)):
        minIndex = i
        for j in range(i, len(alist)):
            if alist[j] < alist[minIndex]:
                minIndex = j
        alist[i], alist[minIndex] = alist[minIndex], alist[i]


def testSelectionSort(alist):
    for i in range(len(alist)-1):
        minIndex = i
        for j in range(i, len(alist)):
            if alist[j] < alist[minIndex]:
                minIndex = j
        alist[minIndex], alist[i] = alist[i], alist[minIndex]





'''
归并排序，不稳定排序
时间复杂度：最好最坏平均O(nlogn)
空间复杂度：O(n)
'''


def mergeSort(alist):
    if len(alist) > 1 :
        mid = len(alist) // 2
        leftHalf, rightHalf = alist[:mid], alist[mid:]
        merge(alist, mergeSort(leftHalf), mergeSort(rightHalf))
    return alist


def merge(alist, leftHalf, rightHalf):
    i = j = k = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            alist[k] = leftHalf[i]
            i += 1
            k += 1
        else:
            alist[k] = rightHalf[j]
            j += 1
            k += 1
    while i < len(leftHalf):
        alist[k] = leftHalf[i]
        i += 1
        k += 1

    while j < len(rightHalf):
        alist[k] = rightHalf[j]
        j += 1
        k += 1


'''
快速排序，稳定排序
时间复杂度：最好O(nlogn), 最坏O(n²)
空间复杂度：O(1)
'''
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, low, high):
    if low < high:
        splitPoint = partition(alist, low, high)
        quickSortHelper(alist, low, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, high)


def partition(alist, low, high):
    privotvalue = alist[low]
    leftmark = low + 1
    rightmark = high
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= privotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= privotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[low], alist[rightmark] = alist[rightmark], alist[low]
    return rightmark




if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertSort(alist)
    print(alist)
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectionSort(alist)
    print(alist)
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)
