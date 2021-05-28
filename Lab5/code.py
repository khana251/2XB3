import timeit
import heap
import math
import random


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

def testmethod(n,method):
    totaltime = 0
    for i in range(10):
        L = create_random_list(n)
        start = timeit.default_timer()
        method(L)
        end = timeit.default_timer()
        totaltime+=end-start
        #print(timer)
    return totaltime/10

# for i in range(0,50000, 500):
#     print(i, testmethod(i,sorts.my_quicksort), testmethod(i,sorts.dual_pivot_quicksort),
#       testmethod(i,sorts.triple_pivot_quicksort), testmethod(i,sorts.quadra_pivot_quicksort))

#Timetest with near sorted list factor
def timetest(algo, runs, n, factor):
    total = 0
    if factor == 100:
        for _ in range(runs):
            L = create_random_list(n)
            start = timeit.default_timer()
            algo(L)
            end = timeit.default_timer()
            total += end - start
        # print("Next")
    else:
        for _ in range(runs):
            L = create_near_sorted_list(n, factor)
            start = timeit.default_timer()
            algo(L)
            end = timeit.default_timer()
            
            total += end - start
    return total/runs


# #Test bottom up mergesort vs regular mergesort
for i in range(0, 50000,1000):
    print(i, timetest(heap.Heap, 5, i,100), timetest(heap.Heap2, 5, i,100), timetest(heap.Heap4, 5, i, 100))

# for i in range(0, 1000,10):
#     print(i, timetest(heap.Heap, 5, i,100), timetest(heap.Heap2, 5, i,100), timetest(heap.Heap3, 5, i, 100))


# for i in range(1000, 50000,1000):
#     print(i, timetest(heap.Heap3, 10, i,100), timetest(heap.Heap4, 10, i, 100))

# for i in range(1, 10000, 10):
print(10, timetest(heap.Heap4, 5, 1000, 100))

#Used to test near sorted mergesort
# i = 0
# while i <= 0.5:
#     print(round(i, 2), timetest(sorts.mergesort_bottom, 10, 1000, round(i, 2)))
#     i += 0.05
