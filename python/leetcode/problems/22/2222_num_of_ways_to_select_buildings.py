class Solution:
    def numberOfWays(self, s: str) -> int:

        nums = tuple(map(int, s))
        # print(f'{nums=}')
        
        # we borrow some code from #2155:

        onesLeft = 0
        zerosLeft = 0
        onesRight = sum(nums)
        zerosRight = len(nums) - onesRight 

        scores = []
        for index, value in enumerate(nums):
            # (1) remove this value from Right counts
            if value:
                onesRight -= 1
            else:
                zerosRight -= 1
            
            # (2) add this score
            if value:
                # "1": multiply zeros
                score = zerosLeft * zerosRight
            else:
                # "0": multiply ones
                score = onesLeft * onesRight
            
            # print(f'[{index}]: {score}')
            scores.append(score)
            
            # (3) add this value to Left counts
            if value:
                onesLeft += 1
            else:
                zerosLeft += 1

        scores.append(score)
        # print(f'{scores=}')
        return sum(scores)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Limit Exceeded)
# NOTE: Runtime 555 ms Beats 51.13%
# NOTE: Memory 23.30 MB Beats 25.50%
