class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        possibles = [
            [C]
            for C in candidates
        ]
        answers = []
        while possibles:
            print(f'L={len(possibles)}')
            P = possibles.pop(0)
            S = sum(P)
            M = max(P)
            print(f'  {S}: {P}')
            if S == target:
                print(f'    ={target}')
                answers.append(P)
                continue
            elif S > target:
                # print(f'    >{target}')
                # too big
                continue
            assert S < target
            for C in candidates:
                if C < M:
                    # print(f'      <{M}')
                    continue
                print(f'    +{C}')
                possibles.append(
                    P + [C]
                )
        return sorted(answers)

# NOTE: Runtime 247 ms Beats 5.58%
# NOTE: Memory 17.78 MB Beats 5.04%
