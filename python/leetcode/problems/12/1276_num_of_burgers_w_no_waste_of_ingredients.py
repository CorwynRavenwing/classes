class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:

        DEBUG = False

        (J, S) = (0, 0)

        if tomatoSlices % 2 != 0:
            print(f'Odd {tomatoSlices=}')
            return []
        
        # now use pairs of tomato slices:
        tomatoSlices //= 2
        if DEBUG: print(f'DEBUG: start {J=} {S=} {tomatoSlices=} {cheeseSlices=}')

        while tomatoSlices > cheeseSlices > 0:
            extras = tomatoSlices - cheeseSlices
            J += extras
            tomatoSlices -= 2 * extras
            cheeseSlices -= extras
            if DEBUG: print(f'DEBUG: jumbo {J=} {S=} {tomatoSlices=} {cheeseSlices=}')
        
        while tomatoSlices == cheeseSlices > 0:
            same = cheeseSlices
            S += same
            tomatoSlices -= same
            cheeseSlices -= same
            if DEBUG: print(f'DEBUG: small {J=} {S=} {tomatoSlices=} {cheeseSlices=}')

        if tomatoSlices or cheeseSlices:
            if DEBUG: print(f'DEBUG: nope! {J=} {S=} {tomatoSlices=} {cheeseSlices=}')
            print(f'Jumbo = {J}\bSmall = {S}\n\t{tomatoSlices=}\n\t{cheeseSlices=}')
            return []
        
        return (J, S)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Time Limit Exceeded)
# NOTE: Runtime 3 ms Beats 8.43%
# NOTE: Memory 16.71 MB Beats 13.61%
