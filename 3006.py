# 3006. 找出数组中的美丽下标 I

from typing import List


# 问题：
# 想在 destination 目标字符串（长） 中匹配 想找到的 pattern 模式串（短）
# 在 destination 中 找到 pattern 出现的 index

#####################################################
############### kmp 算法： 字符比较算法 ###############
#####################################################

# kmp:
# 在 pattern 模式串 中如果有重复的 前缀
# 则：  在遍历 + 移动过程中，可以把 前缀重复出现 部分做上标记， 即 PMT 表
#       在下次移动的时候，可以根据 该 PMT 表快速移动，而不是 一位一位 的移动
# 每个模式串 (待匹配的)，都对应着一张PMT，比如"ababcabaa"对应的PMT如下：
# index:    0   1   2   3   4   5   6   7   8
#   p       a   b   a   b   c   a   b   a   a
#  PMT      0   0   1   2   0   1   2   3   1

def get_pmt(pattern):
    n = len(pattern)
    pmt = [0]*n

    i = 0
    for j in range(1, n):
        # 前缀匹配，则：i，j 向右移
        #     不匹配，则 i 回到 0, 重新开始匹配
        if pattern[i] == pattern[j]:
            pmt[j] = pmt[j-1] + 1
            i += 1
        else:
            i = 0
            if pattern[0] == pattern[j]:
                pmt[j] = 1
    
    return pmt

def kmp(destination, pattern):
    dn = len(destination)
    pn = len(pattern)
    pmt = get_pmt(pattern)

    ans = []

    i = 0
    j = 0
    while i < dn:
        print(i, j)
        if destination[i] == pattern[j]:
            i += 1
            j += 1
            if j == pn:
                ans.append(i-pn)
                j = pmt[-1]
        else:
            if j == 0:
                i += 1
            else:
                j = pmt[j-1]
    return ans

# d = 'ababcabaabababcabaabacaaaa'
# a = 'ababcabaa'

# print(get_pmt(a))
# print(kmp(d, a))


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ### solution 4: kmp 搜 a 和 b， 双指针遍历 a b 的结果
        i_all = kmp(s, a)
        j_all = kmp(s, b)

        if (not i_all) or (not j_all):
            return []

        i = 0
        j = 0

        ans = []
        while i < len(i_all):
            if (abs(i_all[i] - j_all[j]) <= k):
                ans.append(i_all[i])
                i += 1
            else:
                if (j < len(j_all)-1) and (j_all[j] < i_all[i]):
                    j += 1
                else:
                    i += 1
        return ans

        ### solution 3: kmp 搜 a + 遍历 + 搜寻其 k 距离内的 b（同样使用 kmp ）， 记住上一次找过的 lst_j， 下一次 最少要从 lst_j+1 开始找
        # sn = len(s)
        # an = len(a)
        # bn = len(b)

        # i_all = kmp(s, a)
        # b_pmt = get_pmt(b)

        # lst_ok_j = -1
        # lst_searched_j = -1

        # ans = []

        # for i in i_all:
            
        #     if (lst_ok_j >= 0) and (abs(i-lst_ok_j) <= k):
        #         ans.append(i)
        #         continue
            
        #     js = max( [0, lst_searched_j+1, i-k])
        #     jb = 0
        #     flag = False
        #     while js < min( sn, i+k+bn):
        #         if s[js] == b[jb]:
        #             js += 1
        #             jb += 1
        #             if jb == bn:
        #                 flag = True
        #                 break
        #         else:
        #             if jb == 0:
        #                 js += 1
        #             else:
        #                 jb = b_pmt[jb-1]

        #     if flag:
        #         ans.append(i)
        #         lst_ok_j = js-bn
        #         lst_searched_j = lst_ok_j
        #     else:
        #         lst_searched_j = js-bn

        # return ans


        ### solution 2: 暴力遍历 得到 a 所有 i， 再搜寻其 k 距离内的 b， 记住上一次找过的 lst_j， 下一次 最少要从 lst_j+1 开始找
        # sn = len(s)
        # an = len(a)
        # bn = len(b)

        # j_all = []
        # lst_j = -1

        # ans = []

        # for i in range(sn-an+1):
        #     if s[i:i+an] == a:

        #         if j_all and abs(i - j_all[-1]) <= k:
        #             ans.append(i)
        #             continue
                
        #         for j in range( max([0,i-k,lst_j+1]), min(i+k+1, sn-bn+1) ):
        #             if s[j:j+bn] == b:
        #                 ans.append(i)
        #                 j_all.append(j)
        #                 break

        #             lst_j = j

        # return ans


        ### solution 1: 暴力遍历，找到所有 a b 对应的 i j
        # sn = len(s)
        # an = len(a)
        # bn = len(b)
        # i_all = []
        # j_all = []
        # for i in range(sn-an+1):
        #     if s[i:i+an] == a:
        #         i_all.append(i)
        
        # for j in range(sn-bn+1):
        #     if s[j:j+bn] == b:
        #         j_all.append(j)

        # ans = []
        # for i in i_all:
        #     for j in j_all:
        #         if abs(j-i) <= k:
        #             ans.append(i)
        #             break
        
        # return ans
