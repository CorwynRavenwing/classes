class ExamRoom:

    # we borrow some code from #849
    # ... but we give it back because the million-seats testcase
    # times out, for obvious reasons

    def __init__(self, n: int):
        self.full_seats = {}
        self.empty_seats = []
        self.N = n
        print(f'init({n})')

    def newBubble(self, leftId: int, rightId: int) -> Tuple[int,int,Tuple[int,int]]:
        print(f'newBubble({leftId},{rightId})')
        if leftId is None and rightId is None:
            index = 0
            dist = abs(self.N - index)
        elif leftId is None:
            index = 0
            dist = abs(rightId - index)
        elif rightId is None:
            index = (self.N - 1)
            dist = abs(leftId - index)
        else:
            index = (leftId + rightId) // 2
            dist = min(
                abs(leftId - index),
                abs(rightId - index),
            )
        retval = (dist, index, (leftId, rightId))
        print(f'  -> {retval}')
        return retval

    def clean(self) -> None:
        while None in self.empty_seats:
            self.empty_seats.remove(None)
            
    def seat(self) -> int:
        print(f'called seat():')
        if not self.full_seats:
            index = 0
            print(f'  First person sits in seat #{index}')
            emptySeat = (self.N - 1, self.N - 1, (index, None))
            self.empty_seats.append(emptySeat)
            self.full_seats[index] = (None, emptySeat)
            return index

        self.clean()
        
        bestSeat = max(
            self.empty_seats,
            key=lambda x: (x[0], -x[1])
            # highest distance, then lowest seat number
        )
        print(f'  {bestSeat=}')
        (distance, index, neighbors) = bestSeat
        (leftId, rightId) = neighbors
        if leftId is not None:
            (leftKeep, leftJunk) = self.full_seats[leftId]
        else:
            (leftKeep, leftJunk) = (None, None)
        if rightId is not None:
            (rightJunk, rightKeep) = self.full_seats[rightId]
        else:
            (rightJunk, rightKeep) = (None, None)

        newLeftBubble = self.newBubble(leftId, index)
        newRightBubble = self.newBubble(index, rightId)

        if leftId is not None:
            self.full_seats[leftId] = (leftKeep, newLeftBubble)
        self.full_seats[index] = (newLeftBubble, newRightBubble)
        if rightId is not None:
            self.full_seats[rightId] = (newRightBubble, rightKeep)

        self.empty_seats.remove(bestSeat)
        self.empty_seats.append(newLeftBubble)
        self.empty_seats.append(newRightBubble)

        print(f'  next person sits in seat #{index}')
        return index

    def leave(self, p: int) -> None:
        print(f'leave({p})')
        assert p in self.full_seats
        (oldLeftBubble, oldRightBubble) = self.full_seats[p]
        del self.full_seats[p]
        if len(self.full_seats) == 0:
            self.empty_seats = []
            return
        
        if oldLeftBubble is not None:
            (junk1, junk2, leftPoints) = oldLeftBubble
            (leftId, junk5) = leftPoints
        else:
            leftId = None

        if leftId is not None:
            (leftKeep, leftJunk) = self.full_seats[leftId]
        else:
            (leftKeep, leftJunk) = (None, None)

        if oldRightBubble is not None:
            (junk3, junk4, rightPoints) = oldRightBubble
            (junk6, rightId) = rightPoints
        else:
            rightId = None

        if rightId is not None:
            (rightJunk, rightKeep) = self.full_seats[rightId]
        else:
            (rightJunk, rightKeep) = (None, None)

        bigBubble = self.newBubble(leftId, rightId)

        if leftId is not None:
            self.full_seats[leftId] = (leftKeep, bigBubble)
        if rightId is not None:
            self.full_seats[rightId] = (bigBubble, rightKeep)

        if oldLeftBubble is not None:
            self.empty_seats.remove(oldLeftBubble)
        if oldRightBubble is not None:
            self.empty_seats.remove(oldRightBubble)
        self.empty_seats.append(bigBubble)

        self.clean()
        
        print(f'Person in seat #{p} leaves')
        return

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
