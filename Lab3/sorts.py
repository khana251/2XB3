import random
import math

#Code for 2 pivot quicksort
def dual_pivot_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
    if(len(L) < 2):
        return L
    #Order the pivots
    if(L[0] < L[1]):
        pivot1 = L[0]
        pivot2 = L[1]
    else:
        pivot1 = L[1]
        pivot2 = L[0]
    #Continue sorting
    left, middle, right = [], [], []
    for num in L[2:]:
        if num < pivot1:
            left.append(num)
        elif num < pivot2:
            middle.append(num)
        else:
            right.append(num)
    return dual_quicksort_copy(left) + [pivot1] + dual_quicksort_copy(middle) + [pivot2] + dual_quicksort_copy(right)

#Code for 3 pivot quicksort_copy
def triple_pivot_quicksort(L):
    copy = triple_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def triple_quicksort_copy(L):
    if (len(L) < 2):
        return L
    #Return sorted list when there are only two elements
    if(len(L) == 2):
        if(L[0] < L[1]):
            return L
        else:
            return [L[1], L[0]]
    #Order the 3 pivots
    pivot1 = 0
    pivot2 = 0
    pivots = []
    if(L[0] < L[1]):
        pivot1 = L[0]
        pivot2 = L[1]
    else:
        pivot1 = L[1]
        pivot2 = L[0]
    if(L[2] < pivot1):
        pivots = [L[2],pivot1,pivot2]
    elif(L[2] < pivot2):
        pivots = [pivot1,L[2],pivot2]
    else:
        pivots = [pivot1,pivot2,L[2]]
    #Continue sorting
    left, middle1, middle2, right = [], [], [], []
    for num in L[3:]:
        if num < pivots[0]:
            left.append(num)
        elif num < pivots[1]:
            middle1.append(num)
        elif num < pivots[2]:
            middle2.append(num)
        else:
            right.append(num)
    return (triple_quicksort_copy(left) + [pivots[0]] + triple_quicksort_copy(middle1) + [pivots[1]] +
            triple_quicksort_copy(middle2) + [pivots[2]] + triple_quicksort_copy(right))

# Code for 4 pivots
def quadra_pivot_quicksort(L):
    copy = quadra_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def quadra_quicksort_copy(L):
    #If length of list is less than 4, can't be seperated into 4 pivots
    if(len(L) < 2):
        return L
    #If list is of length 2 or 3, sort the list.
    elif(len(L) == 2):
        if(L[0] < L[1]):
            return L
        else:
            return [L[1], L[0]]
    elif(len(L) == 3):
        order1 = 0
        order2 = 0
        if(L[0] < L[1]):
            order1 = L[0]
            order2 = L[1]
        else:
            order1 = L[1]
            order2 = L[0]
        if(L[2] < order1):
            return [L[2],order1,order2]
        elif(L[2] < order2):
            return [order1,L[2],order2]
        else:
            return [order1,order2,L[2]]

    #Ordering the pivots
    firstSmall, firstBig, secondSmall, secondBig = 0, 0, 0, 0
    pivot1, pivot2, pivot3, pivot4 = 0, 0, 0, 0
    if (L[0] > L[1]):
        firstSmall = L[1]
        firstBig = L[0]
    else:
        firstSmall = L[0]
        firstBig = L[1]
    if (L[2] > L[3]):
        secondSmall = L[3]
        secondBig = L[2]
    else:
        secondSmall = L[2]
        secondBig = L[3]

    if (firstSmall > secondSmall):
        pivot1 = secondSmall
        pivot2 = firstSmall
    else:
        pivot1 = firstSmall
        pivot2 = secondSmall
    if (firstBig > secondBig):
        pivot3 = secondBig
        pivot4 = firstBig
    else:
        pivot3 = firstBig
        pivot4 = secondBig
    if (pivot2 > pivot3):
        temp = pivot3
        pivot3 = pivot2
        pivot2 = temp

    #Continue Sorting
    left, middle1, middle2, middle3, right = [], [], [], [], []
    for num in L[4:]:
        if num < pivot1:
            left.append(num)
        elif num < pivot2:
            middle1.append(num)
        elif num < pivot3:
            middle2.append(num)
        elif num < pivot4:
            middle3.append(num)
        else:
            right.append(num)
    return (quadra_quicksort_copy(left) + [pivot1] + quadra_quicksort_copy(middle1) + [pivot2] +
            quadra_quicksort_copy(middle2) + [pivot3] + quadra_quicksort_copy(middle3) +
            [pivot4] + quadra_quicksort_copy(right))

# Optimized Quicksort, includes random pivots to avoid worst case where
# nearly sorted, as well as using insertion sort on pivot splits of size
# less than 16.
def quadra_pivot_quicksort_opt(L):
    copy = quadra_quicksort_copy_opt(L)
    for i in range(len(L)):
        L[i] = copy[i]

def quadra_quicksort_copy_opt(L):
    #If length of list is less than 16 and greater than 1, perform insertion sort.
    if(len(L) < 2):
        return L
    elif(len(L) < 16):
        insertion_sort(L)
        return(L)

    #Randomize the 4 pivots, and order them.
    pivot1, pivot2, pivot3, pivot4 = 0, 0, 0, 0
    pivot4 = random.randint(3, len(L) - 1)
    pivot3 = random.randint(2, pivot4 - 1)
    pivot2 = random.randint(1, pivot3 - 1)
    pivot1 = random.randint(0, pivot2 - 1)
    pivot4 = L[pivot4]
    pivot3 = L[pivot3]
    pivot2 = L[pivot2]
    pivot1 = L[pivot1]

    #Continue sorting
    left, middle1, middle2, middle3, right = [], [], [], [], []
    for num in L[4:]:
        if num < pivot1:
            left.append(num)
        elif num < pivot2:
            middle1.append(num)
        elif num < pivot3:
            middle2.append(num)
        elif num < pivot4:
            middle3.append(num)
        else:
            right.append(num)
    return (quadra_quicksort_copy_opt(left) + [pivot1] + quadra_quicksort_copy_opt(middle1) + [pivot2] +
            quadra_quicksort_copy_opt(middle2) + [pivot3] + quadra_quicksort_copy_opt(middle3) +
            [pivot4] + quadra_quicksort_copy_opt(right))

#Bubble sort from lecture
def bubble_sort_op1(L):
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

#Selection sort from lecture
def selection_sort(L):
    for i in range(len(L)):
        minindex = find_min_index(L,i)
        L[i], L[minindex] = L[minindex], L[i]

def find_min_index(L, n):
    mindex = n
    for i in range(n, len(L)):
        if L[i] < L[mindex]:
            mindex = i
    return mindex

#Insertion sort from lecture
def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L, i)

def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            L[i], L[i-1] = L[i-1], L[i]
        else:
            return
        i -= 1

#Partion function courtesy of stackoverflow as my implementation was somehow n^2
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

#Improved partition which implements a pivotswap to select random pivot
def partition_improved(array, begin, end):
    pivotswap(array, begin,end)
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

#Swaps the begin element with a random to ensure random pivot element, aided from stackoverflow
def pivotswap(array, begin,end):
    randpiv = random.randint(begin, end-1)
    array[begin], array[randpiv] = array[randpiv], array[begin]

#Quicksort without creating new lists
def quicksort_inplace(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

#Quicksort inplace with insertion sort for n<15, random pivot
def quicksort_improved(array, begin=0, end=None):
    # if len(array) < 15:
    #     insertion_sort(array)
    # else:
        if end is None:
            end = len(array) - 1
        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = partition_improved(array, begin, end)
            _quicksort(array, begin, pivot-1)
            _quicksort(array, pivot+1, end)
        return _quicksort(array, begin, end)

#Improved quicksort which further calls 
# insertion sort during the recursive calls for n<15
def quicksort_op3(array, begin=0, end=None):
    if len(array) < 15:
        insertion_sort(array)
    else:
        if end is None:
            end = len(array) - 1
        def _quicksort(array, begin, end):
            if len(array) < 15:
                insertion_sort(array)
            elif begin >= end:
                return
            else:
                pivot = partition_improved(array, begin, end)
                _quicksort(array, begin, pivot-1)
                _quicksort(array, pivot+1, end)
        return _quicksort(array, begin, end)

#Supplied quicksort which creates new subarrays
def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)
