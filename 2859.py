# 2859. 计算 K 置位下标对应元素的和

k_bin = [ [] for _ in range(11) ]
for i in range(1000):
    k_bin[bin(i).count('1')].append(i)

class Solution:
    def sumIndicesWithKSetBits(self, nums, k):
        ans = 0
        n = len(nums)
        for i in k_bin[k]:
            if i < n:
                ans += nums[i]
            else:
                break
        return ans
        
        # return sum( [[nums[i] if i < len(nums) else 0 for i in k_bin[k]] )
