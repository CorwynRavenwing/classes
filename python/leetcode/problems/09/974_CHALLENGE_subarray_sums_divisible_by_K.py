class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # we reuse some code from #523
        
        mods = [None] * len(nums)
        mods[0] = nums[0] % k
        for i in range(1, len(nums)):
            mods[i] = (mods[i-1] + nums[i]) % k
        # mods = [
        #     sum(nums[:i+1]) % k
        #     for i in range(len(nums))
        # ]
        print(f'{mods=}')
        indexLists = {}
        if 0 in mods:
            indexLists[0] = [-1]
        for index, value in enumerate(mods):
            indexLists.setdefault(value, [])
            indexLists[value].append(index)
        print(f'{indexLists=}')
        answer = 0
        for number, indexes in indexLists.items():
            print(f'{number}: {indexes}')
            for i in range(1, len(indexes)):
                # thisIndex = indexes[i]
                # add 1 array starting at each prior index and ending at this one
                answer += i
                print(f'  +{i=}')
            # could just calculate this one, 1 + 2 + 3 + ... + len(indexes)-1
            # therefore just need counts after all, rather than list of indexes

        return answer

