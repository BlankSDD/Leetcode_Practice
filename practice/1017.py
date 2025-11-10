# 1017. 负二进制转换

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        ans = []
        while n:
            res = n & 1
            ans.append(str(res))
            n -= res
            n //= -2
        return ''.join(ans[::-1])
