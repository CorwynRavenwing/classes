class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        DEBUG = False

        max_perim = 0
        
        nums.sort(reverse=True)
        # print(f'{nums=}')
        seen_A = set()
        seen_AB = set()
        seen_ABC = set()

        for i, A in enumerate(nums):
            if A in seen_A:
                # if DEBUG: print(f'[{i},-,-]: {A} SEEN')
                continue
            else:
                seen_A.add(A)
            if A * 3 <= max_perim:
                if DEBUG: print(f'{A=} * 3 <= {max_perim}: skip')
                continue    # no, should be break
            for j in range(i + 1, len(nums)):
                B = nums[j]
                AB = f'({A},{B},-)'
                if AB in seen_AB:
                    # if DEBUG: print(f'[{i},{j},-]: {AB} SEEN')
                    continue
                else:
                    seen_AB.add(AB)
                for k in range(j + 1, len(nums)):
                    C = nums[k]
                    ABC = f'({A},{B},{C})'
                    if ABC in seen_ABC:
                        # if DEBUG: print(f'[{i},{j},{k}]: {ABC} SEEN')
                        continue
                    else:
                        seen_ABC.add(ABC)
                    if A >= B + C:
                        # if DEBUG: print(f'[{i},{j},{k}]: {ABC} INVALID')
                        # if A B C is invalid, A B C' where C' < C is also invalid
                        break
                    else:
                        perim = A + B + C
                        if DEBUG: print(f'[{i},{j},{k}]: {ABC} {perim=}')
                        # yield perim
                        max_perim = max(perim, max_perim)
                        # if A B C is valid, A B C' where C' < C is *smaller*
                        break
        
        return max_perim

# NOTE: Acceptance Rate 58.0% (easy)

# NOTE: Accepted on first Run [for this algorithm]
# NOTE: Accepted on second Submit (Time Exceeded: needed cache)
# NOTE: Runtime 376 ms Beats 5.48%
# NOTE: Memory 27.03 MB Beats 6.53%
