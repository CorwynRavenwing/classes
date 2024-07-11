class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        answers = []
        nameMap = {}

        for N in names:
            # print(f'{N}:')
            newName = N
            k = 0
            if N in nameMap:
                k = nameMap[N]
                # print(f'  {k=}')
                while (newName := f'{N}({k})') in nameMap:
                    k += 1
                    # print(f'->{k=}')
            nameMap.setdefault(newName, 1)
            if k:
                nameMap[N] = k + 1
            answers.append(newName)
        # print(f'Ending {nameMap=}')

        return answers
# NOTE: 280 ms; Beats 89.10%
