# 面试题 03.03. 堆盘子

class StackOfPlates:

    def __init__(self, cap):
        self.cap = cap
        self.all_stack = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if ((self.all_stack) and (len(self.all_stack[-1]) < self.cap)):
            self.all_stack[-1].append(val)
        else:
            self.all_stack.append([val])


    def pop(self):
        if not self.all_stack:
            return -1
        tmp = self.all_stack[-1].pop()
        if not self.all_stack[-1]:
            self.all_stack.pop()
        return tmp
            

    def popAt(self, index):
        if len(self.all_stack) < index+1:
            return -1
        tmp = self.all_stack[index].pop()
        if not self.all_stack[index]:
            self.all_stack.pop(index)
        return tmp


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
