class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        TERM = 'X'
        QUERY = '?'
        DOT = '.'
        RIGHT = 'R'
        LEFT = 'L'
        STOP = '|'
        dominoes = TERM + dominoes + TERM
        print(f'PD():')
        thisRow = tuple(dominoes)
        while True:
            print(f'this: {"".join(thisRow)}')
            nextRow = [
                (
                    QUERY
                    if D == DOT
                    else D
                )
                for D in thisRow
            ]

            while QUERY in nextRow:
                index = nextRow.index(QUERY)
                before = thisRow[index-1]
                after = thisRow[index+1]
                fromLeft = (before == RIGHT)
                fromRight = (after == LEFT)
                toLeft = (before == LEFT)
                toRight = (after == RIGHT)
                if fromLeft and fromRight:  # R.L
                    # print(f'  {index=} FL+FR')
                    nextRow[index] = STOP   # R|L
                elif fromLeft:              # R..
                    # print(f'  {index=} FL')
                    nextRow[index] = RIGHT  # RR.
                elif fromRight:             # ..L
                    # print(f'  {index=} FR')
                    nextRow[index] = LEFT   # .LL
                elif toLeft:                # L?.
                    # print(f'  {index=} TL')
                    nextRow[index] = DOT    # L..
                elif toRight:               # .?R
                    # print(f'  {index=} TR')
                    nextRow[index] = DOT    # ..R
                elif (before in [DOT,TERM]) and (after in [DOT,TERM]):  # .?.
                    # print(f'  {index=} D,T')
                    nextRow[index] = DOT                                # ...
                else:
                    raise Exception(f"Weird, {before=} this='{dominoes[index]}' {after=}")
            
            print(f'next: {"".join(nextRow)}')
            if thisRow == nextRow:
                print(f'... Done')
                break
            thisRow = nextRow

        assert thisRow[0] == thisRow[-1] == TERM
        del thisRow[0]
        del thisRow[-1]
        result = [
            (
                DOT
                if D == STOP
                else D
            )
            for D in thisRow
        ]
        return ''.join(result)

# NOTE: times out on large inputs
