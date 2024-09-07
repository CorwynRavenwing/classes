class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        # we're going to work the grid inverted
        grid = tuple(zip(*grid))
        # print(f'{grid=}')
        grid = tuple(map(tuple, [map(str, row) for row in grid]))
        # print(f'{grid=}')
        
        usedNumbers = {value for row in grid for value in row}
        print(f'{usedNumbers=}')

        priorRowAnswer = None

        for row in grid:
            # print(f'{row=}')
            length = len(row)
            counts = Counter(row)
            # for N in [0, 1]:
            for N in ['X', 'Y']:
                # insert 0 into count under these two numbers
                # === we will definitely have 2 "most common" answers,
                #   even if one of them is a zero
                counts.setdefault(N, 0)
            # print(f'  {counts=}')
            thisRowAnswer = [
                (number, length - count)
                for (number, count) in counts.most_common()
            ]

            # print(f'  {priorRowAnswer=}')
            # print(f'  {thisRowAnswer=}')

            if priorRowAnswer is None:
                priorRowAnswer = thisRowAnswer
                continue
            
            priorRowAnswer = [
                (
                    thisNumber,
                    min([
                        thisCount + priorCount
                        for (priorNumber, priorCount) in priorRowAnswer 
                        if (priorNumber != thisNumber)
                    ])
                )
                for (thisNumber, thisCount) in thisRowAnswer
            ]
            # print(f'  new    {priorRowAnswer=}')
            priorRowAnswer.sort(
                key=lambda x: x[1]  # sort by score
            )
            # print(f'  sorted {priorRowAnswer=}')
            priorRowAnswer = priorRowAnswer[:2]
            # only need best and runner-up-in-case-best-matches-next-row
            # print(f'  trunc  {priorRowAnswer=}')

        answers = [
            priorCount
            for (priorNumber, priorCount) in priorRowAnswer
        ]
        print(f'{answers=}')

        return answers.pop(0)

# NOTE: Runtime 2529 ms Beats 28.26%
# NOTE: Memory 108.24 MB Beats 5.43%
