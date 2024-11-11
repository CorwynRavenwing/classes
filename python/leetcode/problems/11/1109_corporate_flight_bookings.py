class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        deltas = [0] * (n + 2)
        for (firstI, lastI, seatsI) in bookings:
            deltas[firstI] += seatsI
            deltas[lastI + 1] -= seatsI
        print(f'{deltas=}')

        partialSums = tuple(accumulate(deltas))
        print(f'{partialSums=}')

        return partialSums[1:-1]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 27 ms Beats 51.76%
# NOTE: Memory 28.32 MB Beats 89.15%
