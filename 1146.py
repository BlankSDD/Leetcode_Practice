# 1146. 快照数组

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        ### solution 1: 使用 dict 存储 只能用 依次遍历
        # self.a = [ {0:0} for _ in range(length)  ]

        ### solution 2: 使用 list 存储，可以使用 二分法 遍历
        self.b = [ [ [0, 0] ] for _ in range(length) ]
        self.ssid = -1


    def set(self, index: int, val: int) -> None:
        ### solution 1: 使用 dict 存储 只能用 依次遍历
        # self.a[index][self.ssid+1] = val

        ### solution 2: 使用 list 存储，可以使用 二分法 遍历
        if (self.ssid+1) == self.b[index][-1][0]:
            self.b[index][-1][1] = val
        else:
            self.b[index].append( [self.ssid+1, val] )

    def snap(self) -> int:
        self.ssid += 1
        return self.ssid


    def get(self, index: int, snap_id: int) -> int:
        ### solution 1: 使用 dict 存储 只能用 依次遍历
        # for i in range(snap_id, -1, -1):
        #     if i in self.a[index]:
        #         return self.a[index][i]

        ### solution 2: 使用 list 存储，可以使用 二分法 遍历
        x = bisect.bisect_left(self.b[index], [snap_id+1, -1])
        if x == 0:
            return 0
        else:
            return self.b[index][x-1][1]



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
