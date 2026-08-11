class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for check in range(n, n + 10):
            check_digits = tuple(
                map(
                    int,
                    str(check)
                )
            )
            check_prod = math.prod(check_digits)
            check_div = (check_prod % t) == 0
            print(f'{check=} {check_digits} {check_prod} {check_div}')
            if check_div:
                return check
        
        print(f'did not find a match')
        assert "that" == "cant happen"

# NOTE: Acceptance Rate 73.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 2.39%
# NOTE: Memory 19.45 MB Beats 11.95%
