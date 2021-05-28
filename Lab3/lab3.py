import random
import math
import timeit
import sys
sys.setrecursionlimit(1500)

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


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def timetest(algo, runs, n, factor):
    total = 0
    for _ in range(runs):
        L = create_near_sorted_list(n, factor)
        start = timeit.default_timer()
        algo(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def partition_improved(array, begin, end):
    pivotswap(array, begin,end)
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def pivotswap(array, begin,end):
    randpiv = random.randint(begin, end-1)
    array[begin], array[randpiv] = array[randpiv], array[begin]


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

def quicksort_improved(array, begin=0, end=None):
    if len(array) < 15:
        insertion_sort(array)
    else:
        if end is None:
            end = len(array) - 1
        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = partition_improved(array, begin, end)
            _quicksort(array, begin, pivot-1)
            _quicksort(array, pivot+1, end)
        return _quicksort(array, begin, end)

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

def bubble_sort_op1(L):
    for i in range(len(L)):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

testlist = create_random_list(8)
print(testlist)
quicksort_inplace(testlist)
print(testlist)



#Test in-place vs copy quicksort
# for i in range(0, 1490, 10):
#     print(i, timetest(quicksort_inplace, 10, i), timetest(my_quicksort, 10, i))

#Compare average case to worst case quicksort
# for i in range(10, 1490, 10):
#     print(i, timetest(quicksort_inplace, 10, i, 10), timetest(quicksort_inplace, 10, i, .01))

#Test quicksort alone
# for i in range(0, 2000, 10):
#     print(i, timetest(my_quicksort, 10, i))

#Test for different values of the sort factor
# for i in range(0, 1000, 1):
#     print(i*.001, timetest(quicksort_inplace, 10, 1000, i*.001), timetest(selection_sort, 10, 1000, i*.001), timetest(bubble_sort_op1, 10, 1000, i*.001), timetest(insertion_sort, 10, 1000, i*.001))

#Test short lists sorting
# for i in range(0, 50):
#     print(i, timetest(quicksort_inplace, 100, i, 10), timetest(selection_sort, 100, i, 10), timetest(bubble_sort_op1, 100, i, 10), timetest(insertion_sort, 100, i, 10))

#Test quicksort2.0 vs quicksort
# for i in range(0, 50):
#      print(i, timetest(quicksort_inplace, 100, i, 10), timetest(insertion_sort, 100, i, 10), timetest(quicksort_improved, 100, i, 10))

# for i in range(0, 1000, 1):
#      print(i*.001, timetest(quicksort_inplace, 10, 1000, i*.001), timetest(quicksort_improved, 10, 1000, i*.001), timetest(insertion_sort, 10, 1000, i*.001) )

for i in range(0, 1000, 10):
    print(i, timetest(quicksort_improved, 10, i, 10), timetest(quicksort_op3, 10, i, 10))
