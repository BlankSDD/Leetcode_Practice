# 1472. 设计浏览器历史记录

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_index = 0
        self.cur = homepage
        self.his = [homepage]

    def visit(self, url: str) -> None:
        self.cur_index += 1
        self.cur = url
        if self.cur_index >= len(self.his):
            self.his.append(url)
        else:
            self.his[self.cur_index] = url
            self.his = self.his[:self.cur_index+1]

    def back(self, steps: int) -> str:
        self.cur_index = max(0, self.cur_index-steps)
        self.cur = self.his[self.cur_index]
        return self.cur
        
    def forward(self, steps: int) -> str:
        self.cur_index = min(len(self.his)-1, self.cur_index+steps)
        self.cur = self.his[self.cur_index]
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
