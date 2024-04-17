# 705. 设计哈希集合

### 此为哈希表
class MyHashSet:

    def __init__(self):
        self.n = 1000
        self.mhs = [[] for _ in range(self.n)]

    def add(self, key):
        if self.contains(key):
            return
        
        idx = key % self.n
        self.mhs[idx].append(key)

    def remove(self, key):
        if not self.contains(key):
            return
        
        idx = key % self.n
        self.mhs[idx].remove(key)

    def contains(self, key):
        idx = key % self.n
        if any([key == each for each in self.mhs[idx]]):
            return True
        return False


### 下面是一个排序链表（二分法）
# class MyHashSet:

#     def __init__(self):
#         self.n = 0
#         self.mhs = []

#     def add(self, key):
#         if not self.mhs:
#             self.mhs.append(key)
#             self.n += 1
#         else:
#             ind, f = self.find_index(key)
#             if not f:
#                 self.mhs.insert(ind, key)
#                 self.n += 1

#     def remove(self, key):
#         ind, f = self.find_index(key)
#         if f:
#             self.mhs.pop(ind)
#             self.n -= 1

#     def contains(self, key):
#         ind, f = self.find_index(key)
#         return f
    
#     def find_index(self, key):
#         i = 0
#         j = self.n - 1
#         if (self.n == 0) or (key < self.mhs[i]):
#             return (0, False)
#         if (self.mhs[j] < key):
#             return (self.n, False)
        
#         while i < j-1:
#             m = (i+j)//2

#             if (self.mhs[m] < key):
#                 i = m
#             elif (key < self.mhs[m]):
#                 j = m
#             else:
#                 return (m, True)

#         if self.mhs[i] == key:
#             return (i, True)
#         if self.mhs[j] == key:
#             return (j, True)

#         return (i+1, False)
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
