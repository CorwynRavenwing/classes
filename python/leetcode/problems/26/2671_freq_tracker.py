class FrequencyTracker:

    def __init__(self):
        self.count = Counter()  # dict of tracked objects
        self.freq = Counter()   # dict of existing frequencies
        return

    def add(self, number: int) -> None:
        # print(f'+({number})')
        prior_freq = self.count[number]
        self.count[number] += 1
        new_freq = self.count[number]
        if prior_freq:
            self.freq[prior_freq] -= 1
        self.freq[new_freq] += 1
        # print(f'  {self.count=}')
        # print(f'  {self.freq =}')
        return

    def deleteOne(self, number: int) -> None:
        # print(f'-({number})')
        prior_freq = self.count[number]
        if prior_freq:
            self.count[number] -= 1
            new_freq = self.count[number]
            self.freq[prior_freq] -= 1
            self.freq[new_freq] += 1
        # print(f'  {self.count=}')
        # print(f'  {self.freq =}')
        return        

    def hasFrequency(self, frequency: int) -> bool:
        # print(f'?({frequency})')
        # print(f'  {self.freq =}')
        return (self.freq[frequency] > 0)

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# NOTE: Acceptance Rate 30.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 166 ms Beats 16.54%
# NOTE: Memory 80.71 MB Beats 36.84%
