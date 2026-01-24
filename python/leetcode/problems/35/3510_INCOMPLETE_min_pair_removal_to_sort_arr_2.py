class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        pairs = list(pairwise(nums))
        disorder = [
            (A > B)
            for (A, B) in pairs
        ]
        disCount = Counter(disorder)
        sums = list(map(sum, pairs))

        ordered = list(zip(sums, itertools.count(), pairs))
        ordered.sort()

        steps = 0

        while disCount[True]:
            print(f'\n{steps=}')
            print(f'{pairs=}')
            print(f'{disorder=}')
            print(f'{disCount=}')
            print(f'{sums=}')
            print(f'{ordered=}')
            steps += 1
            minObject = ordered.pop(0)
            print(f'  delete {minObject=}')
            (aSum, aOrder, aPair) = minObject
            print(f'  {aSum=} {aOrder=} {aPair=}')
            (A, B) = aPair
            print(f'  {A=} {B=}')
            # NOTE: need to do all three sets of updates here somehow ...
            break

        print(f'\n{steps=}')
        print(f'{pairs=}')
        print(f'{disorder=}')
        print(f'{disCount=}')
        print(f'{sums=}')
        print(f'{ordered=}')

        return steps

# NOTE: Acceptance Rate 15.5% (HARD)

# NOTE: incomplete

