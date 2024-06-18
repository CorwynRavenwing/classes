class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        answer = 0
        if k == 0:
            print(f'{k=}: looking for nums that appear twice')
            counts = Counter(nums)
            for N, count in counts.items():
                if count > 1:
                    print(f'  found {count} {N}s')
                    answer += 1
            
            return answer
        
        print(f'{k=}: looking for numbers K apart')
        numSet = set(nums)  # ignore dups
        for N in numSet:
            if N + k in numSet:
                print(f'  found {N} and {N+k}')
                answer += 1

        return answer

# NOTE: very very low MS score, but only better than ~ 5% (long tail)
