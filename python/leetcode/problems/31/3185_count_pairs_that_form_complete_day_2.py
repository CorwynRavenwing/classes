class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        # we borrow some code from #3184:

        mods = [H % 24 for H in hours]
        print(f'{mods=}')

        counts = Counter(mods)
        print(f'{counts=}')

        answer = 0
        for H, Hcount in counts.items():
            print(f'{H=} {Hcount=}')
            I = -H % 24
            Icount = counts[I]
            same = (H == I)
            print(f'  {I=} {Icount=} {same=}')
            if same:
                print(f'    SAME: {Hcount * (Icount - 1) / 2=}')
                answer += Hcount * (Icount - 1)     # also count this twice
            elif Icount:
                print(f'    DIFF: {Hcount * Icount / 2=}')
                answer += Hcount * Icount   # gets counted twice
                # can't divide by 2 here: counts might both be odd
            else:
                print(f'    SKIP: {Icount=}')
        
        answer //= 2    # fix "counted twice" issue

        return answer

# NOTE: Accepted with code from Version 1 #3184
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 977 ms Beats 62.62%
# NOTE: Memory 68.80 MB Beats 44.63%
