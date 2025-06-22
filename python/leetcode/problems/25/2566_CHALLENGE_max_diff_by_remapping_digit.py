class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        def num_to_digits(num: int) -> List[int]:
            return tuple(
                map(
                    int,
                    tuple(
                        str(num)
                    )
                )
            )
        
        def digits_to_num(digits: List[int]) -> int:
            return int(
                ''.join(
                    map(
                        str,
                        digits
                    )
                )
            )
        
        def first_digit_other_than_N(N: int, digits: List[int]) -> int:
            digits_other_than_N = [
                D
                for D in digits
                if D != N
            ]
            return digits_other_than_N[0] if digits_other_than_N else None
        
        def remap(A: int, B: int, digits: List[int]) -> List[int]:
            # NOTE: if A is 'None', it will not be found,
            #       so the original digits will be returned
            return tuple(
                [
                    (
                        B if D == A
                        else D
                    )
                    for D in digits
                ]
            )
        
        # print(f'DEBUG: {num_to_digits(num)=}')
        # print(f'DEBUG: {digits_to_num([5,4,3,2,1])=}')

        original_digits = num_to_digits(num)

        low_replace = first_digit_other_than_N(0, original_digits)
        high_replace = first_digit_other_than_N(9, original_digits)

        low_digits = remap(low_replace, 0, original_digits)
        high_digits = remap(high_replace, 9, original_digits)

        low = digits_to_num(low_digits)
        high = digits_to_num(high_digits)

        return high - low

# NOTE: Acceptance Rate 60.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 18.09 MB Beats 11.01%

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.78 MB Beats 45.89%
