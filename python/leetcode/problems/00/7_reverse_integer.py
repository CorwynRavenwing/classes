class Solution:
    def reverse(self, x: int) -> int:

        # print(f'Check range: {-(2 ** 31)}, {2 ** 31 - 1}')
        # range: -2147483648, 2147483647

        is_neg = (x < 0)
        if is_neg:
            if x == -2147483648:
                print(f'-MAXINT cannot become positive')
                return 0
            x *= -1
            # x is now positive
        x_str = str(x)
        reversed_x_str = ''.join(list(reversed(x_str)))
        if len(reversed_x_str) >= len('2147483648'):
            if is_neg and reversed_x_str > '2147483648':
                print(f'negative value larger than -MAXINT: {reversed_x_str}')
                return 0
            if not is_neg and reversed_x_str > '2147483647':
                print(f'positive value larger than +MAXINT: {reversed_x_str}')
                return 0
        reversed_x = int(reversed_x_str)
        if is_neg:
            reversed_x *= -1
        return reversed_x

