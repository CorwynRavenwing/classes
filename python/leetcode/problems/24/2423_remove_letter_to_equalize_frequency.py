from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        freq1 = Counter(word)
        print(f'{freq1=}')

        if len(freq1) == 1:
            print("remove 1 from the only group")
            return True
        
        freq2 = Counter(freq1.values())
        print(f'{freq2=}')

        if len(freq2) == 1:
            keys2 = list(freq2.keys())
            if keys2.pop() == 1:
                print("remove 1 that has a freq of 1")
                return True
        
        if len(freq2) != 2:
            print("either 0, 1, or 3+ groups: impossible")
            return False

        (A, B) = sorted(freq2.items())
        print(f'{A=} {B=}')

        (A0, A1) = A
        (B0, B1) = B

        if A0 == (B0 - 1):
            if B1 == 1:
                print("remove 1 from the group that is 1 freq higher than the others")
                return True
        
        if (1,1) in [A, B]:
            print("remove the only member of the group that has a freq of 1")
            return True
        
        print("impossible")
        return False

