# 374. 猜数字大小

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return -1 or 1 or 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while (l<=r):
            m = (l+r)//2

            if (-1 == guess(m)):
                r = m-1
            elif (1 == guess(m)):
                l = m+1
            else:
                return m


