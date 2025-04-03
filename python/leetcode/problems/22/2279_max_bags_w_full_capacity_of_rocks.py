class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        spare = [
            Cap - Rock
            for Cap, Rock in zip(capacity, rocks)
        ]
        spare.sort()
        # print(f'{spare=}')

        answer = 0
        for S in spare:
            print(f'{additionalRocks}: {S} {answer=}')
            if S > additionalRocks:
                print(f'  Out of rocks: quitting')
                break
            answer += 1
            additionalRocks -= S
        
        return answer

# NOTE: Acceptance Rate 67.5% (medium)

# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 151 ms Beats 8.31%
# NOTE: Memory 25.19 MB Beats 60.13%
