
##################################################################################
##################################################################################
##################################################################################
# class UnionSet:
#     def __init__(self, n):
#         self.parent = {i:i for i in range(n)}
#         self.rank = {i:1 for i in range(n)}
#         self.groups = n
    
#     def find_root(self, x):
#         root = self.parent[x]
#         while root != self.parent[root]:
#             root = self.parent[root]
#         self.parent[x] = root
#         return root

#     def connect(self, x, y):
#         return self.find_root(x) == self.find_root(y)
    
#     def union(self, x, y):
#         x_root = self.find_root(x)
#         y_root = self.find_root(y)

#         if x_root != y_root:
#             self.groups -= 1

#             if self.rank[x_root] <= self.rank[y_root]:
#                 self.parent[x_root] = y_root
#                 self.rank[y_root] += self.rank[x_root]
#             else:
#                 self.parent[y_root] = x_root
#                 self.rank[x_root] += self.rank[y_root]
        
#         # if x_root != y_root:
#         #     self.parent[y_root] = x_root
#         #     self.rank[x_root] += self.rank[y_root]

# a = UnionSet(5)
# print(a.parent)

# 1. and 用于判断条件时，前面如果为False，后面不会运行，即使后面有逻辑错误
#    or 用于判断条件时，前面如果为True，后面不会运行，即使后面有逻辑错误
#    &,| 可用于bool值判断，也可用于逻辑与,或操作
#    &,| 用于bool判断时，前后都会运行判断
#    &,| 用于逻辑与,或操作时，运行优先级高于 ==
#        例如： a == 1 & b == 2
#        先运行 1 & b， 然后 a == 中间结果 == 2，形成一个连等判断
#
# 2. =赋值，copy浅拷贝，deepcopy深拷贝
#     =================================================
#    || 完全一样： for循环=赋值
#    || 浅拷贝，第一层： copy浅拷贝，列表生成式，切片[:]
#    || 深拷贝，所有嵌套list： copy.deepcopy()深拷贝
#     =================================================
#    for循环=赋值：两个列表是等价的，修改其中任何一个列表都会影响到另一个列表
#        例如：old = [1,[1,2,3],3]
#              new = []
#              for i in range(len(old)):
#                  new.append(old[i])
#    copy浅拷贝：原list中第一层，是实现了深拷贝，但对于其内嵌套的List，仍然是拷贝
#        例如：old = [1,[1,2,3],3]
#              new = old.copy()
#    列表生成式：浅拷贝方法，只对第一层实现深拷贝
#        例如：old = [1,[1,2,3],3]
#              new = [i for i in old]
#    切片[:]：浅拷贝方法，只对第一层实现深拷贝
#        例如：old = [1,[1,2,3],3]
#              new = old[:]
#    copy.deepcopy()深拷贝：无论多少层嵌套，无论怎样的形式，得到的新列表都是和原来无关的
#        例如：import copy
#              old = [1,[1,2,3],3]
#              new = copy.deepcopy(old)
#
# 3. pow()通过内置的方法直接调用，内置方法会把参数作为整型 int，而 math 模块则会把参数转换为 float
#    pow()可以输入 3 个参数，如果 z 存在则：
#    pow(x,y [, z]) = x**y % z
#
#
#
#    
##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################


##################################################################################
##################################################################################
##################################################################################
# def change(amount, coins):
#     ### solution 2: dp + 贪心 优化
#     if amount < 1:
#         return 1

#     dp = [0] * (amount+1)
#     dp[0] = 1
#     coins.sort()
    
#     if amount < coins[0]:
#         return 0

#     for coin in coins:
#         if coin > amount:
#             break
#         for i in range(coin, amount+1):
#             dp[i] += dp[i-coin]
    
#     return dp[-1]


#     ### solution 1: dp + 贪心
#     # if amount < 1:
#     #     return 1

#     # dp = [-1] * (amount+1)
#     # dp[0] = 1

#     # min_coin = min(coins)

#     # if amount < min_coin:
#     #     return 0
    
#     # for coin in coins:
#     #     for i in range(coin, amount + 1):
#     #         if dp[i] < 0:
#     #             if dp[i-coin] < 0:
#     #                 pass
#     #             else:
#     #                 dp[i] = dp[i-coin]
#     #         else:
#     #             if dp[i-coin] < 0:
#     #                 pass
#     #             else:
#     #                 dp[i] = dp[i] + dp[i-coin]
    
#     # if dp[amount] < 0:
#     #     return 0
#     # else:
#     #     return dp[amount]

# a = 5
# b = [1,2,5]
# print(f'==={change(a,b)}====')

##################################################################################
##################################################################################
##################################################################################
# def coinChange(coins, amount):
#     ### solution 3: dp + 贪心
#     dp = [float("inf")]*(amount+1)
#     dp[0] = 0
    
#     if amount == 0:
#         return 0

#     if (amount < min(coins)):
#         return -1

#     for coin in coins:
#         if (coin < amount):
#             dp[coin] = 1
#         elif (coin == amount):
#             return 1
    
#     for coin in coins:
#         for i in range(coin+1, amount+1): 
#             dp[i] = min(dp[i], dp[i-coin]+1)
    
#     print(dp)
#     if dp[amount] != float("inf"):
#         return dp[amount]
#     else:
#         return -1

# a = [2]
# b = 3
# print(f'==={coinChange(a,b)}===')


##################################################################################
##################################################################################
##################################################################################
# import copy
# from sortedcontainers import SortedList
# import heapq
# def minimumVisitedCells(grid):
#     ## solution 3: DP + heap
#     m = len(grid)
#     n = len(grid[0])
    
#     # 2个list: 每一个元素为 一个队列 [ (最少步数,  i或j), ...]， 队列中每一个元素为 (最少步数,  i或j)
#     heap_m = [[] for _ in range (m)]
#     heap_n = [[] for _ in range (n)]
#     dis = [ [-1]*(n) for i in range(m) ]
#     dis[0][0] = 1
#     for i in range(m):
#         for j in range(n):
#             print(f'aaaa=={i}=={heap_m}=={j}=={heap_n}===')

#             while (heap_m[i]) and (heap_m[i][0][1] + grid[i][heap_m[i][0][1]] < j):
#                 heapq.heappop(heap_m[i])
#             if heap_m[i]:
#                 if dis[i][j] == -1:
#                     dis[i][j] = dis[i][heap_m[i][0][1]] + 1
#                 else:
#                     dis[i][j] = min(dis[i][j], dis[i][heap_m[i][0][1]] + 1)
            
#             while (heap_n[j]) and (heap_n[j][0][1] + grid[heap_n[j][0][1]][j] < i):
#                 heapq.heappop(heap_n[j])
#             if heap_n[j]:
#                 if dis[i][j] == -1:
#                     dis[i][j] = dis[heap_n[j][0][1]][j] + 1
#                 else:
#                     dis[i][j] = min(dis[i][j], dis[heap_n[j][0][1]][j] + 1)
            
#             if dis[i][j] != -1:
#                 heapq.heappush(heap_m[i], (dis[i][j], j))
#                 heapq.heappush(heap_n[j], (dis[i][j], i))
            
#             print(f'bbbb=={i}=={heap_m}=={j}=={heap_n}===')

#     return dis[-1][-1]


#     # def update(x: int, y: int) -> int:
#     #     return y if x == -1 or y < x else x
    
#     # for i in range(m):
#     #     for j in range(n):
#     #         while row[i] and row[i][0][1] + grid[i][row[i][0][1]] < j:
#     #             heapq.heappop(row[i])
#     #         if row[i]:
#     #             dist[i][j] = update(dist[i][j], dist[i][row[i][0][1]] + 1)

#     #         while col[j] and col[j][0][1] + grid[col[j][0][1]][j] < i:
#     #             heapq.heappop(col[j])
#     #         if col[j]:
#     #             dist[i][j] = update(dist[i][j], dist[col[j][0][1]][j] + 1)

#     #         if dist[i][j] != -1:
#     #             heapq.heappush(row[i], (dist[i][j], j))
#     #             heapq.heappush(col[j], (dist[i][j], i))

#     # return dist[m - 1][n - 1]



#     ### solution 2: BFS + 距离优先排序
#     # m = len(grid)
#     # n = len(grid[0])

#     # if (m == 1) and (n == 1):
#     #     return 1

#     # # bfs
#     # possible_next = [[0,0,0]]
#     # tmp = SortedList([])
#     # ans = 1
#     # # searched = dict()
#     # while possible_next:
#     #     dis, cur_i,cur_j = possible_next.pop()
#     #     cur_v = grid[cur_i][cur_j]

#     #     print(f'aaaaaa==={cur_i}=={cur_j}=={tmp}======')

#     #     for i in range( min(cur_i+cur_v, m-1), cur_i, -1):
#     #         if (i == m-1) and (cur_j == n-1):
#     #             return ans+1
#     #         if grid[i][cur_j] > 0:
#     #             tmp.add([i-cur_i+grid[i][cur_j],i,cur_j])
#     #     for j in range( min(cur_j+cur_v, n-1), cur_j, -1):
#     #         if (cur_i == m-1) and (j == n-1):
#     #             return ans+1
#     #         if grid[cur_i][j] > 0:
#     #             tmp.add([j-cur_j+grid[cur_i][j],cur_i,j])
        
#     #     # searched.add([cur_i,cur_j])
#     #     grid[cur_i][cur_j] = -1

#     #     print(f'bbbbbb==={cur_i}=={cur_j}=={tmp}======')

#     #     if not possible_next:
#     #         possible_next = copy.deepcopy(tmp)
#     #         tmp = SortedList([])
#     #         ans += 1
    
#     # return -1

#     ### solution 1: BFS，先纵向添加，再横向，超时了
#     # m = len(grid)
#     # n = len(grid[0])

#     # if (m == 1) and (n == 1):
#     #     return 1

#     # # bfs
#     # possible_next = [[0,0]]
#     # tmp = []
#     # ans = 1
#     # # searched = dict()
#     # while possible_next:
#     #     cur_i,cur_j = possible_next.pop(0)
#     #     cur_v = grid[cur_i][cur_j]

#     #     print(f'aaaaaa==={cur_i}=={cur_j}=={tmp}======')

#     #     for i in range( min(cur_i+cur_v, m-1), cur_i, -1):
#     #         if (i == m-1) and (cur_j == n-1):
#     #             return ans+1
#     #         if grid[i][cur_j] > 0:
#     #             tmp.append([i,cur_j])
#     #     for j in range( min(cur_j+cur_v, n-1), cur_j, -1):
#     #         if (cur_i == m-1) and (j == n-1):
#     #             return ans+1
#     #         if grid[cur_i][j] > 0:
#     #             tmp.append([cur_i,j])
        
#     #     # searched.add([cur_i,cur_j])
#     #     grid[cur_i][cur_j] = -1

#     #     print(f'bbbbbb==={cur_i}=={cur_j}=={tmp}======')

#     #     if not possible_next:
#     #         possible_next = copy.deepcopy(tmp)
#     #         tmp = []
#     #         ans += 1
    
#     # return -1

# a = [[3,4,2,1,5],[4,2,3,1,5],[2,1,0,0,5],[2,4,0,0,5]]
# print(f'======{minimumVisitedCells(a)}======')

##################################################################################
##################################################################################
##################################################################################
# import bisect
# def searchRange(nums, target):
#     ### solution 1: 二分查找 + 遍历右侧
#     n = len(nums)
#     if not n:
#         return [-1,-1]
#     l = bisect.bisect_left(nums, target)
#     if l >= n:
#         return [-1, -1]
#     if nums[l] == target:
#         r = l
#         while (r+1 <= n-1) and (nums[r+1] == target):
#             r += 1
#         return [l,r]
#     else:
#         return [-1,-1]

# a = [5,7,7,8,8,10]
# b = 8
# print(f'===={searchRange(a,b)}====')

##################################################################################
##################################################################################
##################################################################################
# def search(nums, target):
#     ### solution 2: 双指针+二分查找
#     n = len(nums)
#     i = 0
#     j = n-1
#     while j-i > 1:
#         if nums[i] == target:
#             return i
#         if target == nums[j]:
#             return j

#         mid = (i+j)//2
#         if (target <= nums[mid]):
#             if (target <= nums[i] <= nums[mid]):
#                 i = mid
#             else:
#                 j = mid
#         else:
#             if (nums[mid] <= nums[j] <= target):
#                 j = mid
#             else:
#                 i = mid
    
#     if (nums[i] == target):
#         return i
#     if (nums[j] == target):
#         return j
#     else:
#         return -1

# a = [4,5,6,7,0,1,2]
# b = 1
# print(f"======{search(a, b)}======")

##################################################################################
##################################################################################
##################################################################################
# def maximumScore(nums, k):
#     ### solution 5: 双指针 优化
#     # n = len(nums)
#     # ans = nums[k] * 1
#     # i = k-1
#     # j = k+1
#     # min_v = nums[k]
#     # while True:
#     #     while (i >= 0) and (nums[i] >= min_v):
#     #         i -= 1
#     #     while (j <= n-1) and (nums[j] >= min_v):
#     #         j += 1
        
#     #     ans = max(ans, min_v*(j-i-1))

#     #     if (i == -1) and (j == n):
#     #         break
#     #     elif (i != -1) and (j == n):
#     #         min_v = nums[i]
#     #     elif (i == -1) and (j != n):
#     #         min_v = nums[j]
#     #     else:
#     #         min_v = max(nums[i], nums[j])

#     # return ans

#     ### solution 4: 双指针
#     # n = len(nums)
#     # ans = nums[k] * 1
#     # i = k
#     # j = k
#     # min_v = nums[k]
#     # while True:
#     #     while (not left_end):
#     #         if (nums[i] >= min_v):
#     #             i -= 1
#     #             if i < 0:
#     #                 left_end = True
#     #                 break
#     #         else:
#     #             break
#     #     while (not right_end):
#     #         if (nums[j] >= min_v):
#     #             j += 1
#     #             if j > n-1:
#     #                 right_end = True
#     #                 break
#     #         else:
#     #             break
        
#     #     ans = max(ans, min_v*(j-i-1))

#     #     if left_end & right_end:
#     #         break
#     #     elif (not left_end) & right_end:
#     #         min_v = nums[i]
#     #     elif left_end & (not right_end):
#     #         min_v = nums[j]
#     #     else:
#     #         if nums[i] <= nums[j]:
#     #             min_v = nums[j]
#     #         else:
#     #             min_v = nums[i]

#     # return ans

#     ### solution 3: 双向维护最小值
#     # n = len(nums)
#     # ans = nums[k] * 1
    
#     # min_l = nums[k]
#     # for i in range(k-1, -1, -1):
#     #     if nums[i] < min_l:
#     #         min_l = nums[i]
#     #     else:
#     #         nums[i] = min_l
    
#     # min_r = nums[k]
#     # for j in range(k+1, n):
#     #     if nums[j] < min_r:
#     #         min_r = nums[j]
#     #     else:
#     #         nums[j] = min_r
    
#     # for i in range(k, -1, -1):
#     #     for j in range(k, n):
#     #         ans = max(ans, min(nums[i], nums[j])*(j-i+1) )
    
#     # return ans

#     ### solution 2: 小根堆
#     # n = len(nums)
#     # ans = nums[k] * 1
#     # for i in range(k, -1, -1):
#     #     nums_ind = nums[i:k].copy()
#     #     heapq.heapify(nums_ind)
#     #     for j in range(k,n):
#     #         heapq.heappush(nums_ind, nums[j])
#     #         ans = max(ans, nums_ind[0]*(j-i+1))
    
#     # return ans

# a = [1,4,3,7,4,5]
# b = 3
# print(f'==={maximumScore(a,b)}===')

##################################################################################
##################################################################################
##################################################################################
# def findMinHeightTrees(n, edges):
#     ### solution 2: bfs并记录parents, 先0到最远节点x，然后x到最远节点y，最后根据parents找到path，返回path中间的节点
#     # if n == 1:
#     #     return [0]
    
#     # conn = [[] for i in range(n)]
#     # parents = [i for i in range(n)]

#     # for i,j in edges:
#     #     conn[i].append(j)
#     #     conn[j].append(i)
    
#     # def bfs(x):
#     #     nonlocal n
#     #     searched = [False] * n
#     #     fifo = [x]
#     #     while fifo:
#     #         x = fifo.pop(0)
#     #         searched[x] = True
#     #         for x_next in conn[x]:
#     #             if searched[x_next]:
#     #                 continue
#     #             else:
#     #                 fifo.append(x_next)
#     #                 parents[x_next] = x

#     #     return x
    
#     # x = bfs(0)
#     # y = bfs(x)
#     # path = [y]

#     # while y != x:
#     #     y = parents[y]
#     #     path.append(y)
    
#     # m = len(path)

#     # if m%2 :
#     #     return [path[m//2]]
#     # else:
#     #     return path[(m//2-1) : (m//2+1)]
    
#     ### solution 1: 暴力遍历 BFS
#     # if n == 1:
#     #     return [0]
#     # dis = dict()
#     # conn = dict()
#     # ans = []
#     # min_h = n
#     # for i,j in edges:
#     #     if i in conn:
#     #         conn[i].append(j)
#     #     else:
#     #         conn[i] = [j]
#     #     if j in conn:
#     #         conn[j].append(i)
#     #     else:
#     #         conn[j] = [i]
    

#     # for each_node in range(n):
#     #     fifo = [each_node]
#     #     next_fifo = []
#     #     search = set([each_node])
#     #     d = 1
#     #     while fifo:
#     #         cur = fifo.pop(0)
#     #         search.add(cur)
#     #         for next in conn[cur]:
#     #             if not next in search:
#     #                 dis[(each_node,next)] = d
#     #                 dis[(next, each_node)] = d
#     #                 next_fifo.append(next)

#     #         if fifo:
#     #             continue
#     #         else:
#     #             fifo = next_fifo
#     #             next_fifo = []
#     #             d += 1

#     #     if d-1 < min_h:
#     #         min_h = d-1
#     #         ans = [each_node]
#     #     elif d-1 == min_h:
#     #         ans.append(each_node)
    
#     # return ans
    
# a = 4
# b = [[1,0],[1,2],[1,3]]
# c = 1
# d = []
# print(f'==={findMinHeightTrees(a,b)}===')




##################################################################################
##################################################################################
##################################################################################
# def maxMoves(grid):
#     # ### solution 1: DFS，lifo后入先出，遍历，用set()保证不重复搜
#     # h = len(grid)
#     # w = len(grid[0])
#     # reach = set()
#     # lifo = [(i,0) for i in range(h)]
#     # max_step = 0

#     # while True:
#     #     i,j = lifo.pop()
#     #     cur_val = grid[i][j]
#     #     if (i-1 >= 0):
#     #         if (grid[i-1][j+1] > cur_val):
#     #             if (j+1 == w-1):
#     #                 max_step = j+1
#     #                 break
                
#     #             if not (i-1,j+1) in reach:
#     #                 lifo.append((i-1,j+1))
#     #                 reach.add((i-1,j+1))

#     #     if (i+1 <= h-1):
#     #         if (grid[i+1][j+1] > cur_val):
#     #             if (j+1 == w-1):
#     #                 max_step = j+1
#     #                 break
                
#     #             if not (i+1,j+1) in reach:
#     #                 lifo.append((i+1,j+1))
#     #                 reach.add((i+1,j+1))

#     #     if (grid[i][j+1] > cur_val):
#     #         if (j+1 == w-1):
#     #             max_step = j+1
#     #             break
            
#     #         if not (i,j+1) in reach:
#     #             lifo.append((i,j+1))
#     #             reach.add((i,j+1))

#     #     max_step = max(max_step, j)
#     #     if not lifo:
#     #         break

#     # return max_step



#     ### solution 2: solution 1 的简化
#     # h = len(grid)
#     # w = len(grid[0])
#     # lifo = [(i,0) for i in range(h)]
#     # max_step = 0

#     # while True:
#     #     i,j = lifo.pop()
#     #     cur_val = grid[i][j]
#     #     for k in [i-1, i, i+1]:
#     #         if (0 <= k) & (k <= h-1):
#     #             if (grid[k][j+1] > cur_val):
#     #                 if (j+1 == w-1):
#     #                     max_step = j+1
#     #                     break
                    
#     #                 lifo.append((k,j+1))
#     #                 grid[i][j] = 0
#     #                 max_step = max(max_step, j+1)
#     #     if not lifo:
#     #         break

#     # return max_step

# a = [[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068],[1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]]
# print(f'==={maxMoves(a)}===')

##################################################################################
##################################################################################
##################################################################################
# def shortestSubstrings(arr):
#     ### solution 3: 字典：所有substring -> 包含的string的index
#     ###           + set： 已经搜索过的substring
#     # hh = dict()
#     # has_sub = set()
#     # ans = [""]*len(arr)
#     # for ind,each in enumerate(arr):
#     #     for i in range(0, len(each)):
#     #         for j in range(i+1, len(each)+1):
#     #             sub_i_j = each[i:j]

#     #             if sub_i_j in has_sub:
#     #                 continue
                
#     #             if sub_i_j in hh:
#     #                 if hh[sub_i_j] != ind:
#     #                     del hh[sub_i_j]
#     #                     has_sub.add(sub_i_j)
#     #             else:
#     #                 hh[sub_i_j]  = ind

#     # for k,v in hh.items():
#     #     if not (ans[v]):
#     #         ans[v] = k
#     #     else:
#     #         if len(k) < len(ans[v]):
#     #             ans[v] = k
#     #         elif len(k) == len(ans[v]):
#     #             ans[v] = min(ans[v], k)
    
#     # return ans
    
#     ### solution 2: 字典：所有substring -> 包含的string的index的set
#     # hh = dict()
#     # ans = [""]*len(arr)
#     # for ind,each in enumerate(arr):
#     #     for i in range(0, len(each)):
#     #         for j in range(i+1, len(each)+1):
#     #             sub_i_j = each[i:j]
#     #             if sub_i_j in hh:
#     #                 hh[sub_i_j].add(ind)
#     #             else:
#     #                 hh[sub_i_j] = set([ind])
    
#     # for k,v in hh.items():
#     #     if len(v) == 1:
#     #         ind = list(v)[0]
#     #         if not (ans[ind]):
#     #             ans[ind] = k
#     #         else:
#     #             if len(k) < len(ans[ind]):
#     #                 ans[ind] = k
#     #             elif len(k) == len(ans[ind]):
#     #                 ans[ind] = min(ans[ind], k)
    
#     # return ans

#     ### solution 1: 字典：每个string -> 自己的substring
#     # hh = dict()
#     # ans = [""]*len(arr)
#     # for each in arr:
#     #     hh[each] = set()
#     #     for i in range(0, len(each)):
#     #         for j in range(i+1, len(each)+1):
#     #             hh[each].add(each[i:j])
#     # for i,each_i in enumerate(arr):
#     #     cur = hh[each_i]
#     #     for j,each_j in enumerate(arr):
#     #         if i==j:
#     #             continue
#     #         cur = cur - hh[each_j]
#     #     if cur:
#     #         min_sub = list(cur)[0]
#     #         min_l = len(min_sub)
#     #         for each_unique_sub in cur:
#     #             if len(each_unique_sub) < min_l:
#     #                 min_l = len(each_unique_sub)
#     #                 min_sub = each_unique_sub
#     #             elif len(each_unique_sub) == min_l:
#     #                 min_sub = min(min_sub, each_unique_sub)
            
#     #         ans[i] = min_sub
    
#     # return ans

# a = ["vbb","grg","lexn","oklqe","yxav"]
# print(f'=={shortestSubstrings(a)}==')

##################################################################################
##################################################################################
##################################################################################
# import bisect
# def maximumHappinessSum(happiness, k):
#     ### soluton 2: 遍历
#     # n = len(happiness)
#     # happiness.sort()
#     # ans = 0
#     # ind = 1
#     # while ind <= k:
#     #     if happiness[-ind] > (ind-1):
#     #         ans += happiness[-ind] - (ind-1)
#     #     else:
#     #         break
#     #     ind += 1
#     # return ans

#     ### solution 2: 二分插入 bisect
#     # n = len(happiness)
#     # happiness.sort(reverse = False)
#     # ind = bisect.bisect_left(happiness, k)
#     # print(n, ind, k, happiness)
#     # if n-ind >= k:
#     #     return sum(happiness[n-k:]) - (k-1)*k//2
#     # else:
#     #     ind2 = 0
#     #     for i in range(1,n+1):
#     #         if happiness[-i] <= i-1:
#     #             ind2 = n-i+1
#     #             break
#     #     return sum(happiness[ind2:]) - (n-ind2-1)*(n-ind2)//2
#     ### solution 3: 寻找递减为0的一项
#     # n = len(happiness)
#     # happiness.sort(reverse = True)  #降序
#     # ind = 0
#     # if (happiness[k-1] >= k):
#     #     return sum(happiness[:k]) - k*(k-1)//2
#     # for i in range(n):
#     #     if (happiness[i] <= i):
#     #         ind = i
#     #         break
#     # return sum(happiness[:ind]) - ind*(ind-1)//2

# a = [12,1,42]
# b = 3
# print(f'=={maximumHappinessSum(a,b)}==')

##################################################################################
##################################################################################
##################################################################################
# def sellingWood(m, n, prices):
#     ### solution1：暴力遍历
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             for k1,k2,v in prices:
#                 if (i-k1>=0) & (j-k2>=0):
#                     dp[i][j] = max(dp[i-k1][j]+v+dp[k1][j-k2], dp[i][j])
#                     dp[i][j] = max(dp[i][j-k2]+v+dp[i-k1][k2], dp[i][j])
#     return dp[m][n]

#     ### solution2: 切一刀按块算, 1+4 = 4+1, 遍历一半
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     for k1,k2,p in prices:
#         dp[k1][k2] = p
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             for i2 in range(1, i//2 + 1):
#                 dp[i][j] = max(dp[i2][j] + dp[i-i2][j], dp[i][j])
#             for j2 in range(1, j//2+1):
#                 dp[i][j] = max(dp[i][j2] + dp[i][j-j2], dp[i][j])
#     return dp[m][n]

# a = 3
# b = 5
# c = [[1,4,2],[2,2,7],[2,1,3]]
# print(f'==={sellingWood(a,b,c)}===')

##################################################################################
##################################################################################
##################################################################################
# def maxArrayValue(nums):
#     max = nums[-1]
#     for i in range(2,len(nums)+1):
#         if nums[-i] <= max:
#             max += nums[-i]
#         else:
#             max = nums[-i]
#     return max

# a = [2,3,7,9,3]
# print(f'result==={maxArrayValue(a)}===')

##################################################################################
##################################################################################
##################################################################################
# def maxArrayValue(nums):
#     i = 1
#     max = nums[0]
#     while len(nums) >= i+1:
#         if nums[-i-1] <= nums[-i]:
#             nums[-i-1] += nums[-i]
#         i += 1
#         max = nums[-i]
#     return max

# a = [2,3,7,9,3]
# print(f'result==={maxArrayValue(a)}===')

##################################################################################
##################################################################################
##################################################################################
# def maximumOddBinaryNumber(s):
#     n = len(s)
#     # one_num = sum(int(_) for _ in s if _ == '1')
#     one_num = s.count('1')
#     return '1'*(one_num-1) + '0'*(n-one_num) + '1'

##################################################################################
##################################################################################
##################################################################################
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class FindElements:
#     def __init__(self, root):
#         self.root = root
#         self.has = set()

#         self.root.val = 0
#         self.has.add(0)

#         def dfs(node, set_add):
#             if node.left:
#                 node.left.val = 2 * node.val + 1
#                 set_add.add(node.left.val)
#                 dfs(node.left, set_add)
#             if node.right:
#                 node.right.val = 2 * node.val + 2
#                 set_add.add(node.right.val)
#                 dfs(node.right, set_add)
#             if (not node.left) & (not node.right):
#                 return
        
#         dfs(self.root, self.has)
    
#         # def pt(node):
#         #     if node:
#         #         print(node.val)
#         #     if node.left:
#         #         pt(node.left)
#         #     if node.right:
#         #         pt(node.right)
#         # pt(self.root)

#     def find(self, target):
#         return target in self.has

#         # def find_dfs(node, x):
#         #     rlt = False
#         #     if (node.val == x):
#         #         rlt |= True
#         #     else:
#         #         if node.left:
#         #             rlt |= find_dfs(node.left, x)
#         #         if node.right:
#         #             rlt |= find_dfs(node.right, x)
#         #         if (not node.left) & (not node.right):
#         #             rlt |= False
#         #     return rlt
#         # return find_dfs(self.root, target)

# a = TreeNode(-1)
# a.right = TreeNode(-1)
# b = FindElements(a)
# print("====1====", b.find(1))
# print("====2====", b.find(2))

##################################################################################
##################################################################################
##################################################################################
# upper()：所有字母大写
# lower()：所有字母小写
# capitalize()：首字母大写，其他字母小写
# title()：每个单词首字母大写，其他小写
# def capitalizeTitle(title):
#     title = title.lower()
#     words = title.split(' ')
#     for i,word in enumerate(words):
#         if len(word) > 2:
#             words[i] = words[i].capitalize()
#     return ' '.join(words)

# a = "First leTTeR of EACH Word"
# print(f"==={capitalizeTitle(a)}====")

##################################################################################
##################################################################################
##################################################################################
# def getHint(secret, guess):
#     x = 0
#     y = 0
#     n = len(secret)
#     s_g = [[0,0] for _ in range(10)]
#     for i in range(n):
#         if secret[i] == guess[i]:
#             x += 1
#         else:
#             s_g[int(secret[i])][0] += 1
#             s_g[int(guess[i])][1] += 1
#     y = sum([min(i,j) for i,j in s_g])
#     return str(x)+'A'+str(y)+'B'

# a = "1807"
# b = "7810"
# print("aaaa===:", getHint(a,b))

##################################################################################
##################################################################################
##################################################################################
# from sortedcontainers import SortedList
# import itertools

# ### 排列
# # lst = [1, 2, 3]
# # permutations_lst = list(itertools.permutations(lst, 2))
# # print(permutations_lst) 

# ### 组合
# # lst = [1, 2, 3]
# # combinations_lst = list(itertools.combinations(lst, 2))
# # print(combinations_lst)
# import heapq
# def kSum(nums, k):
#     sum = 0
#     for i, x in enumerate(nums):
#         if x >= 0:
#             sum += x
#         else:
#             nums[i] = -x
#     nums.sort()

#     h = [(0, 0)]  # 空子序列
#     for _ in range(k - 1):
#         s, i = heapq.heappop(h)
#         if i < len(nums):
#             # 在子序列的末尾添加 nums[i]
#             heapq.heappush(h, (s + nums[i], i + 1))  # 下一个添加/替换的元素下标为 i+1
#             if i:  # 替换子序列的末尾元素为 nums[i]
#                 heapq.heappush(h, (s + nums[i] - nums[i - 1], i + 1))
#     return sum - h[0][0]

##################################################################################
##################################################################################
##################################################################################
# from sortedcontainers import SortedList
# import itertools

# ### 排列
# # lst = [1, 2, 3]
# # permutations_lst = list(itertools.permutations(lst, 2))
# # print(permutations_lst) 

# ### 组合
# # lst = [1, 2, 3]
# # combinations_lst = list(itertools.combinations(lst, 2))
# # print(combinations_lst)

# def kSum(nums, k):
#     # pos = SortedList()
#     # neg = SortedList()
#     # for _ in nums:
#     #     if _ >= 0:
#     #         pos.add(_)
#     #     else:
#     #         neg.add(_)
#     sum_l = SortedList(nums)
#     combinations_lst = [()]
#     i = 2
#     while i <= len(nums):
#         combinations_lst.extend(list(itertools.combinations(nums, i)))
#         i += 1
    
#     for _ in combinations_lst:
#         sum_l.add(sum(_))

#     print(sum_l)
#     return sum_l[-k]

##################################################################################
##################################################################################
##################################################################################
# def minimumPossibleSum(n, target):
#     ans = int()
#     h = target//2
#     mod = 10**9+7
#     # mod = 1e9 + 7
#     if n <= target/2:
#         ans = ((1+n) * n / 2) % mod
#     else:
#         ans = ((1+h) * h / 2) % mod
#         ans = (ans + ((2*target + n-h-1) * (n-h) / 2) % mod) % mod
#     return int(ans)

# a = 13
# b = 50
# print("AAAA", minimumPossibleSum(a,b))

##################################################################################
##################################################################################
##################################################################################
# ord():    char -> ascii 对应的 int[0,255]
# chr():    int [0,255] -> ascii 对应的符号 char
# def divisibilityArray(word, m):
#     n = len(word)
#     ans = [0]*n
#     tmp = 0
#     for i in range(n):
#         tmp = 10*tmp + int(word[i])
#         if (tmp%m) == 0:
#             ans[i] = 1
#     return ans

# a = "1010"
# b = 10
# print("aaaa", divisibilityArray(a, b))

##################################################################################
##################################################################################
##################################################################################
# def findKOr(nums, k):
#     #1 bin(12345).replace('0b','')
    
#     #2 "{0:b}".format(12345)
    
#     #3 binary = lambda n: if n==0 else binary(n/2) + str(n%2)
#     #3 binary(12345)

#     #4 condition = lambda x: x%2 == 1
    
#     ans = 0
#     loop_times = 0
#     while(1):
#         cnt = 0
#         for i in range(len(nums)):
#             if (nums[i]) & (nums[i]%2 == 1):
#                 cnt += 1
            
#             nums[i] = int(nums[i]/2)
#         if cnt >= k:
#             ans += 2**loop_times
#         if (sum([1 for each in nums if each]) < k):
#             break
#         loop_times += 1
#     return ans

# a = [2]
# print("aaaaaaa {} ".format(findKOr(a,1)))

##################################################################################
##################################################################################
##################################################################################
# def findKOr(nums, k):
#     #1 bin(12345).replace('0b','')
    
#     #2 "{0:b}".format(12345)
    
#     #3 binary = lambda n: if n==0 else binary(n/2) + str(n%2)
#     #3 binary(12345)

#     #4 condition = lambda x: x%2 == 1

#     str_nums = [bin(_).replace('0b','') for _ in nums]
    
#     ans = 0
#     n = len(nums)
#     max_l = len(bin(max(nums)))-2

#     for i in range(1,max_l+1):
#         cnt = 0
#         for _ in str_nums:
#             if len(_) >= i:
#                 if _[-i] == '1':
#                     cnt += 1
#                     if cnt >= k:
#                         ans += 2**(i-1)
#                         break
#     return ans

# a = [7,12,9,8,9,15]
# print("aaaaaaa {} ".format(findKOr(a,4)))

##################################################################################
##################################################################################
##################################################################################
# def validPartition(nums):
#     l = len(nums)
#     dp = [True] + [False]*(3)

#     if (l < 2):
#         return False
#     else:
#         if (nums[0] == nums[1]):
#             dp[2] = dp[0]

#     for i in range(2, l):
        
#         if not (dp[2] | dp[1] | dp[0]):
#             return False

#         if (nums[i] == nums[i-1]):
#             dp[3] |= dp[1]
#             if (nums[i] == nums[i-2]):
#                 dp[3] |= dp[0]
#         elif (nums[i] == nums[i-1]+1) & (nums[i] == nums[i-2]+2):
#             dp[3] |= dp[0]

#         dp.pop(0)
#         dp.append(False)

#     return dp[-2]

##################################################################################
##################################################################################
##################################################################################
# def validPartition(nums):
#     l = len(nums)
#     dp = [False]*(l+1)
#     dp[0] = True

#     if (l < 2):
#         return False
#     else:
#         if (nums[0] == nums[1]):
#             dp[2] = dp[0]

#     for i in range(3, l+1):
        
#         if not (dp[i] | dp[i-2] | dp[i-3]):
#             return False

#         if (nums[i] == nums[i-1]):
#             dp[i] |= dp[i-2]
#             if (nums[i] == nums[i-3]):
#                 dp[i] |= dp[i-3]
#         elif (nums[i] == nums[i-1]+1) & (nums[i] == nums[i-3]+2):
#             dp[i] |= dp[i-3]
    
#         # print("99999999", i, dp)

#     return dp[l]

##################################################################################
##################################################################################
##################################################################################
# def isMatch(s: str, p: str) -> bool:
#     s_len = len(s)
#     p_len = len(p)
#     dp = [False] * (p_len+1)
#     dp[0] = True
#     for p_i in range(1,p_len+1):
#         if p[p_i] == '*':
#             dp[p_i] = dp[p_i-2]

#     dp_next = [False] * (p_len+1)

#     for i in range(1,s_len+1):
#         for j in range(1,p_len+1):
#             if (s[i]==p[j-1]) or (p[j-1] == '.'):
#                 dp_next[j] = dp[j-1]
#             elif p[j-1] == '*':
#                 dp_next[j] = dp_next[j-2]

#                 if (p[j-2] == s[i]) or (p[j-2] == '.'):
#                     dp_next[j] |= dp[j]

#         if not any(dp_next):
#             return False

#         dp = dp_next
#         dp_next = [False] * (p_len+1)

#     return dp[p_len]
            
# a = "a"
# b = ".*..a*"

# print(isMatch(a,b))

##################################################################################
##################################################################################
##################################################################################
# def isMatch(s: str, p: str) -> bool:
#     s_len = len(s)
#     p_len = len(p)
#     dp = [[False]*(p_len+1) for _ in range(s_len+1)]

#     dp[0][0] = True

#     # print("1111", dp)
#     for p_i in range(1,p_len+1):
#         if p[p_i] == '*':
#             dp[0][p_i] = dp[0][p_i-2]
#     # print("2222", dp)

#     for i in range(1,s_len+1):
#         for j in range(1,p_len+1):
#             if (s[i]==p[j-1]) or (p[j-1] == '.'):
#                 dp_next[j] = dp[j-1]
#             elif p[j-1] == '*':
#                 if (p[j-2] == s[i]) or (p[j-2] == '.'):
#                     dp_next[j] = dp_next[j-2] or dp_next[j-1] or dp[j]
#                 else:
#                     dp_next[j] = dp_next[j-2]
                
                
    
#             # print("99999 i j :", i, j, dp)
#     return dp[s_len][p_len]
            
# a = "a"
# b = ".*..a*"

# print(isMatch(a,b))
