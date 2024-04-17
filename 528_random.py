import bisect
import random
from typing import List

# # 产生 1 到 3 的一个整数型随机数：  [1, 3] 左右都可取
# print( random.randint(1,3) )

# # 随机选取 0 到 3 间的偶数：        [0, 4] 左可取，右不可取
# print( random.randrange(0, 4, 2) )

# # 产生 0 到 1 之间的随机浮点数
# print( random.random() )

# # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print( random.uniform(1.1, 5.4) )

# # 从序列中随机选取一个元素
# print( random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()') )
# print( random.choice( [1, 2, 3, 4, 5, 6, 7, 8, 9]) )

# # 多个字符中生成指定数量的随机字符：
# print( random.sample('zyxwvutsrqponmlkjihgfedcba',5) )
# print( random.sample( [1, 2, 3, 4, 5, 6, 7, 8, 9], 3) )

# # 从a-zA-Z0-9生成指定数量的随机字符：
# ran_str = ''.join(random.sample(str.ascii_letters + str.digits, 8))
# print( ran_str )

# # 多个字符中选取指定数量的字符组成新字符串：
# print( ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)) )

# # 将序列a中的元素顺序打乱
# a=[1,3,5,6,7]
# print( random.shuffle(a) )

class Solution:

    def __init__(self, w: List[int]):
        # 提前生成 权重 的list, 插入生成的随机数
        # 例如： w = [2,3,4]
        # 则： w_w= [2, 5, 9]
        #      1,2       ->   index 0
        #      3,4,5     ->   index 1
        #      6,7,8,9   ->   index 2
        self.w_sum = sum(w)

        tmp = [w[0]]
        for i in w[1:]:
            tmp.append(tmp[-1] + i)
        self.w_w = tmp

    def pickIndex(self) -> int:
        ri = random.randint(1, self.w_sum)
        ind = bisect.bisect_left(self.w_w, ri)
        return ind




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
