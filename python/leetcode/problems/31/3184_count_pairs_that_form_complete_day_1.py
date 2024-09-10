class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:

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

# NOTE: Accepted on first Submit
# NOTE: Runtime 67 ms Beats 8.28%
# NOTE: Memory 16.60 MB Beats 59.62%
