class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        seen = set()
        arrSet = set(arr)
        maxlen = 0
        Min = arr[0]
        Max = arr[-1]
        for i, A in enumerate(arr):
            if i == 0:
                continue
            # print(f'[{i}] {A}')
            for j, B in enumerate(arr):
                if i >= j:
                    continue
                # print(f'  [{j}] {B}')
                pair = (A, B)
                if pair in seen:
                    # print(f'    (seen)')
                    continue
                else:
                    seen.add(pair)
                diff = (B - A)
                if diff >= A:
                    # print(f'  {B}-{A} = {diff} >= A')
                    continue
                if diff < Min:
                    # print(f'  {B}-{A} = {diff} < {Min}')
                    continue
                elif diff not in arrSet:
                    # print(f'  {B}-{A} = {diff}, not in array')
                    continue

                length = 3      # 1. B-A; 2. A; 3. B
                maxlen = max(maxlen, length)
                (a, b) = (A, B)
                c = a + b
                if c > Max:
                    # print(f'    TOO HIGH: {A}+{B}={c} > {Max}')
                    # all later B values will be worse: next A
                    break
                # print(f'    [1] {diff}')
                # print(f'    [2] {a}')
                # print(f'    [3] {b}')
                while c in arrSet:
                    length += 1
                    print(f'    [{length}] {a}+{b} -> {c}')
                    pair = (b, c)
                    seen.add(pair)
                    (a, b) = pair
                    c = a + b
                # print(f'  Total {length=}')
                maxlen = max(maxlen, length)
        # print(f'{maxlen=}')
        return maxlen if maxlen > 2 else 0

# NOTE: re-ran for challenge:
# NOTE: Runtime 3993 ms Beats 5.96%
# NOTE: Memory 80.13 MB Beats 5.96%
