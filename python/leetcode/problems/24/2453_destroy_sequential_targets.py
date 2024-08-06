class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:

        nums.sort()
        modulos = [
            N % space
            for N in nums
        ]
        print(f'{modulos=}')
        counts = Counter(modulos)
        print(f'{counts=}')
        maxCount = max(counts.values())
        print(f'{maxCount=}')
        rightAnswers = [
            mod
            for mod, count in counts.items()
            if count == maxCount
        ]
        print(f'{rightAnswers=}')

        for (number, mod) in zip(nums, modulos):
            if mod in rightAnswers:
                return number
        
        return -9999
# NOTE: Runtime 559 ms Beats 23.61%
# NOTE: Memory 48.54 MB Beats 6.95%
