# 1898. 可移除字符的最大数目


from typing import List

### solution 4: 二分法 + 双指针 + 仅匹配 remove 后不匹配的字符
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np = len(s), len(p)
        n = len(removable)
        # 辅助函数，用来判断移除 k 个下标后 p 是否是 s_k 的子序列
        def check(k: int) -> bool:
            state = [True] * ns   # s 中每个字符的状态
            for i in range(k):
                state[removable[i]] = False
            # 匹配 s_k 与 p 
            j = 0
            for i in range(ns):
                # s[i] 未被删除且与 p[j] 相等时，匹配成功，增加 j
                if state[i] and s[i] == p[j]:
                    j += 1
                    if j == np:
                        return True
            return False
        
        # 二分查找
        l, r = 0, n + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1



### solution 3: 二分法 + 双指针， 超时了
# class Solution:
#     def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
#         def check(k):
#             j = 0
#             for i in range(m):
#                 if (not i in removable[:k]) and (s[i] == p[j]):
#                     j += 1
#                 if j == n:
#                     return True
#             return False
        
#         m = len(s)
#         n = len(p)
#         l = 0
#         r = len(removable)

#         while (l < r-1):
#             k = (l+r)//2
#             if check(k):
#                 l = k
#             else:
#                 r = k
        
#         if check(r):
#             return r
#         else:
#             return l


### solution 2: 记录 p 中每个 char 的 index 的 list，移除后，重新匹配子序列， 超时了
# def check_rem(s, p, cnt, rm):
#     ccnt = copy.deepcopy(cnt)
#     for r in rm:
#         if (s[r] in ccnt):
#             ccnt[s[r]].remove(r)
    
#     pre = -1
#     for c in p:
#         if not ccnt[c]:
#             return False
#         if ccnt[c]:
#             f = False
#             for ci in ccnt[c]:
#                 if ci > pre:
#                     f = True
#                     pre = ci
#                     break
#             if not f:
#                 return False
#     return True


# class Solution:
#     def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
#         # p 中的每个 char 在 s 中的 index 的 list
#         c_index = dict()
#         # 初始化 p 中的每个 char
#         for c in p:
#             c_index[c] = []
#         # 找到 char 在 s 中的 index 的 list
#         for i,c in enumerate(s):
#             if c in c_index:
#                 c_index[c].append(i)
        
#         l = 0
#         lf = check_rem(s, p, c_index, removable[:l+1])
#         if not lf:
#             return l

#         r = len(removable)-1
#         rf = check_rem(s, p, c_index, removable[:r+1])
#         if rf:
#             return r+1

#         mid = (l+r)//2
#         midf = False

#         while l < r-1:
#             mid = (l+r)//2
#             midf = check_rem(s, p, c_index, removable[:mid+1])
#             if midf:
#                 l = mid
#             else:
#                 r = mid

#         if r == mid:
#             mid -= 1
#         elif l == mid:
#             mid += 1
        
#         midf = check_rem(s, p, c_index, removable[:mid+1])
        
#         if midf:
#             return mid+1
#         else:
#             return mid





### solution 1: 双指针验证是否为子序列 + 替换移除字符 + 二分法遍历removable， 超时了
# def verify_sublist(x, y):
#     xn = len(x)
#     yn = len(y)
#     i = 0
#     j = 0
#     while True:
#         if (x[i] == y[j]):
#             j += 1
#         i += 1

#         if j == yn:
#             return True
#         if i == xn:
#             return False

# def rmove_k(x, rm):
#     tmp = x[:]
#     for r in rm:
#         tmp = tmp[:r] + '0' + tmp[r+1:]
    
#     return tmp

# class Solution:
#     def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:       
#         sn = len(s)
#         pn = len(p)
        
#         l = 0
#         l_s = rmove_k(s, removable[:1])
#         l_f = verify_sublist(l_s, p)

#         if not l_f:
#             return l

#         r = len(removable)-1
#         r_s = rmove_k(s, removable)
#         r_f = verify_sublist(r_s, p)

#         if r_f:
#             return r+1

#         mid = (l+r)//2
#         mid_s = str()
#         mid_f = False
#         while l < r - 1:

#             mid = (l+r)//2
#             mid_s = rmove_k(s, removable[:mid+1])
#             mid_f = verify_sublist(mid_s, p)

#             if mid_f:
#                 l = mid
#             else:
#                 r = mid



#         if r == mid:
#             mid -= 1
#             mid_s = rmove_k(s, removable[:mid+1])
#             mid_f = verify_sublist(mid_s, p)

#         elif l == mid:
#             mid += 1
#             mid_s = rmove_k(s, removable[:mid+1])
#             mid_f = verify_sublist(mid_s, p)
        
#         if mid_f:
#             return mid+1
#         else:
#             return mid
            
        

        
