class ExamRoom:

    # we borrow some code from #849

    def distanceArray1Dir(self, seats: List[int]) -> List[int]:
        answer = [None] * len(seats)
        MAX = len(seats)
        dist = None
        for i, S in enumerate(seats):
            # print(f'DA[{i}]:{S}')
            if S == 1:
                dist = 0
            elif dist is not None:
                dist += 1
            # print(f'  -> {dist}')
            answer[i] = dist
        while None in answer:
            # print(f'{answer=}')
            answer[answer.index(None)] = MAX
        # print(f'{answer=}')
        return answer

    def distanceArray(self, seats: List[int]) -> int:
        leftArray = self.distanceArray1Dir(seats)
        # print(f'L:{leftArray}')
        rSeats = tuple(reversed(seats))
        rRightArray = self.distanceArray1Dir(rSeats)
        rightArray = tuple(reversed(rRightArray))
        # print(f'R:{rightArray}')
        bothWays = tuple(map(min, zip(leftArray, rightArray)))
        # print(f'B:{bothWays}')
        return bothWays

    def distanceNumber(self, seats: List[int]) -> int:
        bothWays = self.distanceArray(seats)
        return max(bothWays)

    def __init__(self, n: int):
        self.seats = [0] * n

    def seat(self) -> int:
        both = self.distanceArray(self.seats)
        print(f'D:{both}')
        # D = distanceNumber(self.seats)
        D = max(both)
        index = both.index(D)
        print(f'  next person sits in seat #{index}, {D=}')
        self.seats[index] = 1
        print(f'S:{self.seats}')
        return index

    def leave(self, p: int) -> None:
        assert self.seats[p] == 1
        print(f'Person in seat #{p} leaves')
        self.seats[p] = 0
        print(f'S:{self.seats}')
        return

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# NOTE: this is the original, modeled off of #849, which works fine
# until testcase 107 where they go "here's a room with a million seats"
