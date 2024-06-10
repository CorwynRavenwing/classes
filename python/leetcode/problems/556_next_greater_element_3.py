class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # we borrow some code from question #31:

        digits = list(str(n))
        print(f'{digits}')

        def sort_starting_at(ptr: int) -> None:
            nonlocal digits
            # also changes digits in-place, returning nothing
            while ptr < len(digits) - 1:
                print(f'sorting range {digits[ptr:]}')
                MP = ptr
                MN = digits[MP]
                for P in range(ptr + 1, len(digits)):
                    if MN > digits[P]:
                        MN = digits[P]
                        MP = P
                print(f'  minimum value digits[{MP}]={MN}')
                (digits[ptr], digits[MP]) = (digits[MP], digits[ptr])
                print(f'     sorted = {digits[ptr:]}')
                ptr += 1
            return

        # 0. If length of list is 0 or 1, return it as-is
        #    because you can't sort empty or 1-element lists
        if (not digits) or (len(digits) == 1):
            return -1

        # 1. Find section at right that is decreasing (or same).
        #    Everything left of that, stays the same.
        ptr = len(digits) - 1
        print(f'{ptr=}')
        while ptr and (digits[ptr - 1] >= digits[ptr]):
            ptr -= 1
            print(f'{ptr=}')

        print(f'{digits[ptr:]=}')

        if not ptr:
            # entire list is in reverse order.  "next" == fail
            # sort_starting_at(ptr)
            return -1

        # 2. find "next" value greater than pivot, swap it to be next
        pivot = ptr - 1
        PV = digits[pivot]
        MP = ptr
        MN = digits[MP]
        print(f'pivot at {digits[pivot]}; {digits[ptr:]}')
        for P in range(ptr + 1, len(digits)):
            if MN > digits[P] > PV:
                MN = digits[P]
                MP = P
        print(f'  minimum value > {PV} digits[{MP}]={MN}')
        (digits[pivot], digits[MP]) = (digits[MP], digits[pivot])
        print(f'after pivot: {digits[pivot:]}')

        # 3. sort everything after the pivot
        sort_starting_at(ptr)
        answer = ''.join(digits)

        # 4. check for 32-bit signed integer
        MAXINT = (2 ** 31) - 1
        MAXSTR = str(MAXINT)
        if len(answer) > len(MAXSTR):
            # more digits than MAXINT (should be impossible)
            return -1
        elif len(answer) == len(MAXSTR):
            if answer > MAXSTR:
                # same length, string greater === integer > MAXINT
                return -1

        return int(answer)

