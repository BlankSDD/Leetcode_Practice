# 1483. 树节点的第 K 个祖先

class TreeAncestor:
    ### solution 2: 倍增， ST表， 动态规划
    def __init__(self, n, parent):
        self.n = n
        st = [ [-1]*16 for _ in range(n) ]
            
        for i in range(n):
            st[i][0] = parent[i]
        
        for j in range(1, 16):
            for i in range(n):
                if st[i][j-1] != -1:
                    st[i][j] = st[st[i][j-1]][j-1]
        
        self.st = st
        
    def getKthAncestor(self, node, k):
        ### 从k的高位到低位
        k_bin = bin(k)[2:]
        nk = len(k_bin)
        for j in range(nk):
            if k_bin[j] == '1':
                node = self.st[node][nk-1-j]
                if node == -1:
                    return -1
        return node
        
        ### 从k的低位到高位
        # for j in range(16):
        #     if ((k >> j) & 1):
        #         node = self.st[node][j]
        #         if (node == -1):
        #             return -1
        # return node



    ### solution 1: dfs遍历 + 祖先存储，超时
    # def __init__(self, n, parent):
    #     self.n = n
    #     self.p = [ [] for _ in range(n) ]
    #     self.parent = parent
    #     self.searched = [True] + [False] * (n-1)

    # def getKthAncestor(self, node, k):
    #     def dfs(x):
    #         if self.searched[x]:
    #             return
    #         self.searched[x] = True
    #         f = self.parent[x]
    #         self.p[x].append(f)
    #         dfs(f)
    #         self.p[x] += self.p[f]

    #     dfs(node)
    #     return self.p[node][k-1] if k <= len(self.p[node]) else -1


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
