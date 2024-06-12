class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [min(nums) - 100] + nums + [max(nums) + 100]
        print(f'{nums}')
        order = [
            '+' if (A <= B) else '-'
            for (A, B) in zip(nums, nums[1:])
        ]
        print(f'{order}')
        if '-' not in order:
            # what if we don't have to alter anything?
            return True
        
        counts = Counter(order)
        print(f'{counts=}')
        if counts['-'] == 1:
            index = order.index('-')
            assert index != 0
            group = nums[index-1:index+3]
            print(f'{group=}')
            (A, B, C, D) = group
            if A <= C:
                print(f'change {B=} to be somewhere in {A}..{C}')
                return True
            elif B <= D:
                print(f'change {C=} to be somewhere in {B}..{D}')
                return True
            else:
                print(f'no room in in {A=}..{C=} to put {B=}')
                print(f'no room in in {B=}..{D=} to put {C=}')
                return False
        
        print(f'more than one decrease')
        return False

