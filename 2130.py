# 2130. 链表最大孪生和

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import inf


class Solution:
    def pairSum(self, head):
        ### solution 2: 快慢双指针，反转后半链表，遍历一次
        s = head
        f = head.next

        while f.next:
            s = s.next
            f = f.next.next
        
        # 反转 方式1： 倒序插入
        # s    cur   nxt
        # A    B     C    D E F G
        # 1. B -> D
        # 2. C -> A之后的 （把 C 看成前后都断）
        # 3. A -> C
        # 遍历
        cur = s.next
        while cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = s.next
            s.next = nxt


        # 反转 方式2： 
        # s    cur                 f
        # A    B     C    D E F    G
        # 1. A -> G ，形成两条链
        # 2. cur （把 cur 看成前后都断），把 cur 插入到 f 后一位
        #  即： A -> G -> B
        #  f 指针不动
        # 3. cur 右移一位, 遍历至 cur == f
        # cur = s.next
        # s.next = f

        # while cur != f:
        #     tmp = cur.next
        #     cur.next = f.next
        #     f.next = cur
        #     cur = tmp

        ans = -inf
        s = head
        while f:
            ans = max(ans, s.val + f.val)
            s = s.next
            f = f.next

        return ans


        ### solution 1: 单指针，遍历链表一次
        # if not head:
        #     return 0

        # s = []
        # cur = head
        # while cur:
        #     s.append(cur.val)
        #     cur = cur.next
        
        # i = 0
        # j = len(s) - 1
        # ans = -inf
        # while i < j:
        #     ans = max(ans, s[i] + s[j])
        #     i += 1
        #     j -= 1
        # return ans
