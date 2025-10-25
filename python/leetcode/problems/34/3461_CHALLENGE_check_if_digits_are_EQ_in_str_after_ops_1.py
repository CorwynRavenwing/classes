class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        digits = tuple(map(int, s))

        def klibitzim(digits: List[int]) -> List[int]:
            answer = []
            for i in range(1, len(digits)):
                A = digits[i - 1]
                B = digits[i]
                C = (A + B) % 10
                print(f'  ({A},{B}) -> {C}')
                answer.append(C)
            return answer
        
        while len(digits) > 2:
            print(f'{digits=}')
            digits = klibitzim(digits)

        print(f'{digits=}')
        (A, B) = digits
        return (A == B)

# NOTE: Acceptance Rate 78.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 202 ms Beats 6.18%
# NOTE: Memory 18.25 MB Beats 26.37%
