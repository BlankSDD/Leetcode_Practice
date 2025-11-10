# 面试题 03.02. 栈的最小值

import bisect

### solution 2: 1个栈 + 1个栈（存储每个元素存入时的最小值）
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.s_min = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if (not self.s_min) or (x <= self.s_min[-1]):
            self.s_min.append(x)

    def pop(self) -> None:
        tmp = self.s.pop()
        if (tmp == self.s_min[-1]):
            self.s_min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_min[-1]


### solution 1: 1个栈 + 1个sortedlist
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.s = []
#         self.sortStack = []

#     def push(self, x: int) -> None:
#         self.s.append(x)
#         self.sortStack.insert( bisect.bisect_left(self.sortStack, x), x )

#     def pop(self) -> None:
#         tmp = self.s.pop()
#         self.sortStack.remove(tmp)

#     def top(self) -> int:
#         return self.s[-1]

#     def getMin(self) -> int:
#         return self.sortStack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
