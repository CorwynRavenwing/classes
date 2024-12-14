class SeatManager:

    def __init__(self, n: int):
        self.available = list(range(1, n + 1))
        return

    def reserve(self) -> int:
        return self.available.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        bisect.insort(self.available, seatNumber)
        return

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3245 ms Beats 5.01%
# NOTE: Memory 46.53 MB Beats 19.72%
