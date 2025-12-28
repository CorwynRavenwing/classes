class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        print(f'{total_apples=}')
        print(f'{capacity=}')
        sums = tuple(accumulate(capacity))
        print(f'{sums=}')
        index = bisect_left(sums, total_apples)
        print(f'{index=}')

        return index + 1

# NOTE: Acceptance Rate 70.8% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.33 MB Beats 96.18%
