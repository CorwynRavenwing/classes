class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        def AdividesB(A: int, B: int) -> bool:
            return (B % A == 0)

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

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        print(f'{indexesByValue=}')

        answer = 0
        for value, indexes in indexesByValue.items():
            print(f'Checking {value=}')
            for (i, j) in all_combinations_size_K(indexes, 2):
                if AdividesB(k, i * j):
                    print(f'  [{i},{j}]: YES')
                    answer += 1
                else:
                    print(f'  [{i},{j}]: no')
                    pass
        
        return answer

# NOTE: Acceptance Rate 79.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 143 ms Beats 5.33%
# NOTE: Memory 18.06 MB Beats 12.50%
