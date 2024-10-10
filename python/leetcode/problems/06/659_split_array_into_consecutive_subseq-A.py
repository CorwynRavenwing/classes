class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        # the Greedy algorithm, which works for some cases
        # and not for others.
        
        numCounts = Counter(nums)
        while numCounts:
            print(f'{numCounts=}')
            First = min(numCounts)
            value = First
            length = 0
            while True:
                if numCounts[value]:
                    length += 1
                    numCounts[value] -= 1
                    if not numCounts[value]:
                        del numCounts[value]
                    value += 1
                else:
                    if length >= 3:
                        Last = value
                        print(f'Got sequence {length=} [{First} .. {Last}]')
                        break   # break while True == next numCounts
                    else:
                        Last = value - 1
                        print(f'FAIL: Sequence {length=} [{First} .. {Last}]')
                        return False
        return True

