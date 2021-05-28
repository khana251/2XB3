from graphs import *
import random

#Code for creating random graph of size k and with c connections
def created_random_graph(k, c):
    G = Graph(k)
    for _ in range(c):
        int1 = random.randint(0,k - 1)
        int2 = random.randint(0,k - 1)
        while int2 == int1:
            int2 = random.randint(0, k - 1)
        G.add_edge(int1, int2)
    return G


#Connected check
for i in range(400):
    true_count = 0
    for j in range(100):
        G = created_random_graph(100,i)
        if is_connected(G):
            true_count += 1
    print(i, true_count/100)

#Cycle Check
# for i in range(275):
#     true_count = 0
#     for j in range(1000):
#         G = created_random_graph(100,i)
#         if has_cycle(G):
#             true_count += 1
#     print(i, true_count/1000)

# G = Graph(7)
# # G.add_edge(0,3)
# # G.add_edge(1,2)
# G.add_edge(2,4)
# G.add_edge(4,6)
# G.add_edge(3,4)
# G.add_edge(1,3)
# G.add_edge(3,5)
# G.add_edge(4,5)

# G = Graph(9)
# G.add_edge(0,1)
# G.add_edge(0,2)
# G.add_edge(1,3)
# G.add_edge(1,4)
# G.add_edge(2,5)
# G.add_edge(2,6)
# G.add_edge(3,7)
# G.add_edge(3,8)
# G.add_edge(8,4)

# # G = Graph(10)
# # G.add_edge(0,0)
# # G.add_edge(1,2)
# # G.add_edge(1,4)
# # G.add_edge(4,3)
# # G.add_edge(2,7)
# # G.add_edge(7,8)
# # G.add_edge(8,3)
# # G.add_edge(3,6)
# # G.add_edge(7,9)
# # G.add_edge(9,5)

# # G = Graph(20)
# # G.add_edge(1, 2)
# # G.add_edge(2, 3)
# # G.add_edge(3, 4)
# # G.add_edge(1,12)
# # G.add_edge(4, 5)
# # G.add_edge(5, 6)
# # G.add_edge(6, 7)
# # G.add_edge(4, 6)
# # G.add_edge(2, 6)
# # G.add_edge(8, 9)
# # G.add_edge(10, 3)
# # G.add_edge(2, 3)



# print(has_cycle(G))
# print(is_connected(G))
