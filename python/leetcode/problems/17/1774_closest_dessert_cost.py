class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        possible = set(baseCosts)
        for T in toppingCosts:
            newpossible = set()
            for P in possible:
                newpossible.add(P + T)     # add 1 scoop
                newpossible.add(P + T + T) # add 2 scoops
            possible |= newpossible   # merge sets

        print(f'{possible=}')

        best_so_far = None
        best_distance = None
        for P in possible:
            print(f'{P=}')
            distance = abs(P - target)
            print(f'  {distance=}')
            if (best_distance is None) or (best_distance > distance):
                best_distance = distance
                best_so_far = P
                print(f'    new best')
            if best_distance == distance and best_so_far > P:
                best_so_far = P
                print(f'    new lower')
        
        return best_so_far

