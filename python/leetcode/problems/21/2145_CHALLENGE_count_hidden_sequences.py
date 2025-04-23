class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        source = [0] + differences
        target = list(accumulate(source))
        (MIN, MAX) = min(target), max(target)
        print(f'{target=}')
        print(f'{MIN=} {MAX=}')
        diff = (lower - MIN)
        topValue = MAX + diff
        print(f'{diff=} {topValue=} ({upper=})')

        answer = upper - topValue + 1
        if answer < 0:
            return 0
        else:
            return answer

# NOTE: Runtime 844 ms Beats 75.15%
# NOTE: Memory 31.79 MB Beats 31.52%

# NOTE: re-ran for challenge:
# NOTE: Runtime 81 ms Beats 66.67%
# NOTE: Memory 33.58 MB Beats 6.06%
# NOTE: 10x faster, slightly better percentage
# NOTE: same memory, much worse percentage
