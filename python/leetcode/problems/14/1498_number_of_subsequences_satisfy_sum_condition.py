class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        mod = 10 ** 9 + 7

        pow_2_mod_cache = {}
        def pow_2_mod(N):
            # print(f'call pow_2_mod({N}):')
            nonlocal pow_2_mod_cache
            if N in pow_2_mod_cache:
                # print(f'  cache hit {N}')
                return pow_2_mod_cache[N]
            elif N == 0:
                pow_2_mod_cache[N] = (2 ** 0) % mod
                # print(f'  cache miss 0 {N}')
                return pow_2_mod_cache[N]
            else:
                one_down = pow_2_mod(N-1)
                pow_2_mod_cache[N] = (2 * one_down) % mod
                # print(f'  cache miss N {N}')
                return pow_2_mod_cache[N]

        nums.sort()
        answer = 0
        for low_pos, low_val in enumerate(nums):
            # print(f'low_val: nums[{low_pos}]={low_val}')
            high_val = target - low_val
            if high_val < low_val:
                print(f"  {low_pos=}: {high_val=} < {low_val}")
                print("    ALL OTHER, later numbers will be worse")
                break
            high_pos = bisect.bisect_right(nums, high_val, low_pos)
            # print(f'  [{high_pos=}] =? {high_val=}')
            section = nums[low_pos:high_pos]
            # print(f'   nums[{low_pos}:{high_pos}] = {section}')
            if section:
                # print(f'    + 2 ** {len(section) - 1}')
                # print(f'    + 2 ** {len(section) - 1} = {2 ** (len(section) - 1)}')
                answer += pow_2_mod(len(section) - 1)
                answer %= mod

        return answer

