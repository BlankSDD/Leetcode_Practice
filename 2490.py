# 2490. 回环句

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        
        pre = words[0][-1]
        for w in words[1:]:
            if (pre != w[0]):
                return False
            pre = w[-1]
        
        return sentence[0] == sentence[-1]
