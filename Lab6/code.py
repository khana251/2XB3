import timeit
import rbt
import math
import random


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def populate_tree(values, tree):
    for val in values:
        tree.insert(val)
        
def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


l = create_random_list(900)

# bst = rbt.BST()

rbt = rbt.RBTree()

# populate_tree(l, bst)

populate_tree(l, rbt)

print(rbt.get_height())

""" Code for comparing the average height difference between BST and RBT
avg = 0
for i in range(40):
    b = BST()
    r = RBTree()
    l = create_random_list(10000)
    populate_tree(l,b)
    populate_tree(l,r)
    avg += abs(b.get_height() - r.get_height())
    print(b.get_height(), r.get_height())
    
print(avg / 40)
"""

""" Code for comparing the heights of BST vs RBT for near sorted lists
avgb = 0
avgr = 0
i = 0.05
while i <= 1:
    for j in range(5):
        b = rbt.BST()
        r = rbt.RBTree()
        l = create_near_sorted_list(10000, i)
        populate_tree(l,b)
        populate_tree(l,r)
        avgb += b.get_height()
        avgr += r.get_height()
    print(round(i, 2), avgb / 5, avgr / 5)
    i += 0.05
    avgb = 0
    avgr = 0
"""
