class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0
        return

    def visit(self, url: str) -> None:
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index += 1
        return

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.index = 0
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index += steps
        MAX_INDEX = len(self.history) - 1
        if self.index > MAX_INDEX:
            self.index = MAX_INDEX
        return self.history[self.index]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 28 ms Beats 78.99%
# NOTE: Memory 19.21 MB Beats 47.28%
