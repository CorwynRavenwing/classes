class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        no_dups = []
        prev = None
        for N in nums:
            if prev is None or prev != N:
                no_dups.append(N)
            prev = N
        print(f'{no_dups=}')

        def triwise(iterable):
            a, b = tee(iterable)
            a, c = tee(iterable)
            next(b, None)
            next(c, None)
            next(c, None)
            return zip(a, b, c)
        
        answer = 0
        for (A, B, C) in triwise(no_dups):
            print(f'({A},{B},{C})')
            if A < B < C:
                print(f'  slope up')
            elif A > B > C:
                print(f'  slope down')
            else:
                print(f'  hill or valley')
                answer += 1

        return answer

# NOTE: Acceptance Rate 61.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 17.83%
# NOTE: Memory 17.73 MB Beats 64.58%
