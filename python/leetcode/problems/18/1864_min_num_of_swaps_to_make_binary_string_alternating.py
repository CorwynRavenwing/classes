class Solution:
    def minSwaps(self, s: str) -> int:

        check = Counter(s)
        zero = check['0']
        ones = check['1']
        allowed_types = None
        match (ones - zero):
            case -1:
                allowed_types = 'E'     # 01010
            case 0:
                allowed_types = 'EO'    # 1010 or 0101
            case 1:
                allowed_types = 'O'     # 10101
            case _:
                # solvable strings with N ones all have either N-1, N, or N+1 zeros.
                print(f'Mismatch! {zero=} {ones=}')
                return -1
        diffs_even = 0
        diffs_odds = 0
        for index, digit in enumerate(s):
            if index % 2 == 0:
                # even index
                digit_even = '0'
            else:
                # odd index
                digit_even = '1'
            if digit == digit_even:
                diffs_odds += 1
            else:
                diffs_even += 1
            # therefore d_e + d_o === len(s), and we really only need to calculate one of them
        
        available_diffs = [
            diffs_even if 'E' in allowed_types else None,
            diffs_odds if 'O' in allowed_types else None,
        ]
        while None in available_diffs:
            available_diffs.remove(None)
        best_diffs = min(available_diffs)
        print(f'{diffs_even=} {diffs_odds=} {available_diffs=} {best_diffs=}')

        return best_diffs // 2  # ONE swap moves TWO misplaced digits

