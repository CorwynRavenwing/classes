class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        once = set()
        twice = set()
        
        i = 0
        for j in range(len(nums)):
            jVal = nums[j]
            print(f'{i=} {j=} {jVal=}')
            if jVal not in once:
                if i != j:
                    nums[i] = jVal
                i += 1
                once.add(jVal)
                print(f'  x1')
                continue
            elif jVal not in twice:
                if i != j:
                    nums[i] = jVal
                i += 1
                twice.add(jVal)
                print(f'  x2')
                continue
            else:
                # DO NOT copy value here!
                # DO NOT i++ here!
                print(f'  SKIP')
                continue
        return i

# NOTE: could do this without the "once" and "twice" sets, due to
# the non-decreasing order of the input set.
