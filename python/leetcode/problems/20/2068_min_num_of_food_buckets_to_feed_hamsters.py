class Solution:
    def minimumBuckets(self, hamsters: str) -> int:

        hamsters = 'x' + hamsters + 'x'
        print(f'{hamsters=}')

        for problem in ('HHH', 'xHH', 'HHx'):
            if problem in hamsters:
                print(f'Impossible!  {problem=}')
                return -1
        
        hamsters = list(hamsters)   # make it a list, therefore mutable

        HAMSTER = 'H'
        FED_HAMSTER = 'F'
        EMPTY = '.'
        DONUT = 'd'
        foods = 0
        for i, H in enumerate(hamsters):
            print(f'{i=} "{H}"', end=': ')
            if H != HAMSTER:
                print(f'  not a hamster')
                continue
            before = hamsters[i - 1]
            after = hamsters[i + 1]
            if before == DONUT:
                print(f'  fed already by PRIOR food')
                hamsters[i] = FED_HAMSTER
                continue
            if after == EMPTY:
                print(f'  add food AFTER')
                foods += 1
                hamsters[i] = FED_HAMSTER
                hamsters[i + 1] = DONUT
                continue
            elif before == EMPTY:
                print(f'  add food BEFORE')
                foods += 1
                hamsters[i - 1] = DONUT
                hamsters[i] = FED_HAMSTER
            else:
                print(f'  FAILED somehow!  {before=} {H=} {after=}')
                return -1

        hamsters = ''.join(hamsters)    # merge into a string again
        print(f'{hamsters=}')
        
        return foods

