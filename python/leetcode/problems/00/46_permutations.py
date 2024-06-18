class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        possibles = [
            ([], nums)
        ]
        answers = []
        while possibles:
            print(f'L={len(possibles)}')
            P = possibles.pop(0)
            (answer, remaining) = P
            print(f'  {answer} / {remaining}')
            if not remaining:
                print(f'    done')
                answers.append(answer)
                continue
            for C in set(remaining):
                print(f'    +{C}')
                new_remaining = remaining.copy()
                new_remaining.remove(C)
                possibles.append(
                    (answer + [C], new_remaining)
                )
        return sorted(answers)

