class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def DP(nums: List[int]) -> Tuple[int,int]:
            # returns (my_score, other_player_score)
            # therefore we must receive these in the other order
            print(f'DP({nums})')
            if not nums:
                print(f'  trivial 0 0')
                return (0, 0)
            first = nums[0]
            not_first = nums[1:]
            last = nums[-1]
            not_last = nums[:-1]
            if len(nums) == 1:
                print(f'  trivial N 0')
                return (first, 0)
            (him_first, me_first) = DP(not_first)
            me_first += first
            print(f'  first: ({me_first}, {him_first})')
            (him_last, me_last) = DP(not_last)
            me_last += last
            print(f'  last : ({me_last}, {him_last})')
            if (me_first > me_last):
                print(f'  take first')
                return (me_first, him_first)
            else:
                print(f'  take last')
                return (me_last, him_last)

        (P1, P2) = DP(tuple(nums))
        print(f'Final answers: ({P1},{P2})')

        return P1 >= P2     # player 1 wins ties

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 52 ms Beats 34.11%
# NOTE: Memory 17.29 MB Beats 5.12%
