import timeit
import sorts
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
    else:
        for _ in range(runs):
            L = create_near_sorted_list(n, factor)
            start = timeit.default_timer()
            algo(L)
            end = timeit.default_timer()
            total += end - start
    return total/runs



testlist = create_random_list(8)
print(testlist)
sorts.quicksort_inplace(testlist)
print(testlist)



#Test in-place vs copy quicksort
# for i in range(0, 1490,10):
#     print(i, timetest(sorts.quicksort_inplace, 10, i), timetest(sorts.my_quicksort, 10, i))

#Compare average case to worst case quicksort
# for i in range(10, 1490, 10):
#     print(i, timetest(sorts.quicksort_inplace, 10, i,100), timetest(sorts.quicksort_inplace, 10, i, .01))

#Test quicksort alone
# for i in range(0, 2000, 10):
#     print(i, timetest(my_quicksort, 10, i, 100))

#Test for different values of the sort factor
# for i in range(0, 1000, 1):
#     print(i*.001, timetest(sorts.quicksort_inplace, 10, 1000, i*.001), timetest(selection_sort, 10, 1000, i*.001), timetest(sorts.bubble_sort_op1, 10, 1000, i*.001), timetest(sorts.insertion_sort, 10, 1000, i*.001))

#Test short lists sorting
# for i in range(0, 50):
#     print(i, timetest(sorts.quicksort_inplace, 100, i,100), timetest(selection_sort, 100, i,100), timetest(sorts.bubble_sort_op1, 100, i,100), timetest(sorts.insertion_sort, 100, i,100))

#Test quicksort2.0 vs quicksort
# for i in range(0, 50):
#      print(i, timetest(sorts.quicksort_inplace, 100, i, 100), timetest(sorts.insertion_sort, 100, i,100), timetest(sorts.quicksort_improved, 100, i,100))

#Quicksort 2.0 vs quicksort for near sorted lists
# for i in range(0, 1000, 1):
#      print(i*.001, timetest(sorts.quicksort_inplace, 10, 1000, i*.001), timetest(sorts.quicksort_improved, 10, 1000, i*.001), timetest(sorts.insertion_sort, 10, 1000, i*.001) )

#Testing whether quicksort can be improved by swapping to insertion for each recursive call
#With lengths <15
# for i in range(0, 1000, 10):
#     print(i, timetest(sorts.quicksort_improved, 10, i,100), timetest(sorts.quadra_pivot_quicksort, 10, i,100), timetest(sorts.quicksort_inplace, 10, i, 100))


#Testing four pivot QS vs improved inplace
# for i in range(0, 100,1):
#     print(i*.001, timetest(sorts.quicksort_improved, 10, 1000,i*.001), timetest(sorts.quadra_pivot_quicksort, 10, 1000,i*.001), timetest(sorts.quicksort_inplace, 10, 1000, i*.001))