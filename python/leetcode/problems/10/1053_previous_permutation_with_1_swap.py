class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        def R(A: List[int]) -> List[int]:
            return list(reversed(A))
        
        print(f'{arr=}')

        rArr = R(arr)
        print(f'{rArr=}')

        rMin = [None] * len(rArr)
        rMin[0] = rArr[0]
        for i in range(1, len(rArr)):
            # print(f'set rmin[{i}] to min of rArr[{i}] and rMin[{i-1}]')
            rMin[i] = min(rArr[i], rMin[i - 1])
        print(f'{rMin=}')

        rMax = [None] * len(rArr)
        rMax[0] = rArr[0]
        for i in range(1, len(rArr)):
            rMax[i] = max(rArr[i], rMax[i - 1])
        print(f'{rMax=}')

        (A, B) = (None, None)
        print(f'Finding A:')
        for (i, nArr, nMin) in zip(range(len(rArr)), rArr, rMin):
            print(f'  {i=}: ({nArr}, {nMin})')
            if nArr > nMin:
                A = i
                print(f'    found {A=}')
                break
        assert A != 0
        if A is None:
            print(f'No swap possible')
            return arr
        
        bVal = rArr[A]
        print(f'finding B: (< {bVal=}) in {rArr[:A]}')
        bMax = float('-inf')
        for i, nArr in reversed(list(enumerate(rArr[:A]))):
            print(f'  ({i=}, {nArr=})')
            if bMax < nArr < bVal:
                B = i
                bMax = nArr
                print(f'    found {B=} ({bMax})')
                # don't break here

        if B == float('-inf'):
            print(f'Broken; {B=}')
            return arr
        
        print(f'doing swap of {A},{B}:')
        (rArr[A], rArr[B]) = (rArr[B], rArr[A])
        print(f'{rArr=}')

        answer = R(rArr)
        return answer

