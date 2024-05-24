# 1542. 找出最长的超赞子字符串

class Solution:
    def longestAwesome(self, s: str) -> int:
        ### solution 3: 状态压缩 + 哈希表
        ###             1. s[i:j] 中的 cnt = s[0:j]的cnt - s[0:i]的cnt
        ###                只用判断 s[0:j]的cnt 与 s[0:i]的cnt 的差别（即 异或操作）即可
        ###             2. s 中仅包含字符 0-9，可用长度为 10 的 list 计数
        ###                0 表示偶数次， 1 表示奇数次
        ###             3. 按位来表示 list : 0 0 0 0 0 0 0 0 0 0
        ###                        分别对应: 9 8 7 6 5 4 3 2 1 0
        ###                则，可以构成回文的只有 全0 或 只有一个 1 的时候
        ###                或，任意两个 [0:j]的 cnt 的异或为上述情况
        ###                即，作异或后为 (全0) 或 (仅差别一个 1)
        ###             4. 遍历记录奇偶
        ###                例如：当前为 3， 则把 1 左移 3 -> 100
        ###                      把 100 与上一个 进行 异或 （^=操作）
        ###                      则，第 3 位 应该为奇数， 即1
        
        
        # dict 记录 所有 s[0:j] 的奇偶情况 -> 最早出现的 index
        # 为什么用 int 而不是 list of index
        # 1. 只用记录 最早出现的 该种奇偶情况的 index即可，
        # 2. 后续再出现，直接减就好了，如果减 第二个index，必然没有 减第一个（最早的）index 大
        all_types = {0:-1}
        last_type = 0
        
        n = len(s)
        ans = 1
        
        for j in range(n):
            cur_digit = ord(s[j]) - ord('0')
            cur_type = last_type ^ (1 << cur_digit)

            # 出现了，则，可以有 作异或后为 (全0)
            if (cur_type in all_types):
                ans = max(ans, j-all_types[cur_type])
            # 没出现过，添加出现的最早 index
            else:
                all_types[cur_type] = j
            
            #  作异或后为 (仅差别一个 1), 先 异或这个 1，再查找
            for k in range(10):
                diff = cur_type ^ (1 << k)
                if (diff in all_types):
                    ans = max(ans, j-all_types[diff])

            # 更新上一个的奇偶情况
            last_type = cur_type

        return ans
        
        ### solution 2: 优化判断，记录当前子字符串中的每种字符格式
        # n = len(s)
        # ans = 1

        # for i in range(n-1):
        #     cnt = defaultdict(int)
        #     cnt[s[i]] += 1
        #     odd_num = 1

        #     for j in range(i+1, n):
        #         cnt[s[j]] += 1
                
        #         if (cnt[s[j]] % 2):
        #             odd_num += 1
        #         else:
        #             odd_num -= 1

        #         if (odd_num <= 1):
        #             ans = max(ans, j-i+1)

        # return ans


        ### solution 1: 双指针遍历 + 每次判断是否为回文
        # n = len(s)
        # ans = 1

        # for i in range(n-1):
        #     cnt = defaultdict(int)
        #     cnt[s[i]] += 1

        #     for j in range(i+1, n):
        #         cnt[s[j]] += 1
        #         f = 0
        #         for each in cnt.values():
        #             if (each%2):
        #                 f += 1
        #                 if f > 1:
        #                     break
        #         if (f == 0) or (f == 1):
        #             ans = max(ans, j-i+1)
        # return ans

