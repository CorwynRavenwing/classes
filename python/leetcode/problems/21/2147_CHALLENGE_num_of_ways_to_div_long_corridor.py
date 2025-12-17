class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        # batched() comes standard in python 3.12
        # unfortunately, leetcode uses python 3.11.9 as of right now
        # using a recipe from the itertools module, found at:
        # https://docs.python.org/3/library/itertools.html#itertools-recipes
        def batched(iterable, n):
            "Batch data into lists of length n. The last batch may be shorter."
            # batched('ABCDEFG', 3) --> ABC DEF G
            it = iter(iterable)
            while True:
                batch = list(islice(it, n))
                if not batch:
                    return
                yield batch

        # print(f'{sys.version=}')

        indexesByValue = {}
        indexesByValue.setdefault('S', [])          # create zero-seats record
        for index, value in enumerate(corridor):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        seat_indexes = indexesByValue['S']
        seats = len(seat_indexes)
        if seats % 2:
            print(f'Odd number of {seats=}')
            return 0
        if not seats:
            print(f'No {seats=}')
            return 0
        
        mutable_corridor = list(corridor)

        for (A, B) in batched(seat_indexes, 2):
            # print(f'{A},{B}')
            mutable_corridor[A] = 'A'
            mutable_corridor[B] = 'B'

        corridor = ''.join(mutable_corridor)
        print(f'{corridor=}')
        corridor = re.sub(r'AP*B', ':', corridor)   # pair of seats
        print(f'{corridor=}')
        corridor = re.sub(r'^P*:', ':', corridor)   # plants before first seat
        corridor = re.sub(r':P*$', ':', corridor)   # plants after last seat
        print(f'{corridor=}')
        corridor = re.sub(r'^:', '', corridor)      # first seats
        corridor = re.sub(r':$', '', corridor)      # last seats
        print(f'{corridor=}')
        while '::' in corridor:
            corridor = corridor.replace('::', ':')  # adjacent seats without plants
        print(f'{corridor=}')
        plants = corridor.split(':')
        print(f'{plants=}')
        groups = [
            len(frag) + 1
            for frag in plants
        ]
        print(f'{groups=}')

        mod = 10 ** 9 + 7

        answer = 1
        for N in groups:
            answer *= N
            answer %= mod
            print(f'... {answer=}')

        return answer % mod


# NOTE: Acceptance Rate 48.8% (HARD)

# NOTE: Accepted on third Run (edge case)
# NOTE: Accepted on third Submit (Output Exceeded; edge case)
# NOTE: Runtime 874 ms Beats 23.81%
# NOTE: Memory 24.05 MB Beats 24.76%
