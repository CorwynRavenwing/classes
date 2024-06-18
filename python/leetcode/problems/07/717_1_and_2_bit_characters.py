class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        while bits:
            if bits == [0]:
                return True
            
            B = bits[0]
            if B == 0:
                # print(f"  {B} delete one bit {bits[:1]}")
                bits = bits[1:]
            elif B == 1:
                # print(f"  {B} delete two bits {bits[:2]}")
                bits = bits[2:]
        
        # print("exited while loop, no bits left")
        return False

