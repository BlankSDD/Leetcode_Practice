# 1600. 王位继承顺序

class ThroneInheritance:
    ### solution 2: 父子表 + 一直维持继承表 + 划去死亡的，超时
    # def __init__(self, kingName):
    #     self.p_c = dict()
    #     self.heritance = [kingName]
    #     self.dead = set()

    # def birth(self, parentName, childName):
    #     cur = parentName
    #     while (cur in self.p_c) and (self.p_c[cur]):
    #         cur = self.p_c[cur][-1]
    #     insert_index = self.heritance.index(cur)
    #     self.heritance = self.heritance[:insert_index+1] + [childName] + self.heritance[insert_index+1:]
        
    #     if not parentName in self.p_c:
    #         self.p_c[parentName] = [childName]
    #     else:
    #         self.p_c[parentName].append(childName)

    # def death(self, name: str):
    #     self.dead.add(name)

    # def getInheritanceOrder(self):
    #     tmp = copy.deepcopy(self.heritance)
    #     for each in self.dead:
    #         tmp.remove(each)
    #     return tmp

    ### solution 1: 父子表 + 死亡名单 + 重新生成继承表 + 划去死亡的
    def __init__(self, kingName):
        self.king = kingName
        self.p_c = dict()
        self.dead = set()

    def birth(self, parentName, childName):
        if not parentName in self.p_c:
            self.p_c[parentName] = [childName]
        else:
            self.p_c[parentName].append(childName)

    def death(self, name):
        self.dead.add(name)

    def getInheritanceOrder(self):
        ans = []
        tmp = [self.king]
        while tmp:
            cur = tmp.pop(0)
            if not cur in self.dead:
                ans.append(cur)
            
            if cur in self.p_c:
                tmp = self.p_c[cur] + tmp
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
