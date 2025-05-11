class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        if minK > maxK:
            return 0
        
        types = [
            (
                'B' if N == minK == maxK else
                '-' if N == minK else
                '+' if N == maxK else
                ' ' if N < minK else
                ' ' if N > maxK else
                '0'
            )
            for N in nums
        ]
        # print(f'{types=}')
        types = ''.join(types)
        # print(f'{types=}')
        types = types.split(' ')
        # print(f'{types=}')

        answer = 0
        for subarray in types:
            # print(f'{subarray=}')
            mins = maxes = 0
            L = R = 0
            Len = len(subarray)
            while L <= R <= Len:
                # print(f'[{L}:{R}] {mins}/{maxes}')
                if mins and maxes:
                    additional = Len - R + 1
                    # print(f'  YES: +{additional} and shrink left')
                    answer += additional
                    A = subarray[L]
                    if A in ['-', 'B']:
                        mins -= 1
                    if A in ['+', 'B']:
                        maxes -= 1
                    L += 1
                else:
                    # print(f'  NO:  expand right')
                    try:
                        A = subarray[R]
                    except IndexError:
                        # print(f'    FAIL: OOB')
                        break
                    if A in ['-', 'B']:
                        mins += 1
                    if A in ['+', 'B']:
                        maxes += 1
                    R += 1

        return answer

# NOTE: Acceptance Rate 69.4% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case: min > max, Output Exceeds)
# NOTE: Runtime 193 ms Beats 12.33%
# NOTE: Memory 29.03 MB Beats 10.36%
