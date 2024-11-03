class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # we borrow some code from #3185:

        mods = [T % 60 for T in time]
        print(f'{mods=}')

        counts = Counter(mods)
        print(f'{counts=}')

        answer = 0
        for T, Tcount in counts.items():
            print(f'{T=} {Tcount=}')
            I = -T % 60
            Icount = counts[I]
            same = (T == I)
            print(f'  {I=} {Icount=} {same=}')
            if same:
                print(f'    SAME: {Tcount * (Icount - 1) / 2=}')
                answer += Tcount * (Icount - 1)     # also count this twice
            elif Icount:
                print(f'    DIFF: {Tcount * Icount / 2=}')
                answer += Tcount * Icount   # gets counted twice
                # can't divide by 2 here: counts might both be odd
            else:
                print(f'    SKIP: {Icount=}')

        answer //= 2    # fix "counted twice" issue

        return answer

# NOTE: re-used entire previous version, changing 24->60 and var names
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 17 ms Beats 82.49%
# NOTE: Memory 20.78 MB Beats 77.83%
