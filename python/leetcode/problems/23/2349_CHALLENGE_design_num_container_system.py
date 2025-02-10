class NumberContainers:

    def __init__(self):
        self.DataAt = {}
        self.IndexesWith = {}
        return
    
    def change(self, index: int, number: int) -> None:
        try:
            oldNumber = self.DataAt[index]
            self.IndexesWith[oldNumber].remove(index)
        except KeyError:
            pass

        self.DataAt[index] = number
        self.IndexesWith.setdefault(number, [])
        bisect.insort(self.IndexesWith[number], index)
        return

    def find(self, number: int) -> int:
        try:
            indexes = self.IndexesWith[number]
            answer = indexes[0]
        except (KeyError, IndexError):
            answer = -1
        return answer

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# NOTE: Runtime 5674 ms Beats 5.48%
# NOTE: Memory 74.72 MB Beats 54.27%

# NOTE: re-ran for challenge:
# NOTE: Runtime 5464 ms Beats 5.39%
# NOTE: Memory 76.48 MB Beats 81.37%
# NOTE: same memory; much better percentage
