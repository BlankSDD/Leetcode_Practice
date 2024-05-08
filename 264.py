# 264. 丑数 II

uglyNum = [0, 1]
ul = 1
p2 = p3 = p5 = 1

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ### solution 1: 3指针 + 全局变量存储前面遍历过的记录 和 指针位置
        ###             看成3个数组，分别是能被2/3/5整除的递增数组，且每个数组的第一个数都为1
        
        global uglyNum, ul, p2, p3, p5

        for i in range(ul, n+1):
            n2, n3, n5 = uglyNum[p2]*2, uglyNum[p3]*3, uglyNum[p5]*5
            
            tmp = min( [n2, n3, n5] )
            uglyNum.append(tmp)
            ul += 1

            if tmp == n2:
                p2 += 1
            if tmp == n3:
                p3 += 1
            if tmp == n5:
                p5 += 1
        
        return uglyNum[n]
