class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # we borrow some code from #2799:

        everything = len(Counter(nums))
        target = k
        LEN = len(nums)
        answer = 0
        L = 0
        R = 0

        def ExpandRight() -> bool:
            nonlocal L, R, count
            # print(f'  ExpandRight()')
            R += 1
            try:
                count[nums[R]] += 1
            except IndexError:
                # print(f'    FAIL')
                return False
            # print(f'    SUCCEED')
            return True

        def ContractLeft() -> bool:
            nonlocal L, R, count
            # print(f'  ContractLeft()')
            L += 1
            R = L
            count = Counter()   # clear prior window's data
            try:
                count[nums[R]] += 1
            except IndexError:
                # print(f'    FAIL')
                return False
            # print(f'    SUCCEED')
            return True

        count = Counter()
        count[nums[R]] += 1
        while 0 <= L <= R <= LEN:
            # print(f'[{L}..{R}]: {answer=} {len(count)}/{k}:{count=}')
            if len(count) == target:
                if target < everything:
                    answer += 1
                    if ExpandRight():
                        continue
                else:
                    answer += LEN - R

                if not ContractLeft():
                    break
                continue

            elif len(count) < target:
                if not ExpandRight():
                    break
                    # no smaller window will work, then
            
            elif len(count) > target:
                if not ContractLeft():
                    break

        return answer

# NOTE: Acceptance Rate 64.4% (HARD)
# NOTE: Time Limit Exceeded for large inputs
