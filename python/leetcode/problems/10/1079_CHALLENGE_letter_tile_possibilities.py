class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def DeleteIndex(counts: List[int], index: int) -> List[int]:
            A = counts[:index]
            B = ()                  # skip counts[index]
            C = counts[index+1:]
            return A + B + C

        def DecrementIndex(counts: List[int], index: int) -> List[int]:
            A = counts[:index]
            oldVal = counts[index]
            newVal = oldVal - 1
            B = (newVal,)
            C = counts[index+1:]
            return A + B + C

        @cache
        def DP(counts: List[int]) -> int:
            print(f'DP({counts})')
            if not counts:
                print(f'  (1 way to use no tiles)')
                return 1
            if 0 in counts:
                index = counts.index(0)
                new_counts = DeleteIndex(counts, index)
                print(f'  (remove 0)')
                return DP(new_counts)
            answers = [
                DP(DecrementIndex(counts,index))
                for index, value in enumerate(counts)
            ]
            # answers contains the values if each tile is used.
            # we also can use zero tiles:
            return sum(answers) + 1
        
        # DP will return count of all combinations, including "";
        # we want to exclude that case, so:
        return DP(
            tuple(Counter(tiles).values())
        ) - 1

# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 97.58%
# NOTE: Memory 17.10 MB Beats 54.82%

# NOTE: re-ran for challenge:
# NOTE: Runtime 3 ms Beats 98.37%
# NOTE: Memory 18.02 MB Beats 49.32%
