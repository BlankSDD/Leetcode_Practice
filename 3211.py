# 3211. 生成不含相邻零的二进制字符串
from typing import List


def validStrings(n: int) -> List[str]:
    # solution 1: 队列，遍历
    tmp = ["0", "1"]
    if n == 1:
        return tmp
    
    result = []
    while tmp:
        cur = tmp.pop(0)
        if len(cur) == n:
            result.append(cur)
            continue
        if cur[-1] == '0':
            cur += '1'
            tmp.append(cur)
        else:
            tmp.append( cur+'0' )
            tmp.append( cur+'1' )
    
    return result
        
