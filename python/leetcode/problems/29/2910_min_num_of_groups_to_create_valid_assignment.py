class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:

        @cache
        def bestSplit(total, X) -> int:
            # print(f'bestSplit({total},{X})')
            options = [float('inf')]
            x_plus_one_piles = 0
            x_piles = total // X
            remainder = total % X
            x_piles -= remainder            # distribute "remainder" ones
            x_plus_one_piles += remainder   # among this group of "X" piles
            while x_piles >= 0:
                # print(f'  Option:')
                # if x_piles:
                #     # print(f'    {x_piles} piles of {X}')
                # if x_plus_one_piles:
                #     # print(f'    {x_plus_one_piles} piles of {X+1}')
                options.append(x_piles + x_plus_one_piles)

                x_piles -= 1                    # remove 1 "X" pile
                remainder = X                   # redistribute its members 1 by 1:
                x_piles -= remainder            # turn that many "X" piles ...
                x_plus_one_piles += remainder   # into that many "X+1" piles

            answer = min(options)
            # print(f'{answer=} {options=}')
            return answer
        
        counts = Counter(balls)
        # print(f'{counts=}')

        minCount = min([
            count
            for ball, count in counts.items()
        ])
        print(f'{minCount=}')

        def bucketsIfSplitByX(X: int) -> int:
            print(f'\nbucketsIfSplitByX({X})')
            buckets = 0
            for ball, count in counts.items():
                buckets += bestSplit(count, X)

            print(f'Grand total {buckets}')
            return buckets

        return min([
            bucketsIfSplitByX(X)
            for X in range(1, minCount + 2)
        ])

# NOTE: Runtime 1110 ms Beats 5.36%
# NOTE: Memory 48.30 MB Beats 6.25%
