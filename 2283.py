# 2283. 判断一个数的数字计数是否等于数位的值

import collections


class Solution:
    def digitCount(self, num):
        # collections.Counter() 同为 defaultdict(int)类型
        # 无需判断是否在 dict() 中
        cnt = collections.Counter(num)
        for i,k in enumerate(num):
            if (int(k) != cnt[str(i)]):
                return False
        return True
