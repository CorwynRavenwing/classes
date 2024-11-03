class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShipInDdaysWithTargetCapacity(target: int) -> bool:

            DEBUG = False

            if DEBUG: print(f'test({target}):')
            days_required = 1
            ship_load = 0
            for W in weights:
                if ship_load + W > target:
                    # will not fit on current ship
                    if DEBUG: print(f'  ... day #{days_required} {ship_load}')
                    days_required += 1
                    ship_load = 0
                    if days_required > days:
                        if DEBUG: print(f'  FAIL')
                        return False

                if DEBUG: print(f'  +{W}')
                ship_load += W
                
            # Here, True is good and happens for higher numbers
            if DEBUG: print(f'  last day #{days_required} {ship_load}')
            if DEBUG: print(f'  SUCCESS')
            return True

        DEBUG = True

        L = max(weights)        # can just barely carry heaviest package by itself
        # L = max(weights) - 1    # cannot quite carry heaviest package by itself
        # L = 0                   # cannot carry anything
        left = canShipInDdaysWithTargetCapacity(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = sum(weights)        # can carry all packages together in one load
        right = canShipInDdaysWithTargetCapacity(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canShipInDdaysWithTargetCapacity(M)
            if DEBUG: print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                if DEBUG: print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                if DEBUG: print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 195 ms Beats 43.95%
# NOTE: Memory 21.29 MB Beats 85.27%
