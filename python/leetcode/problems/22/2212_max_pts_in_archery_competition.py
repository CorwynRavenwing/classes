class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        # these functions all return (SCORE, (bob_arrows_columns), arrows_unused)
        def dp_skip(column_number: int, arrows_left: int) -> Tuple[int,List[int]]:
            skip = dp(column_number + 1, arrows_left)
            (score, bobsArrows, arrows_unused) = skip
            return (
                score,
                (0,) + bobsArrows,
                arrows_unused
            )
        
        def dp_take(column_number: int, arrows_left: int) -> Tuple[int,List[int]]:
            arrows_needed = aliceArrows[column_number] + 1
            if arrows_left < arrows_needed:
                return (0, (), arrows_left)
            take = dp(column_number + 1, arrows_left - arrows_needed)
            (score, bobsArrows, arrows_unused) = take
            
            return (
                score + column_number,
                (arrows_needed,) + bobsArrows,
                arrows_unused
            )
        
        def dp(column_number: int, arrows_left: int) -> Tuple[int,List[int]]:
            if column_number > 11:
                return (0, (), arrows_left)
            return max([
                dp_skip(column_number, arrows_left),
                dp_take(column_number, arrows_left),
            ])
        
        answer = dp(0, numArrows)
        print(f'{answer=}')
        (score, bobsArrows, arrows_unused) = answer
        retVal = list(bobsArrows)
        retVal[0] += arrows_unused
        print(f'{retVal=}')
        assert sum(retVal) == numArrows
        return retVal

# NOTE: Accepted on second Run (math error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 267 ms Beats 36.15%
# NOTE: Memory 17.83 MB Beats 63.08%
