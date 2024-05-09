class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        print(f"{ranges} [{left},{right}]")

        for N in range(left, right+1):
            N_found = False
            for R in ranges:
                (S, E) = R
                if S <= N <= E:
                    print(f'{N} in range {R}')
                    N_found = True
                    break
                    # next N
            if not N_found:
                print(f'{N} not in any ranges')
                return False
        
        print("All numbers found in a range")
        return True

