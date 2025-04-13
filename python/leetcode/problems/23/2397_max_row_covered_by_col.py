class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        
        M = len(matrix)
        N = len(matrix[0])

        rowSets = [
            {
                col
                for col, value in enumerate(row)
                if value == 1
            }
            for row in matrix
        ]
        print(f'{rowSets=}')

        def pattern_after_value(pattern: List[int], value: int) -> List[int]:
            assert value in pattern
            index = pattern.index(value)
            return pattern[index + 1:]

        # GENERATOR
        def all_combinations_size_K(pattern: List[int], k: int) -> List[List[int]]:
            if k == 0:
                yield ()
                return

            for D in sorted(set(pattern)):
                remainder = pattern_after_value(pattern, D)
                # print(f'  {pattern=}: {D} + {remainder}')
                for value in all_combinations_size_K(remainder, k - 1):
                    yield (D,) + value
            return

        all_columns = tuple(range(N))
        
        coverage = [
            [
                (
                    1
                    if len(row - columns) == 0
                    else 0
                )
                for row in rowSets
            ]
            for columns in map(set, all_combinations_size_K(all_columns, numSelect))
        ]
        print(f'{coverage=}')
        coverage_count = tuple(map(sum, coverage))
        print(f'{coverage_count=}')

        return max(coverage_count)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 21 ms Beats 34.04%
# NOTE: Memory 18.08 MB Beats 17.73%
# NOTE: second run:
# NOTE: Runtime 25 ms Beats 27.66%
# NOTE: Memory 18.33 MB Beats 5.67%
