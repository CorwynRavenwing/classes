class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        answers = []
        for i, A in enumerate(arr):
            if A > 2:
                continue
            for j, B in enumerate(arr):
                if i == j:
                    continue
                AB = f'{A}{B}'
                if AB > '23':
                    continue
                for k, C in enumerate(arr):
                    if i == k or j == k:
                        continue
                    for h, D in enumerate(arr):
                        if i == h or j == h or k == h:
                            continue
                        CD = f'{C}{D}'
                        if CD > '59':
                            continue
                        ABCD = f'{AB}:{CD}'
                        print(f'[{i},{j},{k},{h}] == "{ABCD}"')
                        answers.append(ABCD)
        return max(answers, default='')

