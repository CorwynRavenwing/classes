class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        def dp_rule_1(index: int) -> bool:
            # print(f'  dp_rule_1({index})')
            size = 2
            frag = nums[index:index + size]
            # print(f'    {frag}')
            if size != len(frag):
                # print(f'    (too short)')
                return False
            (A, B) = frag
            if A == B:
                # print(f'    PASS: 2 equal')
                pass
            else:
                # print(f'    not equal')
                return False
            
            return dp(index + size)
        
        def dp_rule_2(index: int) -> bool:
            # print(f'  dp_rule_2({index})')
            size = 3
            frag = nums[index:index + size]
            # print(f'    {frag}')
            if size != len(frag):
                # print(f'    (too short)')
                return False
            (A, B, C) = frag
            if A == B == C:
                # print(f'    PASS: 3 equal')
                pass
            else:
                # print(f'    not equal')
                return False
            
            return dp(index + size)
        
        def dp_rule_3(index: int) -> bool:
            # print(f'  dp_rule_3({index})')
            size = 3
            frag = nums[index:index + size]
            # print(f'    {frag}')
            if size != len(frag):
                # print(f'    (too short)')
                return False
            (A, B, C) = frag
            if A + 1 == B == C - 1:
                # print(f'    PASS: increasing')
                pass
            else:
                # print(f'    not increasing')
                return False
            
            return dp(index + size)
        
        @cache
        def dp(index: int) -> bool:
            # print(f'dp({index})')
            size = 1
            frag = nums[index:index + size]
            if len(frag) == 0:
                # print(f'  (done)')
                return True
            return any([
                dp_rule_1(index),
                dp_rule_2(index),
                dp_rule_3(index),
            ])
        
        return dp(0)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded, Time Exceeded)
# NOTE: Runtime 443 ms Beats 5.19%
# NOTE: Memory 87.16 MB Beats 14.11%
