class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            # nothing to change: swap char 0 with itself
            return True
        
        pairs = tuple(zip(s1, s2))
        print(f'{pairs}')
        differences = tuple(
            (A, B)
            for (A, B) in pairs
            if A != B
        )
        print(f'{differences}')
        if len(differences) != 2:
            return False
        
        (D1, D2) = differences
        (D1a, D1b) = D1
        (D2a, D2b) = D2
        print(f"{D1a}/{D2b} {D1b}/{D2a}")
        if D1a != D2b or D1b != D2a:
            return False
        
        return True

