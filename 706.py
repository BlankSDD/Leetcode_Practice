# 706. 设计哈希映射

class MyHashMap:

    def __init__(self):
        self.n = 1000
        self.mhs = [[] for _ in range(self.n)]

    def put(self, key, value):
        idx = key % self.n
        i,f = self.find_key(key)
        if not f:
            self.mhs[idx].append([key, value])
        else:
            self.mhs[idx][i][1] = value

    def get(self, key):
        idx = key % self.n
        i,f = self.find_key(key)
        if not f:
            return -1
        else:
            return self.mhs[idx][i][1]

    def remove(self, key):
        idx = key % self.n
        i,f = self.find_key(key)
        if f:
            self.mhs[idx].pop(i)

    def find_key(self, key):
        idx = key % self.n
        for i,[k,v] in enumerate(self.mhs[idx]):
            if key == k:
                return [i,True]
        return [-1,False]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
