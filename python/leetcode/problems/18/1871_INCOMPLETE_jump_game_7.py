class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if s[-1] != '0':
            return False
        
        reachable_ranges = [(0,0)]
        while reachable_ranges:
            (A, B) = reachable_ranges.pop(0)
            # print(f'Scanning from {A} to {B}')
            (rA, rB) = (None, None)
            for I in range(A, B + 1):
                if I == len(s) - 1:
                    print(f'  {I=} SUCCESS!')
                    return True
                elif I >= len(s):
                    print(f'  {I=} OOB')
                    return False
                if s[I] != '0':
                    # print(f'  {I=} blocked')
                    continue
                Jmin = I + minJump
                Jmax = I + maxJump
                if rA is None or rB is None:
                    # print(f'  New range {(Jmin, Jmax)=}')
                    (rA, rB) = (Jmin, Jmax)
                elif rA <= Jmin <= rB <= Jmax:
                    # print(f'  Merge ranges {(rA, rB)=} {(Jmin, Jmax)=}')
                    rB = Jmax
                else:
                    # print(f'  Separate ranges {(rA, rB)=} {(Jmin, Jmax)=}')
                    reachable_ranges.append((rA, rB))
                    (rA, rB) = (Jmin, Jmax)
            if rA and rB:
                # print(f'  Store range {(rA, rB)=}')
                reachable_ranges.append((rA, rB))
        return False
# NOTE: Time Limit Exceeded error for large inputs
