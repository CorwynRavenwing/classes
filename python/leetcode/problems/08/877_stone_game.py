class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        nums = piles    # variable rename

        # we borrow some code from #486:

        @cache
        def DP(nums: List[int]) -> Tuple[int,int]:
            # returns (my_score, other_player_score)
            # therefore we must receive these in the other order

            DEBUG = False

            # if DEBUG: print(f'DP({nums})')
            # if DEBUG: print(f'DP({len(nums)})')
            if not nums:
                if DEBUG: print(f'  trivial 0 0')
                return (0, 0)
            first = nums[0]
            not_first = nums[1:]
            last = nums[-1]
            not_last = nums[:-1]
            if len(nums) == 1:
                if DEBUG: print(f'  trivial N 0')
                return (first, 0)
            (him_first, me_first) = DP(not_first)
            me_first += first
            if DEBUG: print(f'  first: ({me_first}, {him_first})')
            (him_last, me_last) = DP(not_last)
            me_last += last
            if DEBUG: print(f'  last : ({me_last}, {him_last})')
            if (me_first > me_last):
                if DEBUG: print(f'  take first')
                return (me_first, him_first)
            else:
                if DEBUG: print(f'  take last')
                return (me_last, him_last)

        (P1, P2) = DP(tuple(nums))
        print(f'Final answers: ({P1},{P2})')

        return P1 >= P2     # player 1 wins ties

# NOTE: Re-used entire prior version as-is, changing 1 variable name
# NOTE: Runtime 2576 ms Beats 5.02%
# NOTE: Memory 284.54 MB Beats 5.97%
