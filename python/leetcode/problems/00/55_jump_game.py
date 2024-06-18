class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        first = 0
        last = len(nums) - 1
        seen = set()
        positions = [first]
        while positions:
            print(f'L={len(positions)}')
            positions.sort()
            P = positions.pop(-1)
            seen.add(P)
            print(f'  {P=}')
            if P == last:
                print(f'    {last=}')
                return True
            max_jump = nums[P]
            for jump in range(1, max_jump + 1):
                # print(f'    {jump}/{max_jump}')
                Q = P + jump
                if Q == P:
                    print(f'      ={Q}')
                    pass
                elif Q == last:
                    print(f'      {last=} (shortcut)')
                    return True
                elif Q not in seen:
                    # print(f'      +{Q}')
                    positions.append(Q)
                else:
                    # print(f'      -{Q} dup')
                    pass
        return False

