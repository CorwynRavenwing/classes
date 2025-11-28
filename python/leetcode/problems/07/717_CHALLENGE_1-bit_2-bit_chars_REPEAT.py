class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        answer = False
        while bits:
            first = bits.pop(0)
            if not first:
                print(f'0')
                answer = True
            else:
                second = bits.pop(0)
                print(f'{first}+{second}')
                answer = False
        return answer

# NOTE: Acceptance Rate 45.5% (easy)

# NOTE: re-created this in the Great Computer Crash incident
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 14.85%
# NOTE: Memory 17.88 MB Beats 40.84%
