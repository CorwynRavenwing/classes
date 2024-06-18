class Solution:
    def lastRemaining(self, n: int) -> int:
        debug = True
        group = [
            (N, format(N, '04b'))
            for N in [1, n]
        ]
        len_group = n
        binary_n = format(n, 'b')
        print(f'{n=} 0b{binary_n}')
        planned_passes = [
            (
                'X'
                if (i % 2 == 0)
                else 'A'
                if (digit == '1')
                else 'B'
            )
            for i, digit in enumerate(reversed(list(binary_n[1:])))
        ]
        print(f'{" ".join(planned_passes)}')
        power = 0
        step = 2 ** power
        first = 1
        print(
            ' '.join([
                f'{power}:^',
                f'{list(range(first, 6*step, step))[:len_group]}',
                ('...' if len_group > 5 else '\t'),
                f'len={len_group}',
            ])
        )
        for pass_cmd in planned_passes:
            if pass_cmd in ['X', 'A']:
                first += step
            power += 1
            step = 2 ** power
            len_group //= 2
            print(
                ' '.join([
                    f'{power}:{pass_cmd}',
                    f'{list(range(first, 6*step, step))[:len_group]}',
                    ('...' if len_group > 5 else '\t'),
                    f'len={len_group}',
                ])
            )
        return first

# NOTE: a much smarter version
