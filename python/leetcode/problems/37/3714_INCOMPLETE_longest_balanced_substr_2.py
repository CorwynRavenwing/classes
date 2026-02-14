class Solution:
    def longestBalanced(self, s: str) -> int:
        
        MATCH = lambda C, L: tuple([(1 if C == X else 0) for X in L])
        ACC = lambda L: (0,) + tuple(accumulate(L))

        As = MATCH('a', s)
        Bs = MATCH('b', s)
        Cs = MATCH('c', s)
        # print(f'{As=}')
        # print(f'{Bs=}')
        # print(f'{Cs=}')

        Asums = ACC(As)
        Bsums = ACC(Bs)
        Csums = ACC(Cs)
        # print(f'{Asums=}')
        # print(f'{Bsums=}')
        # print(f'{Csums=}')

        def run_of_1s(L: List[int]) -> int:
            block = ''.join([('1' if X else '0') for X in L])
            # print(f'{L=}')
            # print(f'  {block=}')
            parts = block.split('0')
            # print(f'  {parts=}')
            lens = tuple(map(len, parts))
            # print(f'  {lens=}')
            return max(lens)
        
        # print(f'{run_of_1s(As)=}')
        # print(f'{run_of_1s(Bs)=}')
        # print(f'{run_of_1s(Cs)=}')

        DIFFS = lambda A, B: tuple([(b - a) for (a, b) in zip(A, B)])

        BminusA = DIFFS(Asums, Bsums)
        CminusA = DIFFS(Asums, Csums)
        CminusB = DIFFS(Bsums, Csums)
        print(f'{BminusA=}')
        print(f'{CminusA=}')
        print(f'{CminusB=}')

        def indexes_by_value(nums: List[int]) -> Dict[int,List[int]]:
            indexesByValue = {}
            for index, value in enumerate(nums):
                indexesByValue.setdefault(value, [])
                indexesByValue[value].append(index)
            return indexesByValue

        def check_pair(XminusY: List[int], Z: List[int]) -> int:
            print(f'{XminusY=}')
            XminusY_markZ = tuple([
                'Z' if Z else XY
                for (XY, Z) in zip(XminusY, (0,) + Z)
            ])
            print(f'{XminusY_markZ=}')
            XminusY_noZ = tuple([
                XY
                for XY in XminusY_markZ
                if XY != 'Z'
            ])
            print(f'{XminusY_noZ=}')
            IBV = indexes_by_value(XminusY_noZ)
            print(f'  {IBV=}')
            answers = [
                indexList[-1] - indexList[0]
                for value, indexList in IBV.items()
                if len(indexList) > 1
            ]
            print(f'  {answers=}')
            return max(answers, default=0)

        print(f'{check_pair(BminusA, Cs)=}')
        print(f'{check_pair(CminusA, Bs)=}')
        print(f'{check_pair(CminusB, As)=}')

        # def check_pair(A: List[int], B: List[int]) -> int:
        #     xxx

        return -9999

# NOTE: Acceptance Rate 21.4% (medium)

# NOTE: Incomplete: wrong answer
