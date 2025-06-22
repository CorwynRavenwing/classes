class Solution:
    def beautySum(self, s: str) -> int:
        
        partialCounts = []
        running_count = Counter()
        new_object = Counter(running_count)
        partialCounts.append(new_object)
        for char in s:
            running_count += Counter(char)
            new_object = Counter(running_count)
            partialCounts.append(new_object)
            # print(f'{char}: {partialCounts=}')
        # print(f'{partialCounts=}')
        
        beauties = []
        for L, Lcount in enumerate(partialCounts):
            for R, Rcount in enumerate(partialCounts):
                if L >= R:
                    continue
                diffCount = Rcount - Lcount
                counts = tuple(sorted(diffCount.values()))
                # print(f'[{L},{R}]: {counts} {diffCount}')
                # print(f'[{L},{R}]: {counts}')
                if len(counts) < 2:
                    continue
                (A, B) = (counts[0], counts[-1])
                C = B - A
                # print(f'  {C} = {B}-{A}')
                beauties.append(C)
            
        print(f'{beauties=}')

        return sum(beauties)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 9734 ms Beats 16.31%
# NOTE: Memory 20.50 MB Beats 5.13%
