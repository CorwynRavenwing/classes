class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        numbers = tuple(range(1, n))
        print(f'{numbers=}')
        total = sum(numbers)
        print(f'{total=}')

        return (-total,) + numbers

# NOTE: Acceptance Rate 76.3% (easy)

# NOTE: Accepted on first attempt!
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 18.08 MB Beats 13.47%
