class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        # Not sure I want to go into bit-manipulation here
        # rather than set membership
        # letters = 'ABCDEF'
        # letter2bit = lambda L: 1 << (letters.index(L))
        
        beAfter = {}
        beAbove = {}
        for (A, B, C) in allowed:
            beAfter.setdefault(A, set())
            beAfter[A].add(B)
            pair = (A,B)
            beAbove.setdefault(pair, set())
            beAbove[pair].add(C)
            # technically, beAfter is just a Dict[str,set] of beAbove.keys()

        print(f'{beAfter=}')
        print(f'{beAbove=}')

        bottomRow = tuple(bottom)
        print(f'{bottomRow=}')

        # @cache
        # cannot cache a generator (easily), so we've wrapped it in another function
        def nextRowGenerator(thisRow: List[str]) -> List[List[str]]:
            text = ''.join(thisRow)
            # print(f'  NRG({text}):')
            if len(thisRow) == 1:
                yield ()
                return
            firstPair = thisRow[:2]
            remainder = thisRow[1:]
            for otherChars in nextRowCached(remainder):
                if firstPair not in beAbove:
                    continue
                for firstChar in beAbove[firstPair]:
                    yield (firstChar,) + otherChars
            return

        @cache
        def nextRowCached(thisRow: List[str]) -> List[List[str]]:
            return tuple(nextRowGenerator(thisRow))

        def canStackOn(thisRow: List[str]) -> bool:
            text = ''.join(thisRow)
            # print(f'CSO({text}):')
            if len(thisRow) == 1:
                return True
            nextRowList = nextRowCached(thisRow)
            if not nextRowList:
                # print(f'  {text}:(no possible next row)')
                return False
            for nextRow in nextRowList:
                # print(f'  {text}:{nextRow=}')
                if canStackOn(nextRow):
                    return True
            return False

        return canStackOn(bottomRow)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 2299 ms Beats 54.49%
# NOTE: Memory 74.92 MB Beats 10.48%
