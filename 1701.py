# 1701. 平均等待时间

class Solution:
    def averageWaitingTime(self, customers):
        wait = 0
        cur = 0
        for arr,cook in customers:
            if cur <= arr:
                cur = arr
            
            cur += cook
            wait += (cur-arr)
            
        return wait/len(customers)

            
