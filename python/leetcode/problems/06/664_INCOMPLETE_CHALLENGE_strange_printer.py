class Solution:
    def strangePrinter(self, s: str) -> int:

        @cache
        def fastestPrint(L: List[str], depth=0) -> int:
            margin = ' ' * depth
            print(f'{margin}FP({"".join(L)})')
            if depth > 5:
                return -999
            if not L:
                return 0

            had_dups = False
            for i in range(1, len(L)):
                if L[i] == L[i-1]:
                    had_dups = True
                    break
            if had_dups:
                L = tuple([key for key, grp in itertools.groupby(L)])
                # print(f'{margin}  Try again with shrunk answer')
                return fastestPrint(L, depth+1)
            # some special cases that are subsumed by the Counter query below
            if len(L) == 1:
                return 1
            elif len(L) == 2:
                return 2
            if len(L) == len(Counter(L)):
                # i.e. "abcd", all letters are different
                return len(L)
            First = L[0]
            Indexes = [
                index
                for index, value in enumerate(L)
                if value == First
            ]
            # print(f'{margin}  {First=} {Indexes=}')
            questions = []
            for I in Indexes:
                # print(f'{margin}{I=} DEBUG: check "{L[:I]}" and "{L[I+1:]}"')
                questions.append(
                #     # print this char by itself
                    (L[:I] + L[I+1:], ())
                )
            for A, B in pairwise(Indexes):
                # print(f'{margin}{(A,B)=} DEBUG: check "{L[A+1:B]}" and "{L[:A]}"+"{L[B+1:]}"')
                questions.append(
                    # print A:B as one unit, then everything within it, then the outside
                    (L[A+1:B], L[:A] + L[B+1:])
                )
            print(f'{margin}  questions:')
            for (X, Y) in questions:
                print(f'{margin}    [{"".join(X)}, {"".join(Y)}]')
            answers = [
                sum([
                    1,
                    fastestPrint(X, depth+1),
                    fastestPrint(Y, depth+1),
                ])
                for (X, Y) in questions
            ]
            answer = min(answers)
            # print(f'{margin}{answer=}')
            return answer
        
        return fastestPrint(tuple(s))

# NOTE: CHALLENGE
# NOTE: INCOMPLETE because Time Limit Exceeded for large inputs
# NOTE: test 51: "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"
