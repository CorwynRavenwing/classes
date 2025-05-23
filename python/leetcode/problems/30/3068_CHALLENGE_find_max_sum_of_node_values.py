class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        # SHORTCUT 1: Since this is a tree, we can always flip
        # any two nodes regardless of whether they share an edge,
        # by flipping the intervening nodes twice (which cancel
        # out because XOR is its own inverse)

        # SHORTCUT 2: Some numbers increase when XOR'ed with K, while some
        # numbers decrease.  We want to only use numbers that increase,
        # want the numbers that increase *the most*, and can only use
        # an even number of them.

        answer = sum(nums)
        print(f'{answer=}')

        XORs = [
            (N, N ^ k)
            for N in nums
        ]
        print(f'{XORs=}')

        changes = [
            changed - orig
            for (orig, changed) in XORs
        ]
        print(f'{changes=}')

        changes.sort(reverse=True)
        print(f'{changes=}')

        if len(changes) % 2 != 0:
            print(f'  Odd: deleting smallest one')
            changes.pop(-1)
        
        while changes:
            (A, B) = changes[:2]
            changes = changes[2:]
            if A + B < 0:
                print(f'ran out of positive changes')
                break
            answer += A + B

        return answer

# NOTE: Acceptance Rate 65.8% (HARD)

# NOTE: I had attempted this one before, failed, and am trying again.

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case: big plus + small minus)
# NOTE: Runtime 589 ms Beats 5.17%
# NOTE: Memory 27.64 MB Beats 17.24%
