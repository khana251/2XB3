from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    # Just marks all nodes in the adj list as unvisited
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

def BFS2(G, node1, node2):
    marked = {node1 : True}
    Q = deque([(node1,[node1])])
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node, path = Q.popleft()
        marked[current_node] = True
        for node in G.adj[current_node]:
            if node == node2:
                path.append(node)
                return path
            if not marked[node]:
                Q.append((node, path + [node]))
                marked[node] = True
        
    return path



#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Depth First Search
def DFS2(G, node1, node2):
    path = []
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()
        # print(current_node)
        path.append(current_node)
        slen = len(S)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    path.append(node)
                    return path
                elif not marked[node]:
                    S.append(node)
            if slen == len(S):
                path.remove(current_node)
                
    return path

def BFS3(G, node1):
    paths = {}
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    predecessor = node1
    counter = len(G.adj[node1])
    while len(Q) != 0:
        current_node = Q.popleft()
        #if counter == 0:
        predecessor = current_node
        for node in G.adj[current_node]:
            if not marked[node] == True:
                counter += 1
        for node in G.adj[current_node]:
            if not marked[node] == True:
                if counter > 0:
                    counter -= 1;
                    paths[node] = predecessor
                    Q.append(node)
                    marked[node] = True
    return paths

def DFS3(G, node1):
    paths = {}
    S = []
    for node in G.adj[node1]:
        S.append([node, node1])
    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node[0]]:
            marked[current_node[0]] = True
            paths[current_node[0]] = current_node[1]
            for node in G.adj[current_node[0]]:
                if marked[node] == False:
                    S.append([node, current_node[0]])
    return paths

def is_connected(G):
    for node in G.adj:
        if len(BFS3(G, node)) < (len(G.adj) - 1):
            return False
    return True

def has_cycle(G):
    for node in G.adj:
        dfs_connect = DFS3(G,node)
        if len(dfs_connect) > 1:
            last_key = list(DFS3(G,node))[-1]
            if G.are_connected(last_key, node):
                return True
    return False

def has_cycle2(G):
    for node in G.adj:
        paths = DFS3(G, node)
        for node2 in paths:
            if not paths[node2] == node:
                if node in G.adj[node2]:
                    return True
    return False

#Code for creating random graph of size k and with c connections
import random
def created_random_graph(k, c):
    G = Graph(k)
    for i in range(c):
        int1 = random.randint(0,k - 1)
        int2 = random.randint(0,k - 1)
        while int2 == int1:
            int2 = random.randint(0, k - 1)
        G.add_edge(int1, int2)
    return G
""" Check if has cycle
G = create_random_graph(100, 30)
print(G.adj) 
print(has_cycle(G))
"""
#Cycle Check
# for i in range(100):
#     true_count = 0
#     for j in range(1000):
#         G = created_random_graph(100,i)
#         if has_cycle2(G):
#             true_count += 1
#     print(i, true_count/1000)

#Connected check
for i in range(0,400):
    true_count = 0
    for j in range(100):
        G = created_random_graph(100,i)
        if is_connected(G):
            true_count += 1
    print(i, true_count/100)



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



print(has_cycle(G))
print(is_connected(G))




