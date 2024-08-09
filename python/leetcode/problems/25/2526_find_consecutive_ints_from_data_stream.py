class DataStream:

    # ignoring the Hint given, a queue structure is not required:
    #   we only need a count

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.runOfConsecutiveValue = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.runOfConsecutiveValue += 1
            print(f'Now a run of {self.runOfConsecutiveValue} {self.value}s')
        else:
            self.runOfConsecutiveValue = 0
            print(f'{num} is not a {self.value}')
        return self.runOfConsecutiveValue >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

# NOTE: Runtime 458 ms Beats 7.29%
# NOTE: Memory 43.13 MB Beats 44.94%
