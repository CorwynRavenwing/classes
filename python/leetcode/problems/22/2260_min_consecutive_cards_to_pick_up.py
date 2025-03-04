class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        indexesByValue = {}
        for index, value in enumerate(cards):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        print(f'{indexesByValue=}')

        answers = [
            (B - A + 1)
            for indexes in indexesByValue.values()
            for (A, B) in pairwise(indexes)
        ]
        print(f'{answers=}')

        return min(answers, default=-1)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 299 ms Beats 5.18%
# NOTE: Memory 47.81 MB Beats 7.03%
