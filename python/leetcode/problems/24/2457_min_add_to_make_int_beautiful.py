class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        def digitSum(n: int) -> int:
            return sum(
                map(
                    int,
                    tuple(
                        str(n)
                    )
                )
            )

        DS = digitSum(n)
        print(f'{n=} {DS=} {target=}')
        x = 0
        power = 1
        while DS > target:
            checkdigit = (n // power) % 10
            addition = (10 - checkdigit) if checkdigit else 0
            print(f'  {checkdigit=} {addition=} {power=}')
            addition *= power
            x += addition
            n += addition
            power *= 10
            DS = digitSum(n)
            print(f'{n=} {DS=} {target=}')

        return x
# NOTE: correct first run; accepted first submit
# NOTE: Runtime 38 ms Beats 34.04%
# NOTE: Memory 16.44 MB Beats 74.47%
