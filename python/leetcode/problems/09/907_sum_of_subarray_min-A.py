class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        size = len(arr)

        def get_range_given_blocked(index: int, blocked: set[int]) -> Tuple[int,int]:
            nonlocal size
            L = index
            while L > 0:
                if L - 1 in blocked:
                    break
                L -= 1
            R = index
            while R + 1 < size:
                if R + 1 in blocked:
                    break
                R += 1
            # print(f'[{index}] {blocked} -> {(L, R)}')
            return (L, R)

        def get_NextTE_pairs() -> List[Tuple[int,int]]:
            nonlocal arr
            nonlocal size
            num_index_pairs = [
                (N, index)
                for (index, N) in enumerate(arr)
            ]
            num_index_pairs.sort()
            # print(f'{num_index_pairs=}')
            range_blocked = set()
            ranges = {}
            for NIP in num_index_pairs:
                (N, i) = NIP
                # print(f'{N}: [{i}] -> {range_blocked}')
                ranges[i] = get_range_given_blocked(i, range_blocked)
                range_blocked.add(i)
            # print(f'{ranges=}')
            answers = [
                ranges[i]
                for i in range(size)
            ]
            # print(f'{answers=}')
            return answers

        NLE_pairs = get_NextTE_pairs()
        print(f'{NLE_pairs=}')

        answers = []
        for i, A in enumerate(arr):
            (L, R) = NLE_pairs[i]
            # print(f'{i=} {A=} {L=} {R=}')
            subarrays_where_i_am_minimum = (
                (i - L + 1) * (R - i + 1)
            )
            print(f'+ {A} * {subarrays_where_i_am_minimum}')
            answers.append(
                (A * subarrays_where_i_am_minimum) % mod
            )
        print(f'{answers=}')
        return sum(answers) % mod

# NOTE: works for reasonable-sized inputs, TLE for large inputs
