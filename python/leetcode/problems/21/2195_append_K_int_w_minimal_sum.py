class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:

        n = k   # the max value we're summing
        numSet = set(nums)
        # if nothing crosses it, the answer == 1 + 2 + ... + k ==
        answer = n * (n + 1) // 2
        print(f'Start with Triangle({n}) = {answer}')
        nums_below_n = [
            Num
            for Num in numSet
            if Num <= n
        ]
        for Num in nums_below_n:
            answer -= Num
            n += 1
            while n in numSet:
                print(f'  (skip {n})')
                n += 1
            answer += n
            print(f'  Replace {Num} with {n}')
        return answer

