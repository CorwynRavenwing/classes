class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        def distanceArray(seats: List[int]) -> List[int]:
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

        leftArray = distanceArray(seats)
        print(f'L:{leftArray}')
        rSeats = tuple(reversed(seats))
        rRightArray = distanceArray(rSeats)
        rightArray = tuple(reversed(rRightArray))
        print(f'R:{rightArray}')
        bothWays = tuple(map(min, zip(leftArray, rightArray)))
        print(f'B:{bothWays}')
        return max(bothWays)

