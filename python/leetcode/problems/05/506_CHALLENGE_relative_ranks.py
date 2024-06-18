class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        print(f'{sorted_scores}')
        ranks = [
            sorted_scores.index(val) + 1
            for val in score
        ]
        print(f'{ranks}')
        ranks = [
            (
                "Gold Medal" if R == 1
                else "Silver Medal" if R == 2
                else "Bronze Medal" if R == 3
                else str(R)
            )
            for R in ranks
        ]
        return ranks

