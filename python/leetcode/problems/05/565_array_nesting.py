class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        loops = [None] * len(nums)
        while None in loops:
            k = loops.index(None)
            label = k
            print(f'marking loop #{label}:')
            while loops[k] is None:
                loops[k] = label
                print(f'  {k=}')
                k = nums[k]
            # print(f'HALT loop #{label} at {k}')
        
        print(f'{loops=}')
        counters = Counter(loops)
        print(f'{counters=}')
        counts = [
            count
            for loop, count in counters.items()
        ]
        print(f'{counts=}')
        return max(counts)

