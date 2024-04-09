# 202. 快乐数

class Solution:
    def calNext(self, x):
        y = 0
        while x > 0:
            y += pow(x%10, 2)
            x //= 10
        return y

    def isHappy(self, n):
        ### solution 2: 快慢指针，判断是否循环
        s = n
        q = self.calNext(n)
        while (s != q):
            s = self.calNext(s)
            q = self.calNext(self.calNext(q))
            if (s == 1) or (q == 1):
                return True
        return (s == 1) or (q == 1)



        ### solution 1: 检查每一个计算出来的数字，判断是否循环
        # searched = set()
        # cur = n
        # while True:
        #     if cur == 1:
        #         return True
        #     if cur in searched:
        #         return False
        #     searched.add(cur)
        #     nxt = 0
        #     while cur > 0:
        #         nxt += pow(cur%10, 2)
        #         cur //= 10
        #     cur = nxt
        # return True
