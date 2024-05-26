class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == k:
            # shortcut
            return arr
        
        low_left = bisect.bisect_left(arr, x)
        high_left = bisect.bisect_right(arr, x)
        print(f'A: {low_left=} {high_left=}')

        low_right = low_left - k
        high_right = high_left + k

        low_right = max(low_right, 0)
        high_right = min(high_right, len(arr) - 1)

        # not sure I have these the right way around:
        high_right = max(high_right, low_right + k)
        low_right = min(low_right, high_right - k)

        high_right = min(high_right, len(arr) - 1)

        if low_right < 0:
            if k <= len(arr):
                print(f'too few values!')
                print(f'{len(arr)=} {k=} {len(arr) < k}')
                return arr
            else:
                print(f'low_right < 0 but plenty of values ?!')
                print(f'{low_right=} {high_right=}')
                print(f'{len(arr)=} {k=} {len(arr) < k}')
                return arr

        length_right = high_right - low_right + 1

        print(f'{k=} {arr[low_right:high_right+1]=}')
        print(f'{high_right}-{low_right}+1={length_right}')
        assert len(arr[low_right:high_right+1]) == length_right
        
        low_data = arr[low_right]
        high_data = arr[high_right]
        print(f'{low_data} <= {x} <= {high_data} ?')
        low_diff = abs(low_data - x)
        high_diff = abs(high_data - x)
        print(f'{low_diff} .. {high_diff} ?')

        L = 0
        length_left = high_left - low_left + 1
        R = max(low_diff, high_diff)
        print(f'[{L},{R}] {k=} len={length_left}..{length_right}')
        while L + 1 < R:
            M = (L + R) // 2
            low_mid = bisect.bisect_left(arr, x - M)
            high_mid = bisect.bisect_left(arr, x + M)
            high_mid = min(high_mid, len(arr) - 1)
            print(f'bisect: {M=} {x-M}..{x+M}')
            length_mid = high_mid - low_mid
            print(f'[{L},{M},{R}] {k=} {low_mid}..{high_mid} len={length_mid}')
            print(f'fragment = {arr[low_mid:high_mid+1]}')
            # if length_mid == k:
            #     print(f'FOUND! {length_mid=} {k=}')
            #     return arr[low_mid:high_mid+1]
            if length_mid <= k:
                # too short: replace "low"
                (L, length_left) = (M, length_mid)
                (low_left, high_left) = (low_mid, high_mid)
                continue
            elif length_mid > k:
                # too long: replace "high"
                (R, length_right) = (M, length_mid)
                (low_right, high_right) = (low_mid, high_mid)
                continue

        print(f'[{L},{R}] {k=} len={length_left}..{length_right}')
        print(f'left:  {arr[low_left:high_left+1]}')
        print(f'right: {arr[low_right:high_right+1]}')

        while len(arr[low_right:high_right+1]) > k:
            low_diff = abs(x - arr[low_right])
            high_diff = abs(x - arr[high_right])
            print(f'low:  {arr[low_right]} ({low_diff})')
            print(f'high: {arr[high_right]} ({high_diff})')
            if low_diff > high_diff:
                print(f'low++')
                low_right += 1
            else:
                # either "high" is lower,
                # or they're equal, in which case remove the higher
                print(f'high--')
                high_right -= 1

        print(f'length is now {k}')
        return arr[low_right:high_right+1]

