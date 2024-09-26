class MyCalendar:

    def __init__(self):
        self.bookings = []
        return
    
    def bookingAllowed(self, booking1: Tuple[int,int], booking2: Tuple[int,int]) -> bool:
        print(f'Compare {booking1=} {booking2=}')
        (start1, end1) = booking1
        assert start1 <= end1
        (start2, end2) = booking2
        assert start2 <= end2
        assert start1 <= start2
        return (start1 <= end1 <= start2 <= end2)

    def bookingConflict(self, booking1: Tuple[int,int], booking2: Tuple[int,int]) -> bool:
        return not self.bookingAllowed(booking1, booking2)

    def book(self, start: int, end: int) -> bool:
        assert start < end
        newBooking = (start, end)
        if len(self.bookings) == 0:
            # nothing in list: insert as first member
            print(f'First booking {newBooking}')
            self.bookings.append(newBooking)
            return True
        
        index = bisect_left(self.bookings, newBooking)
        if index > 0:
            # not first: compare with *prior* booking
            priorBooking = self.bookings[index - 1]
            if self.bookingConflict(priorBooking, newBooking):
                print(f'Conflict: {newBooking=} overlaps {priorBooking=}')
                # do NOT insert it
                return False

        if index < len(self.bookings):
            # not last: compare with *next* booking
            nextBooking = self.bookings[index]
            if self.bookingConflict(newBooking, nextBooking):
                print(f'Conflict: {newBooking=} overlaps {nextBooking=}')
                # do NOT insert it
                return False

        if index >= len(self.bookings):
            # last: insert after everything
            print(f'Last booking {newBooking}')
            self.bookings.append(newBooking)
            return True
        else:
            print(f'New booking {newBooking} at {index=}')
            self.bookings.insert(index, newBooking)
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# NOTE: Runtime 239 ms Beats 47.78%
# NOTE: Memory 17.45 MB Beats 34.88%
