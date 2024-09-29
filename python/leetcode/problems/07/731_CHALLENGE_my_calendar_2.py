class MyCalendarTwo:

    # IDEA: replace "do they conflict" code with "show their overlap" code
    #   then take just the overlaps and post them to a second "double-booked" list
    #   re-lookup new overlaps in the "double-booked" list and reject if "triple-booked"
    
    # we borrow some code from #729:

    def __init__(self):
        self.singleBooked = []
        self.doubleBooked = []
        return

    def insertAndClean(self, bookingsList: List[Tuple[int,int]], booking: Tuple[int,int]) -> None:
        # print(f'insertAndClean():')
        # print(f'  {bookingsList=}')
        # print(f'  {booking=}')
        # do this rather than 'insort()' so that we also have the index afterwards
        index = bisect_left(bookingsList, booking)
        bookingsList.insert(index, booking)
        # print(f'  {index=}')
        if index == 0:
            index += 1
        for i in range(index, len(bookingsList)):
            (prevStart, prevEnd) = bookingsList[i - 1]
            (nextStart, nextEnd) = bookingsList[i]
            if prevEnd > nextStart:
                mergedBooking = (
                    min(prevStart,nextStart),
                    max(prevEnd,nextEnd),
                )
                # print(f'  Clean {i=}: overlap ({prevStart},{prevEnd})/({nextStart},{nextEnd})')
                # print(f'    -> {mergedBooking}')
                bookingsList[i - 1] = None
                bookingsList[i] = mergedBooking
        while None in bookingsList:
            # print(f'  Clean End: remove None')
            bookingsList.remove(None)
        return

    def bookingOverlap(self, booking1: Tuple[int,int], booking2: Tuple[int,int]) -> Tuple[int,int]:
        # print(f'Compare {booking1=} {booking2=}')
        (start1, end1) = booking1
        assert start1 <= end1
        (start2, end2) = booking2
        assert start2 <= end2
        assert start1 <= start2
        answerStart = max(start1, start2)
        answerEnd = min(end1, end2)
        answer = (
            answerStart,
            answerEnd,
        )
        # "<" not "<=" because an "overlap" of (5, 5) doesn't count
        return answer if (answerStart < answerEnd) else ()

    def bookingsListOverlaps(self, label: str, bookingsList: List[Tuple[int,int]], newBooking: Tuple[int,int]) -> List[Tuple[int,int]]:

        # print(f'bookingsListOverlaps({label}):')
        # print(f'  {bookingsList=}')
        # print(f'  {newBooking=}')

        if len(bookingsList) == 0:
            # nothing in list: insert as first member
            # print(f'First {label}-booking {newBooking}')
            return []
        
        # print(f'DEBUG: Calling bisect_left(L)')
        # print(f'  {bookingsList=}')
        # print(f'  {newBooking=}')
        indexLeft = bisect_left(bookingsList, newBooking)
        all_conflicts = []
        if indexLeft > 0:
            # not first: compare with *prior* booking
            priorBooking = bookingsList[indexLeft - 1]
            conflict = self.bookingOverlap(priorBooking, newBooking)
            if conflict:
                # print(f'Conflict: {label}-booking {newBooking=} overlaps {priorBooking=}')
                # print(f'  {conflict=}')
                all_conflicts.append(conflict)

        if indexLeft < len(bookingsList):
            # not last: compare with *next* booking(s)
            (start, end) = newBooking
            bookingEndcap = (end, 0)
            # print(f'DEBUG: Calling bisect_left(R)')
            # print(f'  {bookingsList=}')
            # print(f'  {bookingEndcap=}')
            indexRight = bisect_left(bookingsList, bookingEndcap)
            otherBookingsToRight = bookingsList[indexLeft:indexRight]
            conflicts = [
                self.bookingOverlap(newBooking, nextBooking)
                for nextBooking in otherBookingsToRight
            ]
            if conflicts:
                # print(f'Conflict: {label}-booking {newBooking=} overlaps {otherBookingsToRight=}')
                # print(f'  {conflicts=}')
                all_conflicts.extend(conflicts)

        if all_conflicts:
            return all_conflicts
        else:
            # print(f'New {label}-booking {newBooking} at {indexLeft=}')
            return []

    def bookSingleOverlaps(self, newBooking: Tuple[int,int]) -> List[Tuple[int,int]]:
        return self.bookingsListOverlaps(
            'single',
            self.singleBooked,
            newBooking
        )

    def bookDoubleOverlaps(self, newBooking: Tuple[int,int]) -> List[Tuple[int,int]]:
        return self.bookingsListOverlaps(
            'double',
            self.doubleBooked,
            newBooking
        )

    def book(self, start: int, end: int) -> bool:
        assert start < end
        newBooking = (start, end)
        print(f'\nBOOK({newBooking}):')
        Double_Bookings = self.bookSingleOverlaps(newBooking)
        if Double_Bookings:
            print(f'  -> {Double_Bookings=}')
        Triple_Bookings = [
            triple_booking
            for double_booking in Double_Bookings
            for triple_booking in self.bookDoubleOverlaps(double_booking)
        ]
        if Triple_Bookings:
            print(f'  -> {Triple_Bookings=}')

        # failure: insert nothing, return false.
        if Triple_Bookings:
            print(f'3: TRIPLE-BOOKINGS EXIST {newBooking}')
            print(f'  {Triple_Bookings=}')
            return False
        
        # success: insert both double-bookings...
        for double_booking in Double_Bookings:
            print(f'2: INSERT DOUBLE-BOOKING {double_booking}')
            self.insertAndClean(self.doubleBooked, double_booking)

        # ... and single-bookings; return true.
        print(f'1: INSERT SINGLE-BOOKING {newBooking}')
        self.insertAndClean(self.singleBooked, newBooking)
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

# NOTE: Re-used much of the code from prior version
# NOTE: Runtime 486 ms Beats 58.11%
# NOTE: Memory 17.69 MB Beats 35.11%
