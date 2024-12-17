class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        # we can sort the array as we wish, because the "choose the lowest i"
        # rule is syntactic sugar and doesnt' actually change the answer
        
        # example array, sorted:
        # [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        # grouped by value, still sorted:
        # {1: 4, 2: 3, 3: 2, 4: 1}
        #   0*4 + 1*3 + 2*2 + 3*1   # === sum of (index * count)
        # === (count at this value) * (levels higher than lowest value)
        
        C = Counter(nums)
        answer = [
            index * count
            for index, (num, count) in enumerate(sorted(C.items()))
        ]
        print(f'{answer=}')
        return sum(answer)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 179 ms Beats 14.57%
# NOTE: Memory 31.46 MB Beats 5.39%
