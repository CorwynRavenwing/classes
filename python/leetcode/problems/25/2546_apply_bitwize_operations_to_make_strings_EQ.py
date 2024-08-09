class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:

        if s == target:
            print(f'Yes: already equal')
            return True
        
        countS = Counter(s)
        countT = Counter(target)
        print(f'{countS=}')
        print(f'{countT=}')

        if (countS['1'] == 0):
            print(f'No: only zeros in source')
            return False

        if (countT['1'] == 0):
            print(f'No: only zeros in target')
            return False
        
        print(f'Yes: all other cases')
        return True
# NOTE: Runtime 80 ms Beats 15.91%
# NOTE: Memory 17.65 MB Beats 17.05%
