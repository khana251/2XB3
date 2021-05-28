#Bottom up merge sort
import random

def mergesort_bottom(L):
    n = len(L)
    #Base size for sorting, aka individual element
    i = 1
    while i < n:
        #Iterates across each i*2 block, and sorts the elements
        for j in range(0,n, i*2):
            mid = j + i
            end = j + i*2-1
            merge_bottom(L, j, mid, end)
        i = i*2



def merge_bottom(L, start, mid ,end):
    left = L[start:mid]
    ll = len(left)
    right = L[mid:end+1]
    rl = len(right)

    #Basic merge loops
    i, j = 0, 0
    while i < ll and j < rl:
        if right[j] < left[i]:
            L[start] = right[j]
            j += 1
        else:
            L[start] = left[i]
            i += 1
        start += 1

    while i < ll:
        L[start] = left[i]
        start += 1
        i += 1
    while j < rl:
        L[start] = right[j]
        start += 1
        j += 1

def mergesort_three(L):
    
    if len(L) <= 1:
        return 
    elif(len(L) == 2):
        if(L[0] > L[1]):
            L[0], L[1] = L[1], L[0]
        return
    midOne = len(L)//3
    midTwo = midOne * 2
    left = L[:midOne]
    middle = L[midOne:midTwo]
    right = L[midTwo:]
    
    #Mergesort core
    mergesort_three(left)
    mergesort_three(middle)
    mergesort_three(right)
    temp = merge_three(left, middle, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three(left, middle, right):
    L = []
    i = k = j = 0

    while i < len(left) or j < len(right) or k < len(middle):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            if j >= len(right):
                L.append(middle[k])
                k +=1
            elif k >= len(middle):
                L.append(right[j])
                j+=1
            else:
                if middle[k] <= right[j]:
                    L.append(middle[k])
                    k += 1
                else:
                    L.append(right[j])
                    j += 1
        elif j >= len(right):
            if i >= len(left):
                L.append(middle[k])
                k +=1
            elif k >= len(middle):
                L.append(left[i])
                i += 1
            else:
                if middle[k] <= left[i]:
                    L.append(middle[k])
                    k += 1
                else:
                    L.append(left[i])
                    i += 1
        elif k >= len(middle):
            if i >= len(left):
                L.append(right[j])
                j += 1
            elif j >= len(right):
                L.append(left[i])
                i += 1
            else:
                if right[j] <= left[i]:
                    L.append(right[j])
                    j += 1
                else:
                    L.append(left[i])
                    i += 1
        else:
            if left[i] <= right[j] and left[i] <= middle[k]:
                L.append(left[i])
                i += 1
            elif middle[k] <= left[i] and middle[k] <= right[j]:
                L.append(middle[k])
                k += 1
            else:
                L.append(right[j])
                j += 1
    return L
        
def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

# for j in range(0, 20):
#     t1 = []
#     for i in range(j):
#         t1.append(random.randint(0, 20))
#     # print(t1)
#     t2 = t1.copy()
#     t2.sort()
#     mergesort_bottom(t1)
#     print(t1==t2)
