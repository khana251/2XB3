class KHeap:
    
    k = 0
    length = 0
    data = []
    
    def __init__(self, values, k):
        self.k = k
        self.data = values
        self.length = len(values)
        self.build_heap(self.data)
        
    def build_heap(self, values):
        for i in range(self.length // self.k - 1, -1, -1):
            self.sink(i)
            
    def parent(self, i):
        return (i + (self.k - 1)) // self.k - 1
    
    def children(self, i):
        left = self.k * (i + 1) - (self.k - 1)
        right = self.k * (i + 1)
        return [i for i in range(left, right + 1)]
      
    def sink(self, i):
        largest_known = i
        for j in self.children(i):
            if j < self.length and self.data[j] > self.data[largest_known]:
                largest_known = j
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)
