# 2589. 完成所有任务的最少时间

from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        ### solution 2: 按照 结束时间排序
        ###             1. 正序遍历工作， 占满期间的工作必须占满， 未占满先减去 已占用的工作时间，然后尽量从 结束时间 向 开始时间遍历，下一个工作也可以使用该时间
        n = len(tasks)
        # 按照 结束时间 升序排列（default,也就是reverse = False，升序）
        tasks.sort(key=lambda x: x[1])

        occupied_time = [0] * (tasks[-1][1]+1)

        for s,e,d in tasks:
            if (e-s+1 == d):
                occupied_time[s:e+1] = [1]*d
                continue
            
            res = d-sum(occupied_time[s:e+1])
            if res > 0:
                for i in range(e, s-1, -1):
                    if (not occupied_time[i]):
                        res -= 1
                        occupied_time[i] = 1
                        if (res == 0):
                            break
        
        return sum(occupied_time)



        ### solution 1: 按照 开始时间排序
        ###             1.把所有时间占满的工作先做了,并标记 已做+占用时间点
        ###             2.倒序 遍历， 把 占用时间点减去，剩下的未完成的时间尽量在最开始完成，这样，上一个工作也可以使用该时间 （或者，正序遍历，剩下的未完成的时间尽量在最后完成，下一个工作可以使用该时间）
        ###             3. 计算 占用时间总和
        # n = len(tasks)
        # finished = [0] * n
        # occupied_time = [0] * 2001

        # tasks.sort(key=lambda x: x[0])

        # for i, task in enumerate(tasks):
        #     s = task[0]
        #     e = task[1]
        #     d = task[2]
        #     if (e-s+1 == d):
        #         occupied_time[s:e+1] = [1]*d
        #         finished[i] = 1
        
        # for i,task in enumerate(tasks[::-1]):
        #     if finished[-i-1]:
        #         continue
        #     s = task[0]
        #     e = task[1]
        #     d = task[2]
        #     res = d-sum(occupied_time[s:e+1])
        #     if res > 0:
        #         for i in range(s, e+1):
        #             if (not occupied_time[i]):
        #                 res -= 1
        #                 occupied_time[i] = 1
        #                 if (res == 0):
        #                     break
        
        # return sum(occupied_time)
                
