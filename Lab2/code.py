import timeit
import random
import csv
import statistics

#code for copy method

def newList(n):
    l1 = []
    for i in range(n):
        l1.append(random.randint(0,10000))
    return l1

for i in range(300):
    l = newList(i*500)
    start = timeit.default_timer()
    l2=l.copy()
    end = timeit.default_timer()
    timer=end-start
    print(str(i*500) + " " + str(timer))


#code for Append memory transfer performance

l = []
for i in range(1000000):
    f = open("file2.txt", "a")
    start=timeit.default_timer()
    l.append(i)
    end=timeit.default_timer()
    timer = end - start
    if timer > 10**-4:
        f.write(str(i) + " " + str(timer) + "\n")

#code for general Append performance

l = []
for i in range(1000000):
    start=timeit.default_timer()
    l.append(i)
    end=timeit.default_timer()
    timer = end - start
    if i % 500 == 0:
        print(str(i) + " " + str(timer))

#Measure access time performance
def list_performance():
    res = list(range(1000000))
    times = []
    
    for i in range(0,1000000):
        start = timeit.default_timer()
        x = res[i]
        end = timeit.default_timer()
        timer = end-start
        #print(timer)
        times.append(timer)
    return times
    
#Takes average of multiple instances of list_performance
def average_l():
    average_times = []
    for j in range(10):
        average_times.append(list_performance())
    res = map(statistics.mean, zip(*average_times))
    with open("averagetest.csv", "w", newline='') as results:
        wr = csv.writer(results)
        for val in res:
            wr.writerow([val])
    