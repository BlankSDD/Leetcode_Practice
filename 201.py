# 201. 数字范围按位与

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ### solution 2: 右移，将两个数字压缩为它们的公共前缀
        ###             将得到的公共前缀左移相同的操作数得到结果
        ### 思路理解2 ：只看最低位二进制位，只存在0,1两种情况，所以如果left<right，区间中必然存在left+1,那么最低位&一下一定等于0了，然后不停的右移，一直移到两个相等为止
        offset = 0
        
        while (left < right) and left:
            left = left >> 1
            right = right >> 1
            offset += 1

        # 左为 0， 右不为 0， 则 右 二进制数位长一些，直接为 0
        if not left:
            return 0

        return left << offset
        
        ### solution 1: 暴力遍历
        # ans = right
        # for i in range(left, right):
        #     ans &= i
        # return ans
