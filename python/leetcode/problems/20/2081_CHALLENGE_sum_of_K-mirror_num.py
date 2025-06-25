class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        @cache
        def all_digits_base_B(B: int) -> List[int]:
            # returns a TUPLE.  SHOULD be cached.
            return tuple(range(B))

        def generate_numbers_length_H_base_B(H: int, B: int) -> List[List[int]]:
            # returns a GENERATOR.  May NOT be cached.
            if H == 0:
                yield ()
                return
            for shorter in generate_numbers_length_H_base_B(H - 1, B):
                for digit in all_digits_base_B(B):
                    yield shorter + (digit,)
            return
        
        @cache
        def all_numbers_length_H_base_B(H: int, B: int) -> List[List[int]]:
            # returns a TUPLE.  SHOULD be cached.
            return tuple(generate_numbers_length_H_base_B(H, B))
        
        @cache
        def REV(digits: List[int]) -> List[int]:
            # returns a TUPLE.  SHOULD be cached.
            return tuple(reversed(digits))

        def generate_palindromes_length_L_base_B(L: int, B: int) -> List[List[int]]:
            # returns a GENERATOR.  May NOT be cached.
            if L % 2 == 0:
                # even size
                H = L // 2
                for firsthalf in all_numbers_length_H_base_B(H, B):
                    secondhalf = REV(firsthalf)
                    yield firsthalf + secondhalf
            else:
                # odd size
                H = L // 2
                for firsthalf in all_numbers_length_H_base_B(H, B):
                    secondhalf = REV(firsthalf)
                    for digit in all_digits_base_B(B):
                        yield firsthalf + (digit,) + secondhalf
            return
        
        # print(f'DEBUG: {tuple(generate_palindromes_length_L_base_B(2, 10))=}')
        # print(f'DEBUG: {tuple(generate_palindromes_length_L_base_B(5, 2))=}')

        def generate_palindromes_base_B(B: int) -> List[List[int]]:
            # returns a GENERATOR.  May NOT be cached.
            length = 0
            while True:
                length += 1
                for palindrome in generate_palindromes_length_L_base_B(length, B):
                    if palindrome and (palindrome[0] == 0):
                        # print(f'  DEBUG: skip leading zero: {palindrome}')
                        continue
                    yield palindrome
        
        def digits_to_int_base_B(digits: List[int], B: int) -> int:
            digits = list(digits)
            answer = 0
            while digits:
                answer *= B
                answer += digits.pop(0)
            return answer
        
        def generate_palindromes_base_B_int(B: int) -> List[int]:
            for palindrome in generate_palindromes_base_B(B):
                yield digits_to_int_base_B(palindrome, B)
        
        def generate_palindromes_base_B_and_10(B: int) -> List[List[int]]:
            # returns a GENERATOR.  May NOT be cached.
            base_10_gen = generate_palindromes_base_B_int(10)
            base_B_gen = generate_palindromes_base_B_int(B)
            A = next(base_10_gen)
            B = next(base_B_gen)
            print(f'{A=} {B=}')
            while True:
                if A < B:
                    # print(f'SKIP A: {A} < {B}')
                    A = next(base_10_gen)
                elif A > B:
                    # print(f'SKIP B: {A} > {B}')
                    B = next(base_B_gen)
                elif A == B:
                    print(f'MATCH: {A} == {B}')
                    yield A
                    A = next(base_10_gen)
                    B = next(base_B_gen)
                    
            return (42,)
        
        answer = 0
        i = 0
        for palindrome in generate_palindromes_base_B_and_10(k):
            answer += palindrome
            print(f'[{i}] {palindrome} ({answer})')
            i += 1
            if i >= n:
                break

        return answer

# NOTE: Acceptance Rate 42.3% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 5223 ms Beats 5.16%
# NOTE: Memory 154.68 MB Beats 5.81%
