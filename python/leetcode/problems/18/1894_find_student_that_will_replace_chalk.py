class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        if len(chalk) == 1:
            return 0

        # SHORTCUT:
        one_round = sum(chalk)
        if k > one_round:
            print(f'{k=} % {one_round=}:')
            k %= one_round
            print(f'  ->{k}')
        
        while True:
            for studentID, studentChalk in enumerate(chalk):
                if k < studentChalk:
                    return studentID
                else:
                    k -= studentChalk
# NOTE: Runtime 564 ms; Beats 86.83%
