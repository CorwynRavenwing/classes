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

        def generate_possible_good_ints(pattern: List[int]) -> List[List[int]]:
            if not pattern:
                yield ()
                return
            
            for D in sorted(set(pattern)):
                remainder = pattern_without_value(pattern, D)
                # print(f'  {pattern=}: {D} + {remainder}')
                for value in generate_possible_good_ints(remainder):
                    yield (D,) + value
            return

        @cache
        def possible_good_ints(pattern: List[int]) -> List[List[int]]:
            return generate_possible_good_ints(pattern)

        def generate_good_ints(n: int, k: int) -> List[List[int]]:
            for pattern in generate_k_palindrome_patterns(n, k):
                # print(f'GKPP: {pattern}')
                for good_int in possible_good_ints(pattern):
                    if good_int[0] != 0:
                        # skip initial zeros again
                        yield good_int
            return
        
        def count_good_ints(n: int, k: int) -> int:
            answer = 0
            for X in generate_good_ints(n, k):
                answer += 1
                # print(X)
            
            return answer
        
        return count_good_ints(n, k)

# NOTE: Acceptance Rate 33.0% (HARD)

# NOTE: Timeout Error
