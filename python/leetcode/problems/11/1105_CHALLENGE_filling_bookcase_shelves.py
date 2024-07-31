class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        heightPriorToBook = [float('+inf')] * (len(books) + 1)
        # HEAB[i] is the height consumed by books 0 .. i-1, with book i-1 ending a shelf.
        # we only record the *minimum* such height.
        # Therefore HEAB[0] is the height consumed by no books at all. (=== 0)
        # and the answer is in HEAB[len(books)]

        def showHPTB(i, j):
            lowest = max(0, i-2)
            highest = min(len(books), j + 2)
            print(f'\t...{heightPriorToBook[lowest:highest+1]}...')

        for i in range(len(books)):
            print(f'{i=}')
            # showHPTB(i, i)
            if i == 0:
                heightPriorToBook[i] = 0
                # showHPTB(i, i)
            heightBelowMe = heightPriorToBook[i]
            (currHeight, currWidth) = (0, shelfWidth)
            for j in range(i, len(books)):
                thisBook = books[j]
                (W, H) = thisBook
                # print(f'  {j=} {thisBook=} {currHeight=} {currWidth=}')
                if W <= currWidth:
                    currWidth -= W
                    currHeight = max(H, currHeight)
                    newHeight = heightBelowMe + currHeight
                    heightPriorToBook[j + 1] = min(
                        heightPriorToBook[j + 1],
                        newHeight,
                    )
                    # showHPTB(i, j)
                else:
                    print(f'    {W} > {currWidth}')
                    # stop moving J right
                    break

        return heightPriorToBook[len(books)]
# NOTE: Runtime 67 ms Beats 13.56%
# NOTE: Memory 17.07 MB Beats 48.87%
