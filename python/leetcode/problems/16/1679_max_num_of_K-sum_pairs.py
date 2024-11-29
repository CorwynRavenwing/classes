class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        counts = Counter(nums)
        answer = 0
        if k % 2 == 0:
            # only do this for even K:
            N = k // 2
            countN = counts[N]
            if countN:
                print(f'{N}({countN}) split')
                answer += countN // 2    # pair them with each other
                del counts[N]
        
        for N in tuple(counts.keys()):
            X = k - N
            countN = counts[N]
            if not countN:
                continue
            countX = counts[X]
            if not countX:
                continue
            print(f'{N}({countN}) + {X}({countX})')
            answer += min(countN, countX)
            del counts[N]
            del counts[X]
        
        return answer

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 501 ms Beats 40.87%
# NOTE: Memory 30.12 MB Beats 6.75%
