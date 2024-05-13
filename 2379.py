# 2379. 得到 K 个黑块的最少涂色次数

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ### solution 1: 滑动窗口
        n = len(blocks)
        need_draw_num = blocks[:k].count('W')
        ans = need_draw_num
        for i in range(k, n):
            cur = blocks[i]
            pre = blocks[i-k]
            
            # 判断左右端口，优化写法：
            need_draw_num += (cur=='W') - (pre=='W')
            ans = min(ans, need_draw_num)

            # 判断左右端口
            # if (cur != pre):
            #     if cur == 'W':
            #         need_draw_num += 1
            #     else:
            #         need_draw_num -= 1
            #         ans = min(ans, need_draw_num)

        return ans
