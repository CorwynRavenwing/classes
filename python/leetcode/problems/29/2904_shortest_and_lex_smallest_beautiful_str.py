class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        shortest_length = float('inf')
        shortest_strings = []
        # I was going to do Sliding Window here, but then I realized
        # that we just need groups of K 1's
        one_indexes = [
            index
            for index, value in enumerate(s)
            if value == '1'
        ]
        print(f'{one_indexes=}')
        # and I just realized what I really need is this function:
        # from Itertools Recipes
        # https://docs.python.org/3/library/itertools.html
        def sliding_window(iterable, n):
            "Collect data into overlapping fixed-length chunks or blocks."
            # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
            iterator = iter(iterable)
            window = collections.deque(islice(iterator, n - 1), maxlen=n)
            for x in iterator:
                window.append(x)
                yield tuple(window)
        
        for ones in sliding_window(one_indexes, k):
            print(f'  {ones=}')
            first = ones[0]
            last = ones[-1]
            this_length = last + 1 - first
            this_string = s[first:last + 1]
            if shortest_length == this_length:
                print(f'    NEW GROUP {this_length}')
                shortest_strings.append(this_string)
            elif shortest_length > this_length:
                shortest_length = this_length
                shortest_strings = [this_string]
                print(f'    ADD STRING {this_length}')
        
        print(f'{shortest_length=}')
        print(f'{shortest_strings=}')

        return min(shortest_strings, default='')
        # min() works lexicographically

# NOTE: Accepted on first Submit
# NOTE: Runtime 42 ms Beats 45.22%
# NOTE: Memory 16.76 MB Beats 11.80%
