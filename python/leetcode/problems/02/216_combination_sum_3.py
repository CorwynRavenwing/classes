class Solution:

    # we borrow some code from #40:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        possibles = [
            ([], candidates)
        ]
        answers = []
        while possibles:
            print(f'L={len(possibles)}')
            P = possibles.pop(0)
            (answer, remaining) = P
            S = sum(answer)
            M = max(answer) if answer else 0
            print(f'  {S}: {answer} / {remaining}')
            if S == target:
                print(f'    ={target}')
                answers.append(answer)
                continue
            elif S > target:
                print(f'    >{target}')
                # too big
                continue
            assert S < target
            for C in set(remaining):
                print(f'    +{C}')
                if C < M:
                    print(f'      <{M}')
                    continue
                # print(f'    +{C}')
                new_remaining = remaining.copy()
                new_remaining.remove(C)
                new_remaining = [
                    NR
                    for NR in new_remaining
                    if NR >= C
                ]
                possibles.append(
                    (answer + [C], new_remaining)
                )
        return sorted(answers)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        candidates = list(range(1, 9 + 1))

        answers = self.combinationSum2(candidates, n)
        print(f'{answers=}')
        
        right_length = [
            A
            for A in answers
            if len(A) == k
        ]
        return right_length

# NOTE: Re-used all of prior code, adding only some filters
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 36 ms Beats 54.15%
# NOTE: Memory 17.00 MB Beats 5.86%
