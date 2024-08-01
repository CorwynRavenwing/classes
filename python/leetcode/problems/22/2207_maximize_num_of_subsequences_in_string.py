class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

        # SHORTCUT: all letters that are neither A nor B may be ignored entirely.
        (A, B) = pattern
        relevant_text = [
            L
            for L in text
            if L in (A, B)
        ]
        # print(f'{relevant_text=}')

        # SHORTCUT: the greatest values will be from putting
        # pattern[0] ("A" on the FRONT, or pattern[1] ("B") on the END.
        # All other values will be either equal or less than these.

        testA = [A] + relevant_text
        testB = relevant_text + [B]

        def show_big_list(L: List[str]) -> str:
            if len(L) < 10:
                return f'{L}'
            else:
                return f'{L[:5]}...({len(L)-10})...{L[-5:]}'

        # SHORTCUT: the value of a string will equal:
        # for each letter B: the sum of all letter A to the left of it.

        def valueOf_IfDifferent(test: List[str]) -> int:
            print(f'valueOf({show_big_list(test)}): [DIFF]')
            ones_at_A = [
                1 if (L == A) else 0
                for L in test
            ]
            print(f'  ones_at_A={show_big_list(ones_at_A)}')
            A_left_of = list(accumulate(ones_at_A))
            print(f'  A_left_of={show_big_list(A_left_of)}')
            sums_at_B = [
                Acount if (L == B) else 0
                for L, Acount in zip(test, A_left_of)
            ]
            print(f'  sums_at_B={show_big_list(sums_at_B)}')
            return sum(sums_at_B)

        # If A == B, I think the above still holds, but alternately
        # we can also calculate this as (number of A's) pick (2)
        # which equals:

        def Nchoose2(N: int) -> int:
            return N * (N - 1) // 2

        def valueOf_IfSame(test: List[str]) -> int:
            print(f'valueOf({show_big_list(test)}): [SAME]')
            return Nchoose2(len(test))
        
        def valueOf(test: List[str]) -> int:
            if A == B:
                return valueOf_IfSame(test)
            else:
                return valueOf_IfDifferent(test)

        answerA = valueOf(testA)
        answerB = valueOf(testB)
        print(f'{answerA=}, {answerB=}')
        return max(answerA, answerB)
# NOTE: Runtime 249 ms Beats 33.33%
# NOTE: Memory 25.53 MB Beats 5.98%
