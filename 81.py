# 81. 搜索旋转排序数组 II

from typing import List

def search(nums: List[int], target: int) -> bool:
    # solution 2: 二分法，添加一些条件
    l = 0
    r = len(nums) - 1
    t = 0
    while l < r:
        t += 1
        mid = (l+r)//2
        if mid == l:
            break
        
        if target == nums[r] or target == nums[l]:
            return True
        
        # 重复元素时，二分法的指针要移动
        while l < r-1 and nums[l] == nums[l+1]:
            l += 1
        while l < r-1 and nums[r] == nums[r-1]:
            r -= 1
        if nums[l] == nums[r]:
            l += 1

        elif nums[l] > nums[r]:
            if target < nums[r]:
                if nums[mid] == target:
                    return True
                elif nums[mid] >= nums[l]:
                    l = mid
                else:
                    if nums[mid] <= target:
                        l = mid
                    else:
                        r = mid
            else:
                if nums[mid] == target:
                    return True
                elif nums[mid] <= nums[r]:
                    r = mid
                else:
                    if nums[mid] <= target:
                        l = mid
                    else:
                        r = mid
        else:
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
    
    return nums[l] == target or nums[r] == target
    
    # solution 1: 直接找,暴力
    # return target in nums

a = search([1,0,1,1,1], 0)
print(a)

a = search([1,3], 3)
print(a)

a = search([-9,-9,-9,-8,-8,-7,-7,-7,-7,-6,
            -6,-6,-6,-6,-6,-6,-6,-6,-5,-5,
            -5,-5,-5,-4,-4,-4,-3,-3,-3,-3,
            -3,-3,-2,-2,-2,-2,-2,-2,-2,-2,
            -2,-2,-1,-1,-1,-1,-1,-1,0,0,
            0,1,1,2,2,2,2,2,2,2,
            3,3,3,3,4,4,4,4,4,5,
            5,5,5,5,5,5,6,6,6,7,
            7,7,7,7,8,9,9,9,10,10,
            10,10,10,10,10,-10,-9,-9,-9,-9], 2)
print(a)
