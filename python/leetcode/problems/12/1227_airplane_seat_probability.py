class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:

        # SHORTCUT: the following code works, but gives Memory Limit Exceeded
        # for large inputs.  Let's examine the question statistically.

        # person #0 chooses randomly.  There are three cases:
        # case 1: he chooses his own seat randomly.
        # case 2: he chooses seat #N randomly.
        # case 3: he chooses any other seat.
        # prob(1) = 1/n; prob(2) = 1/n; prob(3) = (n-2)/n.
        # note that specifically, case 1 and case 2 have the SAME probablility.

        # in case 1, everyone gets their own seat, including #N.
        # in case 2, everyone gets their own seat, except #N, who gets seat 1.
        # in case 3, suppose person #0 picked seat #X.

        # persons 1 through X-1 all get their correct seats.
        # person #X does not: he picks randomly from seats (1, X+1, X+2, ... N).
        # case 1: he picks seat #1.
        # case 2: he picks seat #N.  Note that again, these two have equal probability.
        # case 3: he picks any other seat.

        # we can do this again with seat #Y chosen by person #X.
        # In each case, we have 50% yes and 50% no, with an option of trying again
        # with another, higher seat number.  Once we're testing seat #N-1,
        # there are only *two* possibilities:
        # case 1: he picks seat #1.
        # case 2: he picks seat #N.  Again, 50% probability apiece.
        # there are no other available seats.

        # THEREFORE, the probablility is always 50% for any N > 1.
        return (
            1.0
            if n == 1
            else 0.5
        )

        # # @cache
        # def all_random_seat_combos(seats: List[int]) -> List[List[int]]:
        #     return [
        #         seats[:index] + (1,) + seats[index+1:]
        #         for index, value in enumerate(seats)
        #         if value == 0
        #     ]

        # # returning *odds the nth person gets his own seat*
        # # given that we're currently seating #person
        # # and have the current occupied seats:
        # @cache
        # def DP(person: int, seats: List[int]) -> float:
        #     # print(f'DP({person},{seats})')
        #     # unlike the question, we're going to use 0 as first passenger
        #     # and n-1 as last passenger

        #     if seats[person] == 0:
        #         # person's seat is NOT taken

        #         if person == n - 1:
        #             return 1.0000
                
        #         if person != 0:
        #             # any other person number:
        #             index = person
        #             seats = seats[:index] + (1,) + seats[index+1:]
        #             return DP(person + 1, seats)

        #         # person #0 falls through, because he sits somewhere random
            
        #     else:
        #         # person's seat IS taken

        #         if person == n - 1:
        #             return 0.0000
                
        #     # random seat selection case:
        #     possibles = all_random_seat_combos(seats)
        #     answers = [
        #         DP(person + 1, seats)
        #         for seats in possibles
        #     ]
        #     return sum(answers) / len(answers)

        # seats = (0,) * n
        # return DP(0, seats)

# NOTE: DP version: Time Limit Exceeded for large inputs.
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.84 MB Beats 7.84%
