class Solution:
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
# NOTE: Runtime 520 ms Beats 5.01%
# NOTE: Memory 18.21 MB Beats 6.94%
