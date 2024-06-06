class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            (L, R) = (i-1, i+1)
            if L < 0:
                L = 0
            while True:
                group = nums[L:R+1]
                print(f'{i=} {group=} {len(group)=}')
                if len(group) == 3:
                    (A, B, C) = group
                    if A <= B <= C:
                        print(f'  increasing: delete')
                        del nums[i]
                    elif A >= B >= C:
                        print(f'  decreasing: delete')
                        del nums[i]
                    else:
                        print(f'  wiggle: keep')
                        break
                elif len(group) == 2:
                    (A, B) = group
                    if A == B:
                        print(f'  equal: delete')
                        del nums[i]
                    else:
                        print(f'  wiggle: keep')
                        break
                else:
                    break
        print(f'{nums=}')
        return len(nums)

