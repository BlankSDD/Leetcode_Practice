# LCR 147. 最小栈
import bisect
import sortedcontainers
class MinStack:
    ### solution 2: list + sort list
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.sl = []
        # self.sl = sortedcontainers.SortedList()

    def push(self, x):
        self.s.append(x)
        i = bisect.bisect_left(self.sl, x)
        self.sl.insert(i, x)
        # self.sl = self.sl[:i] + [x] + self.sl[i:]

        # self.sl.add(x)

    def pop(self):
        tmp = self.s.pop()
        self.sl.remove(tmp)
        
    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.sl[0]


    ### solution 1: heap + list
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.h = []
    #     self.s = []

    # def push(self, x):
    #     heapq.heappush(self.h, x)
    #     self.s.append(x)

    # def pop(self):
    #     tmp = self.s.pop()
    #     self.h.remove(tmp)
    #     heapq.heapify(self.h)
        

    # def top(self):
    #     return self.s[-1]

    # def getMin(self):
    #     return heapq.nsmallest(1, self.h)[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
