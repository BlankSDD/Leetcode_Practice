# 3258. 统计满足 K 约束的子字符串数量 I

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for l in range(len(s)):

            if s[l] == '0':
                cur_0_cnt = 1
            else:
                cur_0_cnt = 0
            
            ans += 1

            for r in range(l+1, len(s)):

                if s[r] == '0':
                    cur_0_cnt += 1
                
                if (k >= cur_0_cnt) or (k >= r-l+1-cur_0_cnt):
                    ans += 1
        
        return ans
