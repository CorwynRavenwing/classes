class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        possiblePens = total // cost1
        # print(f'{possiblePens=}')
        answer = 0
        for pens in range(possiblePens + 1):
            moneyLeft = total - pens * cost1
            # print(f'  {pens=} {moneyLeft=}')
            possiblePencils = moneyLeft // cost2
            # if possiblePencils:
            #     # print(f'    buy 0 .. {possiblePencils} pencils')
            # else:
            #     # print(f'    buy 0 pencils')
            answer += possiblePencils + 1
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 353 ms Beats 45.80%
# NOTE: Memory 17.82 MB Beats 37.40%
