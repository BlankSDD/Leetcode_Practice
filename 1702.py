# 1702. 修改后的最大二进制字符串

class Solution:
    def maximumBinaryString(self, binary):
        ### 00 -> 10
        ### 10 -> 01

        # 2 个 0 在一起，高位会变成 1
        # 最终答案会恰好包含一个 0
        # 只有一个 0 时只能左移不能右移

        ### solution 2: 直接构造 (简化solution 1的遍历)
        z1 = binary.find('0')
        if z1 < 0:
            return binary

        # 计算 0 的数量
        z2 = binary.count('0', z1+1)
        return (z1+z2) * '1' + '0' + (len(binary) - z1 - z2 - 1) * '1'


        ### solution 1: 遍历 + 让字符串只剩下一个 0
        # n = len(binary)
        # z1 = binary.find('0')
        # if z1 < 0:
        #     return binary

        # ans = binary[:z1]

        # for i in range(z1+1, n):
        #     if binary[i] == '0':
        #         ans += '1'

        # return ans + '0' + (n-len(ans)-1) * '1'
