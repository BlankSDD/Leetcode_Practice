# 2938. 区分黑球与白球

class Solution:
    def minimumSteps(self, s: str) -> int:
        ### solution 3: 一次遍历，记录前面 1 的个数，遇到 0 则 移动该 0 至所有 1 的左侧， 继续记录前面 1 的个数（因为该 0 被移到前面 1 的左侧了,所以需要继续增加）        ans = 0
        tmp = 0
        for i in s:
            if i == '1':
                tmp += 1
            else:
                ans += tmp
        return ans

        ### solution 2: 一次遍历，用 FIFO 队列记录 1 出现的位置
        # ans = 0
        # tmp = []
        # for i,cur in enumerate(s):
        #     if (cur == '1'):
        #         tmp.append(i)
        #     else:
        #         if tmp:
        #             ans += i - tmp.pop(0)
        #             tmp.append(i)
        # return ans


        ### solution 1: 找到 0 1 的数量， 加上前半段找 1 的 index， 减去后半段找 0 的 index，用时太久
        # ans = 0
        # n = len(s)
        # f = True
        # cnt = collections.Counter(s)
        # for i in range(cnt['0']):
        #     if (s[i] == '1'):
        #         f = False
        #         ans -= i

        # if f:
        #     return 0

        # for i in range(cnt['1']):
        #     ind = cnt['0']+i
        #     if (s[ind] == '0'):
        #         ans += ind

        # return ans
