class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        def diff(i: int) -> int:
            val = arr[i]
            return val - i - 1

        print(f'{arr=}')
        L = 0
        R = len(arr) - 1
        left = diff(L)
        right = diff(R)
        print(f'0 [{L},{R}] = ({left},{right}) T={k}')
        if left >= k:
            print(f'{left=} >= {k=}')
            return k
        if right < k:
            print(f'{right=} < {k=}')
            return (k - right) + arr[R]
        while L + 1 < R:
            M = (L + R) // 2
            mid = diff(M)
            print(f'B [{L},{M},{R}] = ({left},{mid},{right}) T={k}')
            # if mid == k:
            #     print(f'found {M=} {mid=}')
            #     return (k - mid) + arr[M]
            if mid < k:
                print(f'replace left')
                (L, left) = (M, mid)
                continue
            if mid >= k:
                print(f'replace right')
                (R, right) = (M, mid)
                continue
            raise ValueError(f'cant compare {mid=} <=> {k=}')

        print(f'Z [{L},{R}] = ({left},{right}) T={k}')
        # if right < k:
        #     print(f'{right=} < {k=}')
        #     return (k - right) + arr[R]
        if left <= k:
            print(f'{left=} <= {k=}')
            return (k - left) + arr[L]
        
        raise Exception(f'Should not get here {left=} {k=}')

# 44 ms: Beats 92.06% of users with Python3

