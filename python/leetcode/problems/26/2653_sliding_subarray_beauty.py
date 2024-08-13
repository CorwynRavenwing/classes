class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        # remove positives, as they are irrelevant and need answer 0:
        nums = [
            min(N, 0)
            # N if (N < 0) else 0
            for N in nums
        ]
        # print(f'{nums=}')

        def getAnswerFromCounts(C: Counter) -> int:
            N = x - 1
            for number, count in sorted(C.items()):
                # print(f'Try {number}: {count} {N=}')
                if N < count:
                    # print(f'  Match')
                    return number
                else:
                    N -= count
                    # print(f'  No match, subtract {count}')
            print(f'  Should never get here')
            return None

        answer = []
        for i in range(k - 1, len(nums)):
            if i == k - 1:
                # print(f'  ({i=} create count {k=})')
                C = Counter(nums[:k])
            else:
                Old = nums[i - k]
                New = nums[i]
                # print(f'  ({i=} remove [{i-k}]{Old} add [{i}]{New})')
                C[Old] -= 1
                C[New] += 1
            A = getAnswerFromCounts(C)
            answer.append(A)
        
        return answer
# NOTE: Runtime 4810 ms Beats 5.06%
# NOTE: Memory 31.29 MB Beats 64.20%
