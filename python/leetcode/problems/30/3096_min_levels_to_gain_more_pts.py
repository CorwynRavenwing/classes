class Solution:
    def minimumLevels(self, possible: List[int]) -> int:

        scores = [
            (1 if P == 1 else -1 if P == 0 else None)
            for P in possible
        ]
        # print(f'{scores=}')

        sums = tuple(accumulate(scores))
        # print(f'{sums=}')

        total = sums[-1]
        leave_bob_one = sums[:-1]
        for index, S in enumerate(leave_bob_one):
            # print(f'[{index}] {S+S=} {total}')
            if S + S > total:
                print(f'[{index}] {S+S=} {total}')
                return index + 1
        return -1

# NOTE: Runtime 1978 ms Beats 48.88%
# NOTE: Memory 22.96 MB Beats 11.18%
