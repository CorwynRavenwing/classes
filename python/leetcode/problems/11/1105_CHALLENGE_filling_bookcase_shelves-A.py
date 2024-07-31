class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        # we need to keep track of these parameters in our queue:
        # (
        #     total_height_of_other_shelves,
        #     height_of_current_shelf,
        #     width_remaining_on_current_shelf,
        #     next_book_index,
        # )
        # hashableBooks = tuple(map(tuple, books))
        queue = [
            (0, 0, shelfWidth, 0)
        ]
        minHeight = float('+inf')
        while queue:
            Q = queue.pop(0)
            (heightBelowMe, currHeight, currWidth, bookIndex) = Q
            # print(f'B={heightBelowMe}, H={currHeight}, W={currWidth}, {bookIndex}')
            if heightBelowMe + currHeight >= minHeight:
                # print(f'  TOO TALL ({heightBelowMe + currHeight})')
                continue
            if bookIndex >= len(books):
                heightBelowMe += currHeight
                minHeight = min(minHeight, heightBelowMe)
                print(f'  ANSWER {heightBelowMe} -> {minHeight=}')
                continue
            thisBook = books[bookIndex]
            (W, H) = thisBook
            # print(f'  {W=} {H=}')
            if W <= currWidth:
                # will fit on current shelf
                A = (heightBelowMe, max(H, currHeight), currWidth - W, bookIndex + 1)
                # print(f'    {A=}')
                queue.append(A)
            # else:
            #     print(f'    {W=} > {currWidth=}, cannot add to current shelf')
            if currHeight > 0:
                # make a new shelf
                B = (heightBelowMe + currHeight, H, shelfWidth - W, bookIndex + 1)
                # print(f'    {B=}')
                queue.append(B)
            # else:
            #     print(f'    {currHeight=} == 0, this is the first shelf')
        return minHeight
# NOTE: works, but Time Limit Exceeded for large inputs.
