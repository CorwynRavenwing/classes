class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # NOTE: we want the Kth string of length N
        
        # SHORTCUT 1: There are exactly 3 happy strings of length 1: ['a', 'b', 'c']
        # of these, 1 does begin with 'a' and 2 don't begin with 'a'; same for 'b' and 'c'.
        # happy_string_count_with(1) = 1
        # happy_string_count_without(1) = 2
        # happy_string_count_total(1) = 3

        # SHORTCUT 2: Happy strings of length N ===
        # 'a' + (happy strings of length N-1 that don't begin with 'a')
        # 'b' + (happy strings of length N-1 that don't begin with 'b')
        # 'c' + (happy strings of length N-1 that don't begin with 'c')
        # happy_string_count_with(N) === 1 * happy_string_count_without(N-1)
        # happy_string_count_without(N) === 2 * happy_string_count_without(N-1) (***)
        # happy_string_count_total(N) === 3 * happy_string_count_without(N-1)

        # SHORTCUT 3: because of the equation with the asterisks (***) above,
        # happy_string_count_without(N) === 2^N for all N.
        # happy_string_count_total(N) === 3/2 * hsc_wo(N) === 2 * 2^(N-1) for all N.

        def happy_string_count_without(N: int) -> int:
            return 2 ** N
        
        def happy_string_count_with(N: int) -> int:
            return 2 ** (N - 1)

        def happy_string_count_total(N: int) -> int:
            return 3 * 2 ** (N - 1)
        
        if k > happy_string_count_total(n):
            print(f'Not enough happy strings')
            return ""
        
        def generate_happy_string(n: int, k: int, skipLetter: str) -> str:
            # again, Kth string of length N
            print(f'GHS({n},{k},"{skipLetter}")')
            if n == 0:
                return ''
            letters_if_we_skip = {
                '': 'abc',
                'a': 'bc',
                'b': 'ac',
                'c': 'ab',
            }
            downOneCount = happy_string_count_without(n - 1)
            for letter in letters_if_we_skip[skipLetter]:
                print(f'  DEBUG: {letter=} {k=} {downOneCount=}')
                if k > downOneCount:
                    print(f'  skip "{letter}":{downOneCount}')
                    k -= downOneCount
                    assert k >= 0
                    continue
                print(f'  pick "{letter}":')
                return letter + generate_happy_string(n - 1, k, letter)
            return 'Error: we should never get here!'

        return generate_happy_string(n, k, '')

# NOTE: Accepted on third Run (two variable-name typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 89.16%
# NOTE: Memory 16.95 MB Beats 46.59%
