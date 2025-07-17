class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        max_reachable = 0
        answer = 0

        for num in nums:
            next_int = max_reachable + 1
            while num > next_int:
                if next_int > n:
                    print(f'All numbers from {1} to {n} are reachable: STOP')
                    return answer
                print(f'{max_reachable}: [{next_int}] PATCH')
                answer += 1
                max_reachable += next_int
                next_int = max_reachable + 1
            print(f'{max_reachable}: [{num}] in original array')
            # don't add to answer here: original array members are free
            max_reachable += num

        while max_reachable < n:
            i = max_reachable + 1
            print(f'[{i}] not reachable: patch')
            answer += 1
            max_reachable += i

        return answer

# NOTE: Acceptance Rate 53.6% (HARD)

# NOTE: Runtime 12 ms Beats 2.20%
# NOTE: Memory 18.02 MB Beats 22.20%
