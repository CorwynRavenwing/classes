class Solution:

    # we borrow some code from #875:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatingTime(speed: int) -> int:
            nonlocal piles
            print(f'  {speed=}')
            time = 0
            for P in piles:
                floor = P // speed
                ceil = floor + (
                    0
                    if (P % speed) == 0
                    else 1
                )
                # print(f'  {P}: {ceil}')
                time += ceil
            print(f'    total {time=}')
            return time

        def eatingTimeOk(speed: int) -> bool:
            nonlocal h
            time = eatingTime(speed)
            ok = time <= h
            # if ok:
            #     print(f'  <= {h} (OK)')
            # else:
            #     print(f'  > {h} (not ok)')
            return ok

        left = 1
        right = max(piles)
        print(f'0: {left} --- {right}')
        if eatingTimeOk(left):
            return left
        if not eatingTimeOk(right):
            print(f'Error: eating speed of {right} is not okay')
            return -88888
        while left + 1 < right:
            mid = (left + right) // 2
            print(f'B: {left} {mid} {right}')
            if eatingTimeOk(mid):
                print(f'      okay, move right')
                right = mid
            else:
                print(f'      too slow, move left')
                left = mid
        print(f'Z: {left} --- {right}')
        return right

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        return self.minEatingSpeed(nums, threshold)

# NOTE: re-used entire previous version, with wrapper code
# NOTE: Accepted on second Run (first was function-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 163 ms Beats 13.62%
# NOTE: Memory 21.92 MB Beats 53.80%
