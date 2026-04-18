
        def reverse_int(N: int) -> int:
            N_str = f'{N}'
            reverse_str = ''.join(reversed(N_str))
            reverse_N = int(reverse_str)
            print(f'{N} -> {reverse_N}')
            return reverse_N

