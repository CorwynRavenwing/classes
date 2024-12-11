class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        original = tuple(range(n))

        def operation(perm: List[int]) -> List[int]:
            nonlocal n
            assert n == len(perm)
            answer = [
                (
                    perm[i // 2]
                    if (i % 2 == 0)
                    else
                    perm[n // 2 + (i - 1) // 2]
                )
                for i in range(n)
            ]
            return tuple(answer)
        
        arr = original
        ops = 0
        print(f'{ops}: {arr}')
        while True:
            ops += 1
            arr = operation(arr)
            print(f'{ops}: {arr}')
            if arr == original:
                break

        return ops

# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 436 ms Beats 5.19%
# NOTE: Memory 17.92 MB Beats 6.38%
