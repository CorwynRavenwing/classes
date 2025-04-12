class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        def generate_list(length: int) -> List[List[int]]:
            # print(f'GL({length})')
            if length == 0:
                yield ()
                return

            for one_smaller in generate_list(length - 1):
                for D in range(10):
                    yield (D,) + one_smaller
            return

        def generate_first_half(n: int) -> List[List[int]]:
            # print(f'GFH({n}):')
            for List in generate_list(n // 2):
                if not List or List[0] != 0:
                    # skip leading zeros
                    yield List
            return
        
        def generate_palindromes(n: int) -> List[List[int]]:
            # print(f'GP({n})')
            for FH in generate_first_half(n):
                REV = tuple(reversed(FH))
                if n % 2 == 0:
                    # even
                    yield FH + REV
                else:
                    # odd
                    for D in range(10):
                        yield FH + (D,) + REV
            return
        
        def digits_to_int(digits: List[int]) -> int:
            answer = 0
            for D in digits:
                answer *= 10
                answer += D
            return answer

        def generate_k_palindromes(n: int, k: int) -> List[List[int]]:
            for palindrome in generate_palindromes(n):
                value = digits_to_int(palindrome)
                if value % k == 0:
                    yield palindrome
            return

        def generate_k_palindrome_patterns(n: int, k: int) -> List[List[int]]:
            SORT = lambda x: tuple(sorted(x))
            sorted_k_palindromes = map(SORT, generate_k_palindromes(n, k))
            deduped_k_palindromes = set(sorted_k_palindromes)
            return SORT(deduped_k_palindromes)
        
        def pattern_without_value(pattern: List[int], value: int) -> List[int]:
            assert value in pattern
            index = pattern.index(value)
            return pattern[:index] + pattern[index + 1:]

        @cache
        def count_good_ints_by_pattern(pattern: List[int], first=True) -> int:
            if not pattern:
                return 1
            
            digits = set(pattern)
            if first:
                digits -= {0}

            answer = 0
            for D in sorted(digits):
                remainder = pattern_without_value(pattern, D)
                answer += count_good_ints_by_pattern(remainder, False)
            return answer

        def count_good_ints(n: int, k: int) -> int:
            return sum([
                count_good_ints_by_pattern(pattern)
                for pattern in generate_k_palindrome_patterns(n, k)
            ])
        
        return count_good_ints(n, k)

# NOTE: Acceptance Rate 33.0% (HARD)

# NOTE: second version:
# NOTE: Accepted on first Run, then added cache
# NOTE: Accepted on first Submit
# NOTE: Runtime 2545 ms Beats 6.45%
# NOTE: Memory 36.66 MB Beats 6.45%
