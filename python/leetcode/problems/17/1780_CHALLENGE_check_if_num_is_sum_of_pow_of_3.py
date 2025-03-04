class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        def base3tuple(n: int) -> List[int]:
            print(f'b3({n})')
            (Div, Mod) = divmod(n, 3)
            print(f'  {Div=} {Mod=}')
            if Div:
                rest = base3tuple(Div)
            else:
                rest = ()
            return rest + (Mod,)
        
        base3 = base3tuple(n)
        print(f'{base3=}')

        return (2 not in base3)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 14.29%
# NOTE: Memory 17.37 MB Beats 10.20%

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.76 MB Beats 59.96%
# NOTE: same code, infinitely faster
