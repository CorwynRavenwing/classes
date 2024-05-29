class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        answer = None

        print(f'before: {len(nums)=}')

        # delete any 1's in the array
        # because (number * 1) is a NOOP
        if 1 in nums:
            while 1 in nums:
                index = nums.index(1)
                # print(f'drop 1 at {index=}')
                del nums[index]
            # add one back, because a single 1 might be necessary
            # (e.g. testcase #100)
            nums.append(1)

        print(f'after: {len(nums)=}')

        # turn any group of three -1's [-1 -1 -1]
        # into a single -1 by deleting the other two
        # because one -1 might be necessary
        # but then a pair of them cancel out
        index = -1
        while -1 in nums:
            try:
                index = nums.index(-1, index + 1)
            except ValueError:
                break
            while nums[index:index + 3] == [-1, -1, -1]:
                del nums[index + 1:index + 3]
                # print(f'delete [-1, -1] at {index + 1}')
                # print(f'during: {len(nums)=}')
        
        print(f'afterer: {len(nums)=}')

        # turn any group of two 0's [0 0]
        # into a single 0 by deleting the second one
        # because one 0 firewalls between groups of numbers
        # but a second, third, etc. adjacent one are irrelevant
        index = -1
        while 0 in nums:
            try:
                index = nums.index(0, index + 1)
            except ValueError:
                break
            while nums[index:index + 2] == [0, 0]:
                del nums[index + 1:index + 2]
                print(f'delete [0] at {index + 1}')
                # print(f'during: {len(nums)=}')
        
        print(f'afterest: {len(nums)=}')
        print(f'{nums=}')

        for i, iVal in enumerate(nums):
            product = iVal
            print(f'i [{i}] {iVal}')
            answer = max(answer, product) if answer is not None else product
            if iVal == 0:
                # product will carry on being zero for any J values
                continue
            for j, jVal in enumerate(nums):
                if i >= j:
                    continue
                print(f'  j [{j}] {jVal}')
                product *= jVal
                fragment = nums[i:j + 1]
                # print(f'    {product=} {fragment=}')
                print(f'    {product=}')
                answer = max(answer, product) if answer is not None else product
                if jVal == 0:
                    # product will carry on being zero for later J values
                    break
        
        return answer

